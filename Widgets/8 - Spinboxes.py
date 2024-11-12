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

initial_value = tk.IntVar(value=20)
spin_box = ttk.Spinbox(
    root,
    #from_=0,
    #to=30,
    values=(5, 10, 15, 20, 25),
    textvariable=initial_value,
    wrap=False #prevents return to 0
)
spin_box.pack()

print(spin_box.get())


root.mainloop()