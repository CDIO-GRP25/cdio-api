# GRUPPE 21
import tkinter as tk
from PIL import Image, ImageTk
from .db import NumDB, SymDB
from .dbsaveview import DBSaveView


class ImageView(tk.Label):
    def __init__(self, img, dim, pos, master=None):
        super().__init__(master)
        self.master = master
        x,y = pos
        self.grid(row=x, column=y, padx=5, pady=5)
        self.set_image(img.copy(), dim)

    def set_image(self, img, dim):
        img = Image.fromarray(img)
        img = img.resize(dim, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.imgtk = img
        self.config(image=img)


class InfoView(tk.Frame):
    def __init__(self, card, pos, master=None):
        super().__init__(master)
        self.master = master
        x,y = pos
        self.grid(row=x, column=y, padx=5, pady=5)
        self.create_widgets(card)

    def create_widgets(self, card):
        self.num    = ImageView(card.num.img, (50,50), (0,0), master=self)
        self.sym    = ImageView(card.sym.img, (50,50), (0,1), master=self)
        self.db_num = DBSaveView(card.num.img, NumDB(),(1,0), master=self)
        self.db_sym = DBSaveView(card.sym.img, SymDB(),(1,1), master=self)


class DBInfoView(tk.Frame):
    def __init__(self, objects, pos, master=None):
        super().__init__(master)
        x,y = pos
        self.master = master
        self.grid(row=x, column=y, padx=5, pady=5)
        self.create_widgets(objects)

    def create_widgets(self, objects):
        cols = 3
        positions = [(x,y)
                for x in range(len(objects))
                for y in range(cols)][:len(objects)]
        self.objects = [ImageView(obj.img,(50,50), pos, master=self)
                for obj,pos
                in zip(objects, positions)]
