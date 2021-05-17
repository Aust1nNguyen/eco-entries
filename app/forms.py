from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
import sys

# User login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username not found')])
    password = PasswordField('Password', validators=[DataRequired(message='Password not found')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("Please check your username and password again")
        



# Sign up form
class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username not found')])
    email = StringField('Email', validators=[DataRequired(message='Email not found'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password not found')])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(message='Password not found'), EqualTo('password')])
    submit = SubmitField('Register')

    # validate unique username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    # validate unique email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


