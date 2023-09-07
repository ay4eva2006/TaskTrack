# config.py

class Config:
    SECRET_KEY = 'your can never guess'  # Replace with a strong secret key
    DEBUG = True  # Set to False in production

# Configuration for the base TaskTracker class
class TaskTrackerConfig(Config):
    # Add any configuration specific to TaskTracker here
    pass

# Configuration for the Task subclass
class TaskConfig(Config):
    # Add any configuration specific to Task here
    pass

# Configuration for the User subclass
class UserConfig(Config):
    # Add any configuration specific to User here
    pass

# Configuration for the AdminPanel subclass
class AdminPanelConfig(Config):
    # Add any configuration specific to AdminPanel here
    pass

# Configuration for Flask extensions (if any)
# For example, SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

