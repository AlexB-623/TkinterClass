import tkinter as tk
from tkinter import ttk
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
style =ttk.Style(root)

name = ttk.Label(root, text="Hello World!")
entry = ttk.Entry(root, width=15)
name.pack()

#print(name["style"]) #no result = default
print(name.winfo_class()) #returns TLabel



root.mainloop()