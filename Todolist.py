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