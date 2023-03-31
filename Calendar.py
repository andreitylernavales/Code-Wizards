import calendar


class Calendar:
    def __init__(self):
        self.year = tk.StringVar()
        self.month = tk.StringVar()
        self.year.set(str(calendar.datetime.datetime.now().year))
        self.month.set(str(calendar.datetime.datetime.now().month))

        self.calendar_frame = tk.Frame(self.master)
        self.calendar_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.calendar_frame.configure(bg="#45458B")

    def show_calendar(self):
        year = int(self.year.get())
        month = int(self.month.get())
        var = calendar.monthcalendar(year, month)
        name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        var.insert(0, name)
        for r, row in enumerate(var):
            for c, col in enumerate(row):
                button = tk.Button(self.calendar_frame, text=str(col))
                button.grid(row=r, column=c, padx=10, pady=10)

                
