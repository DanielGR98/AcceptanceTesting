class Task:
    def __init__(self, title, status="Pending"):
        self.title = title
        self.status = status

class TodoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def list_tasks(self):
        return [task.title for task in self.tasks]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "Completed"
                break

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    manager = TodoListManager()
    
