from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from your_app.models import TaskTracker, Task, User, AdminPanel  # Import your models
from flask_login import login_required, current_user

task_tracker_bp = Blueprint('task_tracker', __name__)

# Home Page
@task_tracker_bp.route('/')
@login_required
def index():
    if current_user.username == 'admin':
        return redirect(url_for('task_tracker.admin_panel'))
    else:
        user_tasks = [task for task in current_app.task_tracker.tasks if task.user == current_user.username]
        return render_template('user_template.html', user=current_user, tasks=user_tasks)

# Add Task
@task_tracker_bp.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    task = Task(title, description, due_date)
    task.user = current_user.username
    current_app.task_tracker.add_task(task)
    flash('Task added successfully', 'success')
    return redirect(url_for('task_tracker.index'))

# Delete Task
@task_tracker_bp.route('/delete_task/<int:task_id>')
@login_required
def delete_task(task_id):
    task = next((task for task in current_app.task_tracker.tasks if task.id == task_id), None)
    if task and task.user == current_user.username:
        current_app.task_tracker.delete_task(task_id)
        flash('Task deleted successfully', 'success')
    else:
        flash('Task not found or unauthorized', 'error')
    return redirect(url_for('task_tracker.index'))

# Set Reminder for Task
@task_tracker_bp.route('/set_reminder/<int:task_id>', methods=['POST'])
@login_required
def set_reminder(task_id):
    task = next((task for task in current_app.task_tracker.tasks if task.id == task_id), None)
    if task and task.user == current_user.username:
        reminder = request.form['reminder']
        current_app.task_tracker.set_reminder(task_id, reminder)
        flash('Reminder set successfully', 'success')
    else:
        flash('Task not found or unauthorized', 'error')
    return redirect(url_for('task_tracker.index'))

# User Profile
@task_tracker_bp.route('/user_profile')
@login_required
def user_profile():
    user_tasks = [task for task in current_app.task_tracker.tasks if task.user == current_user.username]
    return render_template('user_template.html', user=current_user, tasks=user_tasks)

# Admin Panel (Note: Add admin access check)
@task_tracker_bp.route('/admin_panel')
@login_required
def admin_panel():
    if current_user.username == 'admin':
        return render_template('admin_template.html', admin_panel=current_app.task_tracker.admin_panel)
    else:
        flash('Access denied. You must be an admin.', 'error')
        return redirect(url_for('task_tracker.index'))

# ... Add more routes and views as needed ...


