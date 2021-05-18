from datetime import datetime
from time import sleep
from flask import Flask, render_template, flash, redirect, url_for, request
from flask import jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db, models
from app.forms import LoginForm, SignUpForm, EmptyForm
from app.models import User, Course, Quiz
from werkzeug.urls import url_parse
from sqlalchemy import event

# Home view
@app.route('/')
@app.route('/index')
def home():
    # Add available courses
    if not models.is_init_course():
        db.session.add(Course(coursename='Demand and Supply', courseurl='ds'))
        db.session.add(Course(coursename='Elasticity', courseurl='elasticity'))
        db.session.add(Course(coursename='Consumer and Producer Surplus', courseurl='surplus'))
        db.session.commit()
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
            form.username.errors.append("Please check your username and password again")
            form.password.errors.append("Please check your username and password again")
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


# Dashboard view
@app.route('/dashboard')
@login_required
def dashboard():
    courses = current_user.enrolled_course().all()
    quizes = current_user.completed_quiz()

    return render_template("dashboard.html", title='Dashboard', courses=courses, quizes=quizes)

@app.route("/profile")
def profile():
    course_point = float(current_user.user_course_points())
    quiz_point = current_user.user_quiz_points()
    total_point = course_point + quiz_point
    return render_template("profile.html", title= "Profile", coursepoint=course_point, quizpoint=quiz_point, totalpoint=total_point)


# Courses view
@app.route('/content')
def content():
    return render_template("content.html", title= "Content")

@app.route('/ds')
def ds():    
    if current_user.is_authenticated:
        course = Course.query.filter_by(coursename="Demand and Supply").first()
        current_user.enrol(course)
        db.session.commit()

    return render_template("ds.html", title= "Demand and Supply")

@app.route("/elasticity")
def elasticity():
    if current_user.is_authenticated:
        course = Course.query.filter_by(coursename="Elasticity").first()
        current_user.enrol(course)
        db.session.commit()

    return render_template("elasticity.html", title= "Elasticity")

@app.route("/surplus")
def surplus():
    if current_user.is_authenticated:
        course = Course.query.filter_by(coursename="Consumer and Producer Surplus").first()
        current_user.enrol(course)
        db.session.commit()
    
    return render_template("surplus.html", title= "Consumer and Producer Surplus")

# Quiz view
@app.route('/feedback')
def feedback():
    return redirect(url_for('/dashboard'))


@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html', title='Quiz', form='quizForm')

@app.route('/ds_quiz', methods=['GET', 'POST'])
@login_required
def ds_quiz():
    answers = ["b", "c", "c", "b", "c"]
    
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        questions = [q1, q2, q3, q4, q5]

        score = models.quiz_score(questions, answers)

        quiz = Quiz(quizname='Demand and Supply', quizurl='ds_quiz', quiz_scoreoutofhundred=score)
        current_user.attempt(quiz)
        db.session.commit()
        sleep(60)
        return redirect(url_for('dashboard'))

    elif request.method == 'GET':
        return render_template('ds_quiz.html', title='Quiz', form='quizForm')

@app.route('/elasticity_quiz', methods=['GET', 'POST'])
@login_required
def elasticity_quiz():
    answers = ["c", "a", "a", "c", "a"]
    
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        questions = [q1, q2, q3, q4, q5]

        score = models.quiz_score(questions, answers)

        quiz = Quiz(quizname='Elasticity', quizurl='elasticity_quiz', quiz_scoreoutofhundred=score)
        current_user.attempt(quiz)
        db.session.commit()
        sleep(60)
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        return render_template('elasticity_quiz.html', title='Quiz', form='quizForm')

@app.route('/surplus_quiz', methods=['GET', 'POST'])
@login_required
def surplus_quiz():
    answers = ["a", "c", "b", "c", "c"]
    
    if request.method == 'POST':
        q1 = request.form['q1']
        q2 = request.form['q2']
        q3 = request.form['q3']
        q4 = request.form['q4']
        q5 = request.form['q5']
        questions = [q1, q2, q3, q4, q5]

        score = models.quiz_score(questions, answers)

        quiz = Quiz(quizname='Consumer and Producer Surplus', quizurl='surplus', quiz_scoreoutofhundred=score)
        current_user.attempt(quiz)
        db.session.commit()
        sleep(60)
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        return render_template('surplus_quiz.html', title='Quiz', form='quizForm')

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)

