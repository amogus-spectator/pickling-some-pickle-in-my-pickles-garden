import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.priority = priority

    def urgency_score(self):
        days_left = (self.deadline - datetime.now()).days
        priority_weight = {"low": 1, "medium": 2, "high": 3}[self.priority]
        return (days_left+1) * priority_weight

    def __str__(self):
        return f"{self.name} (Deadline: {self.deadline.strftime('%Y-%m-%d')}, Priority: {self.priority})"

class TaskManager:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("Task Prioritizer")

        # Input Fields
        self.name_label = tk.Label(root, text="Task Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.deadline_label = tk.Label(root, text="Deadline (YYYY-MM-DD):")
        self.deadline_label.grid(row=1, column=0, padx=5, pady=5)
        self.deadline_entry = tk.Entry(root)
        self.deadline_entry.grid(row=1, column=1, padx=5, pady=5)

        self.priority_label = tk.Label(root, text="Priority (low, medium, high):")
        self.priority_label.grid(row=2, column=0, padx=5, pady=5)
        self.priority_entry = tk.Entry(root)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.display_button = tk.Button(root, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=5)

        # Task Display
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=5, column=0, columnspan=2, pady=5)

    def add_task(self):
        name = self.name_entry.get()
        deadline = self.deadline_entry.get()
        priority = self.priority_entry.get().lower()

        if not name or not deadline or not priority:
            messagebox.showerror("Input Error", "All fields are required!")
            return

        try:
            new_task = Task(name, deadline, priority)
            self.tasks.append(new_task)
            self.name_entry.delete(0, tk.END)
            self.deadline_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Task added successfully!")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid date format. Use YYYY-MM-DD.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        sorted_tasks = sorted(self.tasks, key=lambda t: t.urgency_score(), reverse=True)
        for task in sorted_tasks:
            self.task_listbox.insert(tk.END, str(task))

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
