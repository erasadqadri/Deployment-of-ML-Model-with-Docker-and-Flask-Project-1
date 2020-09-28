"""
Author: Asad Qadri
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import sklearn


app = Flask(__name__)
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

@app.route("/")
def welcome():
    return "Welcome All"

@app.route("/predict")
def bank_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "predicted class value is " + str(prediction)

@app.route("/predict_file", methods = ["POST"])
def bank_note_file_authentication():
    df_test = pd.read_csv(request.files.get("files"))
    prediction = classifier.predict(df_test)
    return "predicted class value for TestFile is " + str(list(prediction))

if __name__ == '__main__':
    app.run()