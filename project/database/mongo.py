# GRUPPE 21
import numpy as np
import pickle
from pymongo import MongoClient
from bson.binary import Binary
from models.cornerobject import CornerObject


class MongoDB:
    def __init__(self, uri):
        self.db  = MongoClient(uri)['cdio']

    def save_number(self, image, value): self.__save_one(image, value, self.db['numbers'])
    def save_symbol(self, image, value): self.__save_one(image, value, self.db['symbols'])

    def get_numbers(self):
        return self.__get_all(self.db['numbers'])

    def get_symbols(self):
        return self.__get_all(self.db['symbols'])

    def __img_to_binary(self, img):
        return Binary(pickle.dumps(img, protocol=2), subtype=128)

    def __binary_to_img(self, binary):
        return pickle.loads(binary)

    def __get_all(self, col):
        return [CornerObject(self.__binary_to_img(x['image']), x['value'])
                for x in col.find()]

    def __save_one(self, image, value, col):
        return col.insert_one({
                'image': self.__img_to_binary(image),
                'value': value,
                })

