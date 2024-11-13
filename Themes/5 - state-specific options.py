import tkinter as tk
from tkinter import ttk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam") #must use custom theme to MAP well (state change in program)
style.map("CustomButton.TButton",
          foreground=[("pressed", "red"), ("active", "white")],
          background=[("pressed", "!disabled", "black"), ("active", "black")],
          font=[("pressed", ("TkDefaultFont", 15))]
          )
name = ttk.Label(root, text="Hello World!")
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press Me!", style="CustomButton.TButton")

name.pack()
entry.pack()
button.pack()


root.mainloop()