# GRUPPE 21
import tkinter as tk

class DBSaveView(tk.Frame):
    def __init__(self, image, db, pos, master=None):
        super().__init__(master)
        x, y            = pos
        self.image      = image
        self.db         = db
        self.master     = master
        self.choice     = tk.StringVar(self)

        self.grid(row=x, column=y)
        self.choice.set(self.db.options[0])

        self.create_widgets()

    def save_choice(self):
        self.db.save(self.image, self.choice.get())

    def create_widgets(self):
        self.menu   = tk.OptionMenu(self,self.choice, *self.db.options)
        self.btn    = tk.Button(self, text="save", command=self.save_choice)
        self.menu.grid(row=0, column=0, padx=5,pady=5)
        self.btn.grid(row=0, column=1, padx=5,pady=5)

