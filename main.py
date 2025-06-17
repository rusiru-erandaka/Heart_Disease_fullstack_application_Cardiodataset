from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to the Website!!"
@app.route('/check')
def check():
    return render_template('check.html')

app.run(debug=True)
