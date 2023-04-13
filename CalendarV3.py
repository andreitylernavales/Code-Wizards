import datetime
import calendar
from time import strftime, localtime


    def create_calendar(self):
        for widget in self.calendar.winfo_children():
            widget.destroy()
        if self.year_entry.get():
            try:
                self.current_year = int(self.year_entry.get())
            except ValueError:
                pass

        if self.month_entry.get():
            try:
                self.current_month = int(self.month_entry.get())
            except ValueError:
                pass

        month_name = calendar.month_name[self.current_month]
        header_text = f"{month_name} {self.current_year}"
        self.header.config(text=header_text)
        self.header.grid(row=3, column=6)
        weekday_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, weekday_name in enumerate(weekday_names):
            label = tk.Label(self.calendar, text=weekday_name, bg="#5e5c5c", font=("Ariel", 13, "bold"))
            label.grid(row=0, column=i, padx=5, pady=5)

        data = calendar.monthcalendar(self.current_year, self.current_month)

        holidays = {
            "New Year's Day": (1, 1),
            "Araw ng Kagitingan": (4, 9),
            "Maundy Thursday": None,
            "Good Friday": None,
            "Labor Day": (5, 1),
            "Independence Day": (6, 12),
            "National Heroes Day": (8, 30),
            "Bonifacio Day": (11, 30),
            "Christmas Day": (12, 25),
            "Rizal Day": (12, 30),
        }

        for i, week in enumerate(data):
            for j, day in enumerate(week):
                if day != 0:
                    button = tk.Button(self.calendar, text=day, bg="#333333", fg="white", width=4, height=2)
                    button.grid(row=i + 1, column=j, padx=5, pady=5)
                    if (j + 1) % 7 == 0:
                        button.config(bg="#8B0000", fg="white")

                    if day == datetime.date.today().day and self.current_month == datetime.date.today().month and self.current_year == datetime.date.today().year:
                        button.config(bg="#023020")

                    # check if current day is a holiday
                    for holiday, date in holidays.items():
                        if date is not None and date[0] == self.current_month and day == date[1]:
                            button.config(bg="#db3445")
                            break

