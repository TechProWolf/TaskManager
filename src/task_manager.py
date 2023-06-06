from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, title, due_date, priority):
        task = Task(title, due_date, priority)
        self.tasks.append(task)

    def update_task(self, task_index, **kwargs):
        task = self.tasks[task_index]
        for key, value in kwargs.items():
            setattr(task, key, value)

    def complete_task(self, task_index):
        task = self.tasks[task_index]
        task.mark_as_completed()

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Not Completed"
            print(f"Task {i+1}: {task.title} | Due: {task.due_date} | Priority: {task.priority} | Status: {status}")

    def save_tasks(self):
        # Code to save tasks to a file or database
        pass

    def load_tasks(self):
        # Code to load tasks from a file or database
        pass
