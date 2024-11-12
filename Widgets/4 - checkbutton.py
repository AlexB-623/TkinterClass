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

check_button = ttk.Checkbutton(root, text="Check me, Captain!")
check_button.pack()

check_button["state"] = "normal"

selected_option = tk.StringVar()

def print_current_option():
    print(selected_option.get())

check = ttk.Checkbutton(
    root,
    text="Check Example",
    variable=selected_option,
    command=print_current_option,
    onvalue="On",
    offvalue="Off"
)

check.pack()

root.mainloop()