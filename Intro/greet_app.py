import tkinter as tk
from tkinter import ttk

def greet():
    #print("Hello World")
    print(f'Hello, {user_name.get() or 'World'}!')

root = tk.Tk()

user_name = tk.StringVar()
#define variable & type first

name_label = ttk.Label(root,text="Name")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
#defines entry field & assigns it to the variable

name_entry.pack(side="left")
name_entry.focus()
#cases the field to be rendered right away

greet_button = ttk.Button(root, text="Greet", command=greet)
#greet_button.pack(side="left", fill="x", expand=True)
greet_button.pack(side="left")

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
#quit_button.pack(side="left", fill="x", expand=True)
quit_button.pack(side="right")

root.mainloop()
