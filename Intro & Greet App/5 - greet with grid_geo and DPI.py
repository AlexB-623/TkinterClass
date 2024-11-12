import tkinter as tk
from tkinter import ttk
#Make text look better with DPI (Windows only)
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def greet():
    print(f'Hello, {user_name.get() or 'World'}!')

root = tk.Tk()
root.title("Greeter")
root.columnconfigure(0, weight=1)

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky="EW")
#grid with no argument means objects get put into the first row/column
#no arguments = all vertical

name_label = ttk.Label(input_frame,text="Name: ")
name_label.grid(row=0, column=0, padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()


buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(sticky="EW")
#sticky forces the grid to stay on one side, EW are East West

buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()