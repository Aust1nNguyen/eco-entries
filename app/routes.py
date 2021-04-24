from flask import Flask, render_template,request

app = Flask(__name__)

# Home and index page
@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        pass

# Run with debug mode
if __name__ == '__main__':
    app.run(debug=True)