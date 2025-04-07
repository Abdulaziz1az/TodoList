import json
import os
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.history = []
        self.filename = "tasks.json"
        self.load_tasks()
        
    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f'Task added: {task}')
    
    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.tasks, file)
            print("Tasks saved successfully.")
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.tasks = json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")
        else:
            print(f"{self.filename} not found. Starting wiht an empty task list.")                
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            remove_task = self.tasks.pop(index)
            self.history.append(remove_task)
            print(f'Task removed: {remove_task["task"]}')
        
        else:
            print("Invalid index")
            
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            print(f'Task marked as done: {self.tasks[index]["task"]}')
        else:
            print("Invalid index")
    
    def undo_remove(self):
        if self.history:
            restored_task = self.history.pop()
            self.tasks.append(restored_task)
            print(f'Task restored: { restored_task["task"]}')
        else:
            print("No tasks to restore")
        
    def show_tasks(self):
        if not self.tasks:
            print('No tasks in the list')
        for i, task in enumerate(self.tasks):
            status = 'Done' if task['done'] else 'Pending'
            print(f'{i}. {task["task"]} [{status}]')
            
    def export_tasks(self):
        export_filename = "task_export.txt"
        try:
            with open(export_filename, 'w') as file:
                if not self.tasks:
                    file.write('No tasks in the list\n')
                else:
                    for i, task in enumerate(self.tasks):
                        status = 'Done' if task['done'] else 'Pending'
                        file.write(f'{i}. {task["task"]} [{status}]\n')
            print(f'Tasks exported to {export_filename}')
        except IOError as e:
            print(f"Error exporting tasks: {e}")
    
    def clear_all_tasks(self):
        self.tasks.clear()
        self.history.clear()
        self.save_tasks()
        print("All tasks have been cleard.")