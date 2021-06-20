from cvengine import edge as im
import os
import tkinter as tk
from database.mongo import MongoDB
from .board import BoardView
from .cardscroller import CardScollerView
from .menu import MenuView


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

    def set_board_view(self, image_path):
        self.focus.destroy()
        self.focus = BoardView(image_path, master=self)

    def set_card_scroller_view(self, images):
        self.focus.destroy()
        self.focus = CardScollerView(images, master=self)


if __name__ == '__main__':
    root    = tk.Tk()
    app     = Application(master=root)
    root.resizable(width=0, height=0)
    root.title("CDIO - Final Project")
    app.mainloop()