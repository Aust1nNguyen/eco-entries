from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# Home view
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# Login view
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Form processing - check for POST request
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if (re.search('\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email)) == None:
            flash('Email address is invalid.', category='error')
        elif len(email) < 4:
            flash("Please enter a valid email.", category="error")
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters.', category='error')
        else:
            flash('Account created!', category='success')
    return render_template("sign_up.html")

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)
