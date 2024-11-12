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

def scale_change(event):
    print(scale.get())

scale = ttk.Scale(root, orient="horizontal", from_=0, to=10, command=scale_change)
scale.pack(fill="x")

root.mainloop()