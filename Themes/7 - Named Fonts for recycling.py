import tkinter as tk
from tkinter import ttk
import tkinter.font as font
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = tk.Tk()
style = ttk.Style(root)
print(font.families())

warningLabelFont = font.Font(family="Helvetica", size=14, weight="bold").copy()
warningLabelFont.configure(size=15)

name = ttk.Label(root, text="Hello World!", font=warningLabelFont)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press Me!")

name.pack()
entry.pack()
button.pack()


root.mainloop()
