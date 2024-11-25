# To-Do List Application using Python

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append({"task": task, "completed": False})
        print(f'Task added: "{task}"')

    def view_tasks(self):
        """View all tasks in the to-do list."""
        if not self.tasks:
            print("No tasks in your to-do list.")
        else:
            print("\nYour To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{idx}. {task['task']} [{status}]")

    def mark_completed(self, task_number):
        """Mark a specific task as completed."""
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task {task_number} marked as completed!')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        """Delete a task from the to-do list."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task removed: "{removed_task["task"]}"')
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        """Clear all tasks from the to-do list."""
        self.tasks.clear()
        print("All tasks cleared!")


def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List Application!")

    while True:
        print("\nChoose an option:")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Clear all tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "5":
            todo_list.clear_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
