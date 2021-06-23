# GRUPPE 21
import os
import tkinter as tk
from database.mongo import MongoDB


class DB:
    def __init__(self):
        uri = os.environ['CDIO_MONGO_PASS']
        self.db = MongoDB(uri)


class NumDB(DB):
    def __init__(self):
        DB.__init__(self)
        self.options = [
                "A",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                ]
    def save(self, img, val):
        self.db.save_number(img, val)


class SymDB(DB):
    def __init__(self):
        DB.__init__(self)
        self.options = [
                "S",
                "D",
                "C",
                "H",
                ]
    def save(self, img, val):
        self.db.save_symbol(img, val)
