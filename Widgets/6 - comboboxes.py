import tkinter as tk
from calendar import weekday
from tabnanny import check
from tkinter import ttk, StringVar
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

selected_weekday = StringVar()

weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday["values"] = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Extraday")
weekday["state"] = "readonly"
weekday.pack()

def handle_selection(event):
    print(f'Today is {selected_weekday.get()}')
    print("But we're gonna change it to Friday")
    selected_weekday.set("Friday")
    print(weekday.set)

weekday.bind("<<ComboboxSelected>>", handle_selection)


root.mainloop()

print(selected_weekday.get(), "was selected")