class TaskTracker:
    def __init__(self):
        self.tasks = []  # List to store tasks
        self.users = {}  # Dictionary to store user data (username: password)
        self.logged_in_user = None  # To keep track of the logged-in user

    def add_task(self, task_title, task_description, due_date):
        """Add a new task to the task list."""
        task = {
            'title': task_title,
            'description': task_description,
            'due_date': due_date,
            'reminder': None  # Initialize reminder as None
        }
        self.tasks.append(task)

    def delete_task(self, task_index):
        """Delete a task by its index in the task list."""
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def set_reminder(self, task_index, reminder):
        """Set a reminder for a task by its index in the task list."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['reminder'] = reminder

    def add_user(self, username, password):
        """Add a new user to the user dictionary."""
        if username not in self.users:
            self.users[username] = password

    def login(self, username, password):
        """Log in a user if the username and password match."""
        if username in self.users and self.users[username] == password:
            self.logged_in_user = username
            return True
        else:
            return False

    def logout(self):
        """Log out the currently logged-in user."""
        self.logged_in_user = None

