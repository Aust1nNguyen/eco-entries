from flask import Flask, render_template, flash, redirect, url_for, Blueprint
from flask_login import login_required
from flask_login import current_user, login_user
from app import app
from app.forms import LoginForm, SignUpForm
from app.models import User
import re

# Home view
@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title='Home Page')

# Login view
@app.route('/login', methods=['GET', 'POST'])
def login():
    # check if user logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # validate form
    if form.validate_on_submit():
        # return the user object if exist
        user = User.query.filter_by(username=form.username.data).first()
        # if the user is not exist or the password is incorrect
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # register valid user as logged in state
        login_user(user, remember=form.remember_me.data)
        # get the next page argument
        next_page = request.args.get('next')
        # if there is no next argument or next redirect to other domain return to index page
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# Sign up view
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        # hash the plain password
        user.set_password(form.password1.data)
        # Add registered user to our database
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Sign Up', form=form)

# Logout view
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# authent = Blueprint("authent", __name__)

# @authent.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     # Form processing - check for POST request
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template('login.html', title='Sign In', form=form)

# @authent.route("/sign_up", methods=["GET", "POST"])
# def sign_up():
#     if request.method == "POST":
#         email = request.form.get('email')
#         username = request.form.get('username')
#         password1 = request.form.get("password1")
#         password2 = request.form.get("password2")

#         if (re.search('\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email)) == None:
#             flash('Email address is invalid.', category='error')
#         elif len(email) < 4:
#             flash("Please enter a valid email.", category="error")
#         elif len(username) < 2:
#             flash('Username must be greater than 1 character.', category='error')
#         elif password1 != password2:
#             flash('Passwords don\'t match.', category='error')
#         elif len(password1) < 8:
#             flash('Password must be at least 8 characters.', category='error')
#         else:
#             flash('Account created!', category='success')
#     return render_template("sign_up.html")


# Dashboard view
@app.route('/dashboard')
@login_required
def dashboard():
    pass

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)
