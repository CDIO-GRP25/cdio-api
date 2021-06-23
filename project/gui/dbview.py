# GRUPPE 21
import tkinter as tk
from cvengine import edge as im
from .components import ImageView, InfoView, DBInfoView

class DBView(tk.Frame):
    def __init__(self, corner_objects, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.keys = [x.val for x in corner_objects]
        self.corner_objects = self.sort(corner_objects)
        self.index = 0
        self.create_widgets()
        self.showtime()

    def sort(self, corner_objects):
        return {k: [x for x in corner_objects if x.val == k] for k in self.keys}

    def go_left(self):
        self.index = (self.index+1)%len(self.keys)
        self.info.destroy()
        self.showtime()

    def go_right(self):
        self.index = (self.index-1)%len(self.keys)
        self.info.destroy()
        self.showtime()

    def showtime(self):
        objects     = self.corner_objects[self.keys[self.index]]
        self.info   = DBInfoView(objects, (1,1), master=self)

    def exit(self):
        self.master.set_menu_view()

    def create_widgets(self):
        self.btn_left = tk.Button(self, text='<', command=self.go_left, height=10)
        self.btn_left.grid(row=1, column=0, padx=5, pady=5)

        self.btn_right = tk.Button(self, text='>', command=self.go_right, height=10)
        self.btn_right.grid(row=1, column=2, padx=5, pady=5)

        self.btn_exit = tk.Button(self, text='exit', command=self.exit)
        self.btn_exit.grid(row=2, column=1, padx=5, pady=5)
