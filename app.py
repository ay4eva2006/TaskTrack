from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import Config  # Import the Config class from config.py
from app.models import TaskTracker, Task, User, AdminPanel  # Import your models
from app import routes

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Set the login view to your login route

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize TaskTracker instance
task_tracker = TaskTracker()

if __name__ == '__main__':
    # Create the database tables if the script is run directly
    db.create_all()
    app.run()
