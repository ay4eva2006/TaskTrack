class User(TaskTracker):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.tasks = []  # Store tasks associated with this user

    def add_task(self, task):
        self.tasks.append(task)

    def __str__(self):
        return f"User: {self.username}"

