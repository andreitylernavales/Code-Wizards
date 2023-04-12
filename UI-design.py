import tkinter as tk
from tkinter import font


class CalendarGUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("My_Calendar_UI_design")
        self.parent.geometry("1200x800")
        self.parent.configure(bg="#6E6E6E")
        self.month_entry = tk.Entry()

        self.current_month = datetime.date.today().month
        self.current_year = datetime.date.today().year

        self.time_label = tk.Label(self.parent, font=("Times New Roman", 30), fg="white", bg="#333333")
        self.time_label.grid(row=0, column=2, pady=15)

        self.update_clock()

        self.label = tk.Label(self.parent, text="CODE_WIZARDS", font=("Times New Roman", 40, "bold"), fg="#FFFF00",
                              bg="#6E6E6E")
        self.label.grid(row=0, column=6, padx=5, pady=5)

        self.year_label = tk.Label(self.parent, text="Years:", fg="black", bg="#6E6E6E", font=("Ariel", 10, "bold"))
        self.year_label.grid(row=3, column=1, padx=10, pady=10)
        self.year_entry = tk.Entry(self.parent, bg="#6E6E6E", font=("calibre", 15))
        self.year_entry.grid(row=3, column=2, padx=10, pady=10)

        self.search_button = tk.Button(self.parent, text="Show Calendar", command=self.create_calendar, fg="black",
                                       bg="#6E6E6E", font=("Ariel", 10, "bold"))
        self.search_button.grid(row=3, column=3, padx=10, pady=10)


root = tk.Tk()
MyUI = MyUI(root)
root.mainloop()

