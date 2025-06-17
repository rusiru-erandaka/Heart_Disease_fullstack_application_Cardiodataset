from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K



app = Flask(__name__)
@app.route('/')
def index():
    return "Welcome to the Website!!"
@app.route('/check')
def check():
    return render_template('check.html')

app.run(debug=True)
