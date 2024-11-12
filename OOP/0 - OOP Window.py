import tkinter as tk
from tkinter import ttk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello world!")
        ttk.Label(self, text="Hello World!").pack()


root = HelloWorld()

root.mainloop()