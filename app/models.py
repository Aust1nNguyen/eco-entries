from datetime import datetime
from app import db

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)

    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)

    password_hash = db.Column(db.String(128))

    # Posts of user
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    # Represent data to user
    def __repr__ (self):
        return '<User {}>'.format(self.username)

class Post(db.Model):

    id = db.Column(db.Integer, primary_key = True)

    body = db.Column(db.String(256))

    # time when post happen
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    
    # foreign key of user id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)