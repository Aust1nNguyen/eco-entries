from flask import Flask
from config import Config

# Create application object as an instace of class Flask
app = Flask(__name__)
app.config.from_object(Config)

from app import routes