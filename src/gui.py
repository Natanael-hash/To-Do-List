import tkinter as tk
from tkinter import messagebox, ttk
from src.task_manager import TaskManager


class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("800x600")

        self.task_manager = TaskManager()
        self.create_widgets()
        self.refresh_listbox()

    def create_widgets(self):

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        self.task_entry = tk.Entry(input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, expand=True)

        add_btn = tk.Button(input_frame, text="Adaugă", command=self.on_add_task)
        add_btn.pack(side=tk.LEFT, padx=5)


        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)

        self.tasks_listbox = tk.Listbox(list_frame, width=50, height=15)
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tasks_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_listbox.config(yscrollcommand=scrollbar.set)


        delete_btn = tk.Button(self.root, text="Șterge sarcina selectată", command=self.on_delete_task)
        delete_btn.pack(pady=5)

    def on_add_task(self):
        task_name = self.task_entry.get()
        try:
            new_id = self.task_manager.add_task(task_name)
            self.task_entry.delete(0, tk.END)
            self.refresh_listbox()
            messagebox.showinfo("Succes", f"Sarcina adăugată cu ID-ul {new_id}")
        except ValueError as e:
            messagebox.showerror("Eroare", str(e))

    def on_delete_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            selected_task = self.tasks_listbox.get(selected_index)
            task_id = int(selected_task.split(" - ")[0].split(": ")[1])

            if self.task_manager.delete_task(task_id):
                self.refresh_listbox()
                messagebox.showinfo("Succes", "Sarcina ștearsă cu succes!")
            else:
                messagebox.showerror("Eroare", "ID-ul sarcinii nu a fost găsit!")
        except IndexError:
            messagebox.showerror("Eroare", "Te rog selectează o sarcină!")

    def refresh_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.task_manager.all_tasks:
            self.tasks_listbox.insert(tk.END, f"ID: {task['id']} - {task['sarcina']}")