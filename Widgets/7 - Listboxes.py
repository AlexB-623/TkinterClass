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

programming_languages = ("C", "Go", "JavaScript", "Perl", "Python", "Rust")

langs = tk.StringVar(value=programming_languages)
langs_select = tk.Listbox(root, listvariable=langs, height=6, selectmode="extended")
langs_select.pack()

def handle_selection_changes(event):
    selected_indices = langs_select.curselection()
    for i in selected_indices:
        print(langs_select.get(i))

langs_select.bind("<<ListboxSelect>>", handle_selection_changes)

root.mainloop()