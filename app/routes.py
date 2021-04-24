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

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)