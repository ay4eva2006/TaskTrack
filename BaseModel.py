from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

class Task(BaseModel):
    title = db.Column(db.String(128))
    description = db.Column(db.String(256))
    due_date = db.Column(db.Date)
    reminder = db.Column(db.Date)
    user = db.Column(db.String(64))  # Store the username of the associated user

class User(BaseModel):
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))  # Store hashed passwords

class AdminPanel(BaseModel):
    admin_users = db.relationship('User', backref='admin_panel', lazy='dynamic')

    def add_admin_user(self, user):
        self.admin_users.append(user)

    def remove_admin_user(self, user):
        self.admin_users.remove(user)

    def view_all_users(self):
        return User.query.all()

