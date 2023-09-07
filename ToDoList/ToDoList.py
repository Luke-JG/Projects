import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("Modern To-Do List")
root.geometry("400x400")
root.config(bg="#f4f4f4")

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 24), bg="#f4f4f4")
title_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
task_entry.pack(pady=10)

# Add Button
add_button = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#007acc", fg="#ffffff")
add_button.pack()

# Remove Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Helvetica", 12), bg="#ff4444", fg="#ffffff")
remove_button.pack()

# Task Listbox
task_listbox = tk.Listbox(root, width=40, height=10, font=("Helvetica", 12))
task_listbox.pack(pady=10)

root.mainloop()
