import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text="Hello World", padding=(30, 10)).pack()
#.pack puts the element into the window (root)

root.mainloop()
