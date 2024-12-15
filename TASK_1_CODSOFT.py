class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "[Done]" if task["completed"] else "[Pending]"
                print(f"{idx}. {task['task']} {status}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]["task"]
            self.tasks[index]["task"] = new_task
            print(f'Task "{old_task}" updated to "{new_task}" successfully.')
        else:
            print("Invalid task number.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f'Task "{self.tasks[index]["task"]}" marked as complete.')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task["task"]}" deleted successfully.')
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Clear All Tasks")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == 2:
            todo_list.view_tasks()

        elif choice == 3:
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to update: ")) - 1
                new_task = input("Enter the updated task: ")
                todo_list.update_task(index, new_task)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == 4:
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to mark as complete: ")) - 1
                todo_list.mark_task_complete(index)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == 5:
            todo_list.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(index)
            except ValueError:
                print("Please enter a valid task number.")

        elif choice == 6:
            todo_list.clear_tasks()

        elif choice == 7:
            print("Exiting To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()