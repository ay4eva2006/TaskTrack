class TaskTracker:
    # ... (base class code)

class Task(TaskTracker):
    def __init__(self, title, description, due_date):
        super().__init__()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.reminder = None

    def set_reminder(self, reminder):
        self.reminder = reminder

    def __str__(self):
        return f"Task: {self.title}, Due Date: {self.due_date}"

