# GRUPPE 21
import os
import tkinter as tk
from database.mongo import MongoDB
from .board import BoardView
from .cardscroller import CardScollerView
from .menu import MenuView
from .dbview import DBView
from . import db


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.focus = MenuView(master=self)

    def set_menu_view(self):
        self.focus.destroy()
        self.create_widgets()

    def set_db_view(self, objects):
        self.focus.destroy()
        self.focus = DBView(objects, master=self)

    def set_board_view(self, image_path):
        self.focus.destroy()
        self.focus = BoardView(image_path, master=self)

    def set_card_scroller_view(self, cards):
        self.focus.destroy()
        self.focus = CardScollerView(cards, master=self)


if __name__ == '__main__':
    root    = tk.Tk()
    app     = Application(master=root)
    root.resizable(width=0, height=0)
    root.title("CDIO - Final Project")
    app.mainloop()
