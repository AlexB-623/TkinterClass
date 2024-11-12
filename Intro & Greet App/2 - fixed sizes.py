import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rect 1", bg="blue", fg="white")
#rectangle_1.pack(ipadx=10, ipady=10, fill="y", expand=True)
#since these are aligned to top by default, the fill y pushes it to the bottom

rectangle_1.pack(side="left", ipadx=10, ipady=10, fill="both")

rectangle_2 = tk.Label(root, text="Rect 2", bg="red", fg="white")
#rectangle_2.pack(ipadx=10, ipady=10, fill="x")
#fill = x means take up all horizontal space allocated

rectangle_2.pack(ipadx=10, ipady=10, fill="both")
#alternatively, fill="both" does both x & y
#removing fill and sticking with expand, causes centering
#omitting a side value can cause odd alignment issues

#expansion priority = adding expand=True to both means the first one to be added gets priority,
# leaving minimal space to the one on the left
root.mainloop()