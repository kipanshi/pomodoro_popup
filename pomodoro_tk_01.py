import tkinter as tk
from tkinter import messagebox
import time

class PomodoroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro App")
        
        self.timer_label = tk.Label(self.master, text="25:00", font=("Arial", 24))
        self.timer_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=1, column=1, padx=5, pady=5)

        self.time_remaining = 1500  # 25 minutes in seconds
        self.is_running = False

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.countdown()

    def countdown(self):
        if self.time_remaining <= 0:
            self.is_running = False
            messagebox.showinfo("Pomodoro", "Time's up!")
            return

        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.configure(text=time_str)

        self.time_remaining -= 1
        self.master.after(1000, self.countdown)

    def reset_timer(self):
        self.is_running = False
        self.time_remaining = 1500
        self.timer_label.configure(text="25:00")


if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
