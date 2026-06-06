# List to store tasks
tasks = []


# Function to display menu
def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")
    print("================================")


# Function to view tasks
def view_tasks():

    if len(tasks) == 0:
        print("\nNo tasks available.")

    else:
        print("\nYour Tasks:\n")

        for index, task in enumerate(tasks, start=1):

            status = "✓" if task["completed"] else "✗"

            print(f"{index}. [{status}] {task['title']}")


# Function to add a task
def add_task():

    task_name = input("\nEnter task name: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    task = {
        "title": task_name,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


# Function to update task
def update_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to update: "))

        if 1 <= task_number <= len(tasks):

            new_task = input("Enter new task name: ").strip()

            if new_task == "":
                print("Task cannot be empty.")
                return

            tasks[task_number - 1]["title"] = new_task

            print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Function to delete task
def delete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            removed_task = tasks.pop(task_number - 1)

            print(f"Deleted task: {removed_task['title']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Function to mark task as completed
def complete_task():

    view_tasks()

    if len(tasks) == 0:
        return

    try:
        task_number = int(input("\nEnter task number to mark completed: "))

        if 1 <= task_number <= len(tasks):

            tasks[task_number - 1]["completed"] = True

            print("Task marked as completed!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main Program Loop
while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("\nThank you for using To-Do List Application!")
        break

    else:
        print("Invalid choice. Please try again.")