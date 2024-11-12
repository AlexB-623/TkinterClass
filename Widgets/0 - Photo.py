import tkinter as tk
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

image = Image.open("Summer.jpeg").resize((75, 75))
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Image with text", image=photo, padding=5, compound="left")
label.pack()

root.mainloop()