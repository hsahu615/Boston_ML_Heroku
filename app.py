from flask import Flask, render_template, redirect, request, url_for
from flask_cors import CORS, cross_origin
import pickle
import numpy as np
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def HomePage():
    return render_template('index.html')

@app.route('/prediction', methods = ['POST'])
def predict():
    try:
        CRIM = float(request.form.get('CRIM'))
        NOX = float(request.form.get('NOX'))
        RAD = float(request.form.get('RAD'))
        ZN = float(request.form.get('ZN'))
        RM = float(request.form.get('RM'))
        PTRATIO = float(request.form.get('PTRATIO'))
        INDUS = float(request.form.get('INDUS'))
        AGE = float(request.form.get('AGE'))
        B = float(request.form.get('B'))
        CHAS = float(request.form.get('CHAS'))
        DIS = float(request.form.get('DIS'))
        LSTAT = float(request.form.get('LSTAT'))
        boston = pickle.load(open('final_model.pickle','rb'))
        result = 'Price of Houses are around $ ' + str(boston.predict([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, PTRATIO, B, LSTAT]])[0] * 1000)
        return render_template('predict.html', result = result)

    except:
        return """<h1>Something went wrong</h1>"""

port = int(os.getenv("PORT"))
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=port)