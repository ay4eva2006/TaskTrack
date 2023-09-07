class AdminPanel(TaskTracker):
    def __init__(self):
        super().__init__()
        self.admin_users = []

    def add_admin_user(self, username, password):
        self.admin_users.append({'username': username, 'password': password})

    def remove_admin_user(self, username):
        self.admin_users = [user for user in self.admin_users if user['username'] != username]

    def view_all_users(self):
        return [user.username for user in self.users]

    def __str__(self):
        return "Admin Panel"

