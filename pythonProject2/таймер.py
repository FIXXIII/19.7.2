import tkinter as tk


class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Таймер")
        self.master.geometry("250x150")
        self.time_left = 0
        self.running = False
        self.timer_label = tk.Label(self.master, text="00:00", font=("Helvetica", 50))
        self.timer_label.pack()
        self.start_button = tk.Button(self.master, text="Старт", command=self.start_timer)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.master, text="Стоп", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

    def start_timer(self):
        if not self.running:
            self.time_left = 120
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.update_timer()

    def stop_timer(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.time_left > 0 and self.running:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            time_string = "{:02d}:{:02d}".format(minutes, seconds)
            self.timer_label.config(text=time_string)
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.stop_timer()


if __name__ == "__main__":
    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()