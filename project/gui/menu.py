# GRUPPE 21
import tkinter as tk
from tkinter import filedialog
from os import listdir
import sys
from cvengine.edge import CVEngine
from cvengine import serializer as im
from .db import DB


class MenuView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.db = DB()
        self.cv = CVEngine()
        self.master = master
        self.grid()
        self.create_widgets()

    def get_board(self):
        image_path = tk.filedialog.askopenfilename()
        self.master.set_board_view(image_path)

    def get_nums(self):
        nums = self.db.db.get_numbers()
        self.master.set_db_view(nums)

    def get_syms(self):
        syms = self.db.db.get_symbols()
        self.master.set_db_view(syms)

    def get_images_from_folder(self):
        path = tk.filedialog.askdirectory()
        cards = [self.cv.get_card(im.get(f'{path}/{x}'))
                for x in listdir(path)
                if x[-3:] == 'jpg']
        self.master.set_card_scroller_view(cards)

    def create_widgets(self):
        self.btn_load = tk.Button(self, text='load folder', command=self.get_images_from_folder)
        self.btn_load.grid(row=0, column=0, padx=5, pady=5)

        self.btn_load = tk.Button(self, text='load board', command=self.get_board)
        self.btn_load.grid(row=1, column=0, padx=5, pady=5)

        self.btn_load_syms = tk.Button(self, text='load syms from db', command=self.get_syms)
        self.btn_load_syms.grid(row=2, column=0, padx=5, pady=5)

        self.btn_load_keys = tk.Button(self, text='load nums from db', command=self.get_nums)
        self.btn_load_keys.grid(row=3, column=0, padx=5, pady=5)

        self.btn_exit= tk.Button(self, text='exit', command=sys.exit)
        self.btn_exit.grid(row=4, column=0, padx=5, pady=5)

