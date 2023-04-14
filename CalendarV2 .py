        self.search_button = tk.Button(self.parent, text="Show Calendar", command=self.create_calendar, fg="white",
                                       bg="#5e5c5c", font=("Ariel", 10, "bold"))
        self.search_button.grid(row=1, column=2, padx=10, pady=10)

        self.letter = tk.Label(self.parent, text="CALENDAR", font=("Times New Roman", 30, "bold"), fg="#FFFF00",
                               bg="#5e5c5c")
        self.header = tk.Label(self.parent, bg="#5e5c5c", font=("Times New Roman", 20, "bold"))
        self.header.grid(row=3, column=6, padx=6, pady=5)

        self.calendar = tk.Frame(self.parent, bg="#5e5c5c")
        self.calendar.grid(row=4, column=6, columnspan=2, pady=5, padx=5)
        self.create_calendar()

        self.navigation = tk.Frame(self.parent, bg="#5e5c5c")
        self.navigation.grid(row=6, column=6, padx=5, pady=5)

        tk.Button(self.navigation, text="Prev Month", command=self.prev_month, bg="#5e5c5c",
                  font=("Ariel", 10, "bold")).pack(side="left", pady=5, padx=5)
        tk.Button(self.navigation, text="Next Month", command=self.next_month, bg="#5e5c5c",
                  font=("Ariel", 10, "bold")).pack(side="left", pady=5, padx=5)
        tk.Button(self.navigation, text="Today", command=self.go_to_today, bg="#5e5c5c",
                  font=("Ariel", 10, "bold")).pack(side="left", pady=5, padx=5)
        
        
