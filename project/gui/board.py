# GRUPPE 21
import tkinter as tk
from itertools import chain
from cvengine import serializer as im
from cvengine.edge import CVEngine
from .components import ImageView
from .cardscroller import CardScollerView
from .db import DB

def make_positions():
    def is_place(x,y): return y!=1 or x!=1 and x!=2
    return list(chain(*[[(x,z)
        for z in y]
        for x,y in enumerate([[x
            for x in range(7) if is_place(x,y)]
            for y in range(2)])]))

class BoardView(tk.Frame):
    def __init__(self, image_path, master=None):
        super().__init__(master)
        self.db = DB()
        cv = CVEngine()
        self.board = cv.gamestate_from_board(self.db.db, im.get(image_path))
        self.master = master
        self.grid()
        self.create_widgets()

    def scroll(self, cards):
        self.scroller = CardScollerView(cards, master=self)

    def exit(self):
        self.master.set_menu_view()

    def create_widgets(self):
        self.cards = [ImageView(card.img,(150,250), pos, master=self)
                for card,pos
                in zip(list(self.board), make_positions())]

        self.btn_exit = tk.Button(self, text='exit', command=self.exit)
        self.btn_exit.grid(row=3, column=0, padx=5, pady=5)

        self.btn_scrollview = tk.Button(self, text='scroll', command=self.scroll)
        self.btn_scrollview.grid(row=4, column=0, padx=5, pady=5)

