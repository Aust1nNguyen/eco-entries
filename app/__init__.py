from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Database instance of sqlalchemy
db = SQLAlchemy(app)

# Migration of database
migrate = Migrate(app, db, render_as_batch=True)

# Users login manager
login = LoginManager(app)

# require user to login
login.login_view = 'login'

from app import routes, models
