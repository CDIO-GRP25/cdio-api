# GRUPPE 21
from .cornerobject import CornerObject
import json
import numpy as np

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self.__dict__)
    def __repr__(self):
        return self.toJson()

class Card(JsonSerializable):
    def __init__(self, card, num, sym):
        self.img = card
        self.num = CornerObject(num)
        self.sym = CornerObject(sym)

    def find_values(self, nums, syms):
        self.num.find_value(nums)
        self.sym.find_value(syms)

    def __repr__(self):
        return f'Card({self.sym.val}{self.num.val})'

    def __str__(self):
        return f'{self.sym.val}{self.num.val}'

class EmptyCard(Card):
    def __init__(self):
        img = np.zeros((200,300,3), np.uint8)
        num = np.zeros((10,10,3), np.uint8)
        sym = np.zeros((10,10,3), np.uint8)
        Card.__init__(self, img, num, sym)

    def find_values(self, nums, syms):
        pass

    def __repr__(self):
        return f'Card()'

    def __str__(self):
        return ''
