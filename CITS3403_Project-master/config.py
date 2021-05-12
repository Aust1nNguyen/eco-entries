import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration settings
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'our-secret-key'

    # Tell config where to find sqlalchemy database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False