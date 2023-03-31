import tkinter as tk
from tkinter import font


class MyUI:
    def __init__(self, master):
        self.master = master
        self.master.title("My_Calendar_UI_design")
        self.master.geometry("1000x1000")
        self.master.configure(bg="#ecc19c")

        self.custom_font = font.Font(family="Times New Roman", size=40, weight="bold")

        self.label = tk.Label(self.master, text="CODE_WIZARDS", font=self.custom_font, fg="#FFFF00", bg="#3b4d61")
        self.label.grid(row=0, column=6, padx=5, pady=5)

        self.year_label = tk.Label(self.master, text="Years:", fg="white", bg="#0000FF")
        self.year_label.grid(row=1, column=0, padx=5, pady=5)
        self.year_entry = tk.Entry(self.master, bg="#40E0D0")
        self.year_entry.grid(row=1, column=1, padx=5, pady=5)
        self.month_label = tk.Label(self.master, text="Months:", fg="black", bg="#00FF00")
        self.month_label.grid(row=2, column=0, padx=5, pady=5)
        self.month_entry = tk.Entry(self.master, bg="#40E0D0")
        self.month_entry.grid(row=2, column=1, padx=5, pady=5)
        self.search_button = tk.Button(self.master, text="Show Calendar", fg="black", bg="#FF0000")
        self.search_button.grid(row=2, column=3, padx=5, pady=5)


root = tk.Tk()
MyUI = MyUI(root)
root.mainloop()
