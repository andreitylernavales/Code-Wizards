    def prev_month(self):
       if self.current_month == 1:
           self.current_month = 12
           self.current_year -= 1
       else:
           self.current_month -= 1

       self.create_calendar()


    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1

        self.create_calendar()


    def go_to_today(self):
        self.current_month = datetime.date.today().month
        self.current_year = datetime.date.today().year

        self.create_calendar()


    def update_clock(self):
        current_time = strftime('%I:%M:%S %p', localtime())
        self.time_label.config(text=current_time)
        self.parent.after(1000, self.update_clock)