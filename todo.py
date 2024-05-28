import json

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def add_task(description):
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks()

def list_tasks():
    for task in tasks:
        status = "✓" if task["completed"] else "✗"
        print(f"{task['id']}. {task['description']} [{status}]")

def update_task(task_id, description):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            save_tasks()
            return
    print("Task not found.")

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks()
            return
    print("Task not found.")

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks()

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            description = input("Enter task description: ")
            add_task(description)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            description = input("Enter new description: ")
            update_task(task_id, description)
        elif choice == "4":
            task_id = int(input("Enter task ID to complete: "))
            complete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
