import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os
import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # Create a custom style for widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Arial", 12))
        self.style.configure("TButton", font=("Arial", 12))

        self.category_label = ttk.Label(root, text="Category:")
        self.amount_label = ttk.Label(root, text="Amount (ZAR):")
        self.date_label = ttk.Label(root, text="Date (YYYY-MM-DD):")

        self.category_entry = ttk.Entry(root, font=("Arial", 12))
        self.amount_entry = ttk.Entry(root, font=("Arial", 12))
        self.date_entry = ttk.Entry(root, font=("Arial", 12))

        self.record_button = ttk.Button(root, text="Record Expense", command=self.record_expense)
        self.view_button = ttk.Button(root, text="View Expenses", command=self.view_expenses)

        self.category_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.amount_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.date_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.category_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.amount_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.date_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.record_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def record_expense(self):
        category = self.category_entry.get()
        amount = self.amount_entry.get()
        date = self.date_entry.get()

        if not category or not amount or not date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            amount = float(amount)
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid amount or date format.")
            return

        filename = f"{os.getlogin()}_expenses.csv"
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, f"ZAR {amount:.2f}"])

        messagebox.showinfo("Success", "Expense recorded successfully!")

        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)

    def view_expenses(self):
        filename = f"{os.getlogin()}_expenses.csv"
        if not os.path.exists(filename):
            messagebox.showinfo("Info", "No expenses recorded yet.")
            return

        expenses_window = tk.Toplevel(self.root)
        expenses_window.title("Expenses")

        tree = ttk.Treeview(expenses_window, columns=("Date", "Category", "Amount"))
        tree.heading("#1", text="Date")
        tree.heading("#2", text="Category")
        tree.heading("#3", text="Amount")

        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                tree.insert("", "end", values=(row[0], row[1], row[2]))

        tree.pack()

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
