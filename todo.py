import json

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True

    def display_tasks(self):
        return json.dumps(self.tasks, indent=4)

# Initialize the app
app = TodoApp()

# Add predefined tasks
app.add_task("Buy groceries")
app.add_task("Read a book")
app.add_task("Write some code")

# Complete a task
app.complete_task("Read a book")

# Display tasks
print(app.display_tasks())
