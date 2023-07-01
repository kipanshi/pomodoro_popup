import tkinter as tk
import tkinter.font as font
import time

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        
        self.timer_label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

        self.time_left = 0
        self.timer_running = False

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.DISABLED)
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.time_left = 0
        self.update_timer()

    def update_timer(self):
        minutes, seconds = divmod(self.time_left, 60)
        hours, minutes = divmod(minutes, 60)
        timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_label.configure(text=timer_text)
        
        if self.time_left > 0 and self.timer_running:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)

    def start_pomodoro(self):
        self.time_left = 25 * 60  # 25 minutes
        self.start_timer()

    def start_short_break(self):
        self.time_left = 5 * 60  # 5 minutes
        self.start_timer()

    def start_long_break(self):
        self.time_left = 15 * 60  # 15 minutes
        self.start_timer()

root = tk.Tk()
pomodoro_app = PomodoroApp(root)

start_pomodoro_button = tk.Button(root, text="Start Pomodoro", command=pomodoro_app.start_pomodoro)
start_pomodoro_button.pack(pady=5)

start_short_break_button = tk.Button(root, text="Start Short Break", command=pomodoro_app.start_short_break)
start_short_break_button.pack(pady=5)

start_long_break_button = tk.Button(root, text="Start Long Break", command=pomodoro_app.start_long_break)
start_long_break_button.pack(pady=5)

root.mainloop()
