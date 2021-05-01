from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create application object as an instace of class Flask
app = Flask(__name__)
app.config.from_object(Config)

# Initialize a database instance of sqlalchemy
db = SQLAlchemy(app)

# Migrate app to database
migrate = Migrate(app, db)

from app import routes, models