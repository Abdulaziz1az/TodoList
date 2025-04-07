from Todolist import  ToDoList
def main():
    todo = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Undo Remove")
        print("5. Show Task")
        print("6. Export Tasks to File")
        print("7. Clear All Tasks")
        print("8. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo.add_task(task)
            
        elif choice == '2':
            todo.show_tasks()
            index = int(input("Enter the task index to remove: "))
            todo.remove_task(index)
            
        elif choice == '3':
            todo.show_tasks()
            index = int(input("Enter the task index to mark as done: "))
            todo.mark_done(index)
            
        elif choice == '4':
            todo.undo_remove()
            
        elif choice == '5':
            todo.show_tasks()
            
        elif choice == '6':
            todo.export_tasks()
            
        elif choice == '7':
            todo.clear_all_tasks()
        
        elif choice == '8':
            print("Exiting the To-Do List program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            
if  __name__ =="__main__":
    main()