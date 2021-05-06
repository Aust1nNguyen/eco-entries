from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# loading logged in user
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# association tables for many-to-many relationship\
# track the enrollment of users
class CourseEnrol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('course.id'))

# track the attempt quiz of user
class QuizAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))


# User model
class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True) 
    # ONLY store hashed password
    password_hash = db.Column(db.String(128))
    # gained by complete quiz
    scores = db.Column(db.Integer)
    # user's enrolled courses
    courses = db.relationship('Course', secondary='CourseEnrol', lazy = 'dynamic')
    # user's attempted quiz
    quizes = db.relationship('Quiz', secondary='QuizAttempt', lazy = 'dynamic')

    # hash plain password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # check hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # represent data
    def __repr__ (self):
        return '<User {}>'.format(self.username)

# Course mmodel
class Course(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    coursename = db.Column(db.String(128), index = True, unique = True)
    users = db.relationship('User', secondary='CourseEnrol')

    def __repr__(self):
        return '<Course {}>'.format(self.id)


# Quiz mmodel
class Quiz(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    quizname = db.Column(db.String(128), index = True, unique = True)
    quizscore = db.Column(db.Integer())
    users = db.relationship('User', secondary='QuizAttempt')

    def __repr__(self):
        return '<Quiz {}>'.format(self.id)