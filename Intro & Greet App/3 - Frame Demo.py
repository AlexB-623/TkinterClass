import tkinter as tk
from tkinter import ttk
root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)
# here we create a top-level container and pack the labels into it
tk.Label(main, text="TOP", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(main, text="TOP", bg="red").pack(side="top", expand=True, fill="both")
#this label is still in Root, outside the container
tk.Label(root, text="LEFT", bg="green").pack(side="left", expand=True, fill="both")

root.mainloop()