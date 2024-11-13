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
name.pack()


print(style.layout("TLabel"))
#('Label.border', {'sticky': 'nswe', 'border': '1', 'children': [('Label.padding', {'sticky': 'nswe', 'border': '1', 'children': [('Label.label', {'sticky': 'nswe'})]})]})

print("default")
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound")) #not set, so no value returned

style.theme_use("clam")
print("Clam Jam")
print(style.element_options("Label.border"))
print(style.element_options("Label.padding"))
print(style.element_options("Label.label"))

print(style.lookup("TLabel", "font"))
print(style.lookup("TLabel", "foreground"))
print(style.lookup("TLabel", "compound"))

style.configure("TLabel", bordercolor="#f00")
style.configure("TLabel", borderwidth=20)
style.configure("TLabel", relief="solid") # requires border

root.mainloop()