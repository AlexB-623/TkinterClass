import tkinter as tk
from tkinter import ttk

def greet():
    #print("Hello World")
    print(f'Hello, {user_name.get() or 'World'}!')

root = tk.Tk()

root.title("Greeter")
user_name = tk.StringVar()

#define variable & type first
input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame,text="Name")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
#defines entry field & assigns it to the variable
name_entry.pack(side="left")
name_entry.focus()
#causes the field to be rendered right away

button_frame = ttk.Frame(root, padding=(20, 10))
button_frame.pack(fill="both")
greet_button = ttk.Button(button_frame, text="Greet", command=greet)
#greet_button.pack(side="left", fill="x")
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(button_frame, text="Quit", command=root.destroy)
#quit_button.pack(side="left", fill="x", expand=True)
quit_button.pack(side="right", fill="x", expand=True)

root.mainloop()
