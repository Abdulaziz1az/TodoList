class ToDoList:
    def __init__(self):
        self.tasks = []
        self.history = []
        
    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f'Task added: {task}')
    
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
todo = ToDoList()
todo.add_task("complete TODO list")
todo.add_task("Python project")
todo.show_tasks()
todo.mark_done(0)
todo.remove_task(1)
todo.show_tasks()
todo.undo_remove()
todo.show_tasks()