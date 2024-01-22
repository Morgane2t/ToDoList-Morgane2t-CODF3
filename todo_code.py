class Task:
    def __init__(self, name):
        self.name = name
        self.is_completed = False

    def complete(self):
        self.is_completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.complete()
                return True
        return False

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks(self):
        for task in self.tasks:
            status = 'Completed' if task.is_completed else 'Not Completed'
            print(f'Task: {task.name}, Status: {status}')

def main():
    task_manager = TaskManager()
    while True:
        print("1. Add task")
        print("2. Complete task")
        print("3. Delete task")
        print("4. View tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter task name: ")
            task_manager.add_task(name)
        elif choice == '2':
            name = input("Enter task name: ")
            if not task_manager.complete_task(name):
                print("Task not found.")
        elif choice == '3':
            name = input("Enter task name: ")
            if not task_manager.delete_task(name):
                print("Task not found.")
        elif choice == '4':
            task_manager.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()