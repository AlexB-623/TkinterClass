# calls the chat_frames folder

import tkinter as tk
from tkinter import ttk
from collections import deque
from pomodoro_frames import Timer, Settings
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

COLOR_PRIMARY = "#2e3f4f"
COLOR_SECONDARY = "#293846"
COLOR_LIGHT_BACKGROUND = "#fff"
COLOR_LIGHT_TEXT = "#eee"
COLOR_DARK_TEXT = "#8095a8"

class PomodoroTimer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Timer.TFrame", background=COLOR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOR_PRIMARY)
        style.configure(
            "TimerText.TLabel",
            background=COLOR_LIGHT_BACKGROUND,
            foreground=COLOR_DARK_TEXT,
            font="Courier 38"
        )

        style.configure(
            "LightText.TLabel",
            background=COLOR_PRIMARY,
            foreground=COLOR_LIGHT_TEXT
        )

        style.configure(
            "PomodoroButton.TButton",
            background=COLOR_SECONDARY,
            foreground=COLOR_LIGHT_TEXT
        )

        style.map(
            "PomodoroButton.TButton",
            background=[("active", COLOR_PRIMARY), ("disabled", COLOR_LIGHT_TEXT)],
        )

        self["background"] = COLOR_PRIMARY

        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)

        self.timer_order = ["Pomodoro",
                            "Short Break",
                            "Pomodoro",
                            "Short Break",
                            "Pomodoro",
                            "Long Break"]
        self.timer_schedule = deque(self.timer_order)

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = dict()

        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NSEW")
        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NSEW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame

        self.show_frame(Timer)


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


app = PomodoroTimer()
app.mainloop()