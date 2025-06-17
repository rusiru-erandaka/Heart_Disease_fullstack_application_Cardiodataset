from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K

model = load_model('models/model-197.model')

scaler_data = joblib.load('models/scaler_data.sav')
scaler_target = joblib.load('models/scaler_target.sav')

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('details.html')
@app.route('/getresults', methods=['POST'])
def getresults():

    results = request.form
    print(results)
    name = results['name']
    gender = float(results['gender'])
    age = float(results['age'])
    tc = float(results['tc'])
    hdl = float(results['hdl'])
    smoke = float(results['smoke'])
    bpm = float(results['bpm'])
    diab = float(results['diab'])

    test_data = np.array([gender, age, tc, hdl, smoke, bpm, diab]).reshape(1, -1)
    test_data = scaler_data.transform(test_data)
    prediction = model.predict(test_data)
    prediction = scaler_target.inverse_transform(prediction)
    print(prediction, prediction[0], prediction[0][0])

    resultDict = {"name": name, "risk": round(prediction[0][0],2)}
    return render_template('result.html', result=resultDict)

app.run(debug=True)
