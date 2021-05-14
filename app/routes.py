from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, SignUpForm
from app.models import User
from werkzeug.urls import url_parse
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
        return redirect(url_for('dashboard'))
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
            next_page = url_for('dashboard')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# Sign up view
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        # hash the plain password
        user.set_password(form.password.data)
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
    return redirect(url_for('login'))

# Quiz view
@app.route('/ds_quiz')
def ds_quiz():
    return render_template('ds_quiz.html', title='Quiz', form='quizForm')

# Course 1 view
@app.route('/courses')
def courses():
    return render_template("courses.html", title= "Courses")

# Courses view
@app.route('/content')
def content():
    if current_user.is_authenticated:
        current_user.enroll_course()
    return render_template("content.html", title= "Content")

# Dashboard view
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", title='Dashboard')

@app.route("/elasticity")
def elasticity():
    return render_template("elasticity.html", title= "Elasticity")

@app.route("/ds")
def ds():
    return render_template("ds.html", title= "Demand and Supply")

@app.route("/surplus")
def surplus():
    return render_template("surplus.html", title= "Consumer and Producer Surplus")

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)

