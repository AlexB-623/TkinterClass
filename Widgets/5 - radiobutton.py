import tkinter as tk
from tabnanny import check
from tkinter import ttk
from PIL import Image, ImageTk
#Make text look better with DPI (Windows only)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x400")
root.resizable=(False, False)
root.title("Widget Examples")

storage_variable = tk.StringVar()

option_one = ttk.Radiobutton(
    root,
    text="Option 1",
    variable=storage_variable,
    value="1st Option"
)

option_two = ttk.Radiobutton(
    root,
    text="Option 2",
    variable=storage_variable,
    value="2nd Option"
)

option_three = ttk.Radiobutton(
    root,
    text="Option 3",
    variable=storage_variable,
    value="3rd Option"
)

option_one.pack()
option_two.pack()
option_three.pack()

root.mainloop()