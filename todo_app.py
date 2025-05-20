import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List App")
        self.root.geometry("500x450")
        self.root.resizable(True, True)
        
        # Set theme colors
        self.bg_color = "#f5f5f5"
        self.highlight_color = "#4caf50"
        self.root.configure(bg=self.bg_color)
        
        # Data file path
        self.data_file = "todo_data.json"
        
        # Load tasks
        self.tasks = self.load_tasks()
        
        # Create UI elements
        self.create_widgets()
        
        # Populate initial tasks
        self.refresh_task_list()
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="Todo List", font=("Arial", 18, "bold"),
                             bg=self.bg_color, fg="#333")
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.pack(fill=tk.X)
        
        # Task entry
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        # Add button
        add_button = tk.Button(input_frame, text="Add Task", font=("Arial", 10, "bold"),
                             bg=self.highlight_color, fg="white", 
                             activebackground="#45a049", cursor="hand2",
                             command=self.add_task)
        add_button.pack(side=tk.RIGHT, padx=(10, 0), ipadx=10, ipady=5)
        
        # Separator
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=15)
        
        # Task list frame with scrollbar
        list_frame = tk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Task listbox with custom formatting
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 12), bd=0,
                                     selectbackground="#a6a6a6", activestyle="none",
                                     highlightthickness=0, relief=tk.FLAT)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Connect scrollbar to listbox
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.bg_color)
        buttons_frame.pack(fill=tk.X, pady=(15, 0))
        
        # Complete button
        complete_btn = tk.Button(buttons_frame, text="Mark Complete", font=("Arial", 10),
                               bg="#3f51b5", fg="white", cursor="hand2",
                               activebackground="#303f9f",
                               command=self.toggle_complete_task)
        complete_btn.pack(side=tk.LEFT, ipadx=10, ipady=5)
        
        # Delete button
        delete_btn = tk.Button(buttons_frame, text="Delete Task", font=("Arial", 10),
                             bg="#f44336", fg="white", cursor="hand2",
                             activebackground="#d32f2f",
                             command=self.delete_task)
        delete_btn.pack(side=tk.RIGHT, ipadx=10, ipady=5)
        
    def add_task(self):
        task_text = self.task_entry.get().strip()
        
        if not task_text:
            messagebox.showwarning("Empty Task", "Please enter a task.")
            return
        
        # Create new task with default status of not completed
        new_task = {"text": task_text, "completed": False}
        self.tasks.append(new_task)
        
        # Clear entry
        self.task_entry.delete(0, tk.END)
        
        # Save and refresh
        self.save_tasks()
        self.refresh_task_list()
        
    def toggle_complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.save_tasks()
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task.")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.refresh_task_list()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task.")
    
    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        
        # Add all tasks with formatting
        for task in self.tasks:
            task_text = task["text"]
            if task["completed"]:
                # Strikethrough effect for completed tasks
                task_display = f"✓ {task_text}"
                self.task_listbox.insert(tk.END, task_display)
                # Get the index of the just-inserted item
                idx = self.task_listbox.size() - 1
                # Configure its foreground color
                self.task_listbox.itemconfig(idx, fg="#888888")
            else:
                task_display = f"□ {task_text}"
                self.task_listbox.insert(tk.END, task_display)
    
    def load_tasks(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_tasks(self):
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.tasks, file)
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
