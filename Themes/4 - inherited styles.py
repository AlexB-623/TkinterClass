import tkinter as tk
from tkinter import ttk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
style =ttk.Style(root)
style.configure("CustomEntryStyle.TEntry", padding=20)

name = ttk.Label(root, text="Hello World!")
entry = ttk.Entry(root, width=15)
entry["style"] = "CustomEntryStyle.TEntry"
name.pack()
entry.pack()

entry2 = ttk.Entry(root, width=15)
entry2.pack()

root.mainloop()