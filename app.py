from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from config import Config  # Import the Config class from config.py
from your_app.models import TaskTracker, Task, User, AdminPanel  # Import your models

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

# Define your routes and views here

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password

