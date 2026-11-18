
class StudentTaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty")

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

        task = {
            "id": self.next_id,
            "title": title.strip(),
            "completed": False
        }

        self.tasks.append(task)
        self.next_id += 1
        return task

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "Completed" if task["completed"] else "Pending"
            print(f'{task["id"]}. {task["title"]} - {status}')
# Marks an existing task as completed only once.
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task is already completed.")
                    return False

                task["completed"] = True
                return True

        return False
    # Deletes a task only when its identifier is valid.
    def delete_task(self, task_id):
        if not isinstance(task_id, int) or task_id < 1:
            return False

        for task in self.tasks:
         if task["id"] == task_id:
                self.tasks.remove(task)
                return True

        return False


def main():
    manager = StudentTaskManager()

    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Enter task title: ")
                manager.add_task(title)
                print("Task added successfully!")

            elif choice == "2":
                manager.display_tasks()

            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                print("Completed!" if manager.complete_task(task_id) else "Invalid ID")

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                print("Deleted!" if manager.delete_task(task_id) else "Invalid ID")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Invalid choice!")

        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
