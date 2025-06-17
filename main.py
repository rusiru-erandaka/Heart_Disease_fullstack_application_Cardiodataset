from flask import Flask,render_template,request
import joblib
import numpy as np
from keras.models import load_model
from keras import backend as K

model = load_model('models/model-197.model')

scaler_data = joblib.load('models/scaler_data.sav')
scaler_target = joblib.load('models/scaler_target.sav')


