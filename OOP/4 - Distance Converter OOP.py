import tkinter as tk
from tkinter import ttk
import tkinter.font as font
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class DistanceConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Distance Converter")
        frame = MetersToFeet(self, padding=(60, 30))
        frame.grid()
        self.bind("<Return>", frame.calculate_feet)
        self.bind("<KP_Enter>", frame.calculate_feet)


class MetersToFeet(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        # variable for storing the captured meters
        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar(value="Feet shown here")

        meters_label = ttk.Label(self, text="Meters:")
        meters_input = ttk.Entry(self, width=10, textvariable=self.meters_value, font=("Segoe UI", 15))
        feet_label = ttk.Label(self, text="Feet:")
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text="Calculate", command=self.calculate_feet)

        #layout
        meters_label.grid(column=0, row=0, sticky="w")
        meters_input.grid(column=1, row=0, sticky="ew")
        meters_input.focus()

        feet_label.grid(column=0, row=1, sticky="w")
        feet_display.grid(column=1, row=1, sticky="ew")
        calc_button.grid(column=0, row=2, columnspan=2, sticky="ew")

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

    def calculate_feet(self, *args):
        try:
            meters = float(self.meters_value.get())
            feet = meters * 3.28084
            print(f'{meters} meters is equal to {feet:.3f} feet.')
            self.feet_value.set(f"{feet:.3f}")
        except ValueError:
            print("There was a value error")
            print(f'{self.meters_value.get()} was provided')


root = DistanceConverter()
font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()