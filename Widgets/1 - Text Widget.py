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

text = tk.Text(root, height=8)
text.pack()

text.insert("1.0", "Please enter a comment...")
text["state"] = "normal"
#greytext - 1.0 means first line, char 0

text_content = text.get("1.0", "end")
print(text_content)
#runs once
root.mainloop()