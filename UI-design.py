import tkinter as tk
from tkinter import ttk

gray_bg = '#5e5c5c'

darkgray_bg = '#333333'


def Switch_theme():
    current_theme = root.cget('bg')
    if current_theme == gray_bg:
        root.config(bg=darkgray_bg)
        for widget in root.winfo_children():
            widget.config(bg=darkgray_bg)
    else:
        root.config(bg=gray_bg)
        for widget in root.winfo_children():
            widget.config(bg=gray_bg)


class CalendarGUI:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("My_Calendar_UI")
        self.parent.geometry("1200x800")
        self.parent.configure(bg="#5e5c5c")
        self.month_entry = tk.Entry()
        self.events = []

        self.current_month = datetime.date.today().month
        self.current_year = datetime.date.today().year

        self.time_label = tk.Label(self.parent, font=("Times New Roman", 30, "bold"), fg="black", bg="#5e5c5c")
        self.time_label.grid(row=0, column=1, pady=15)
        self.update_clock()

        self.label = tk.Label(self.parent, text="CODE_WIZARDS", font=("Times New Roman", 40, "bold"), fg="#FFFF00",
                              bg="#5e5c5c")
        self.label.grid(row=0, column=6, padx=5, pady=5)

        self.year_label = tk.Label(self.parent, text="Search Years:", fg="black", bg="#5e5c5c", font=("Times New Roman", 15, "bold"))
        self.year_label.grid(row=1, column=0, padx=10, pady=10)
        self.year_entry = tk.Entry(self.parent, bg="#36454F", font=("calibre", 15, "bold"))
        self.year_entry.grid(row=1, column=1, padx=10, pady=10)


root = tk.Tk()
MyUI = CalendarGUI(root)
root.mainloop()
