import numpy as np
import pickle
from flask import Flask,render_template,request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

""" @app.route('/predict',methods=['GET','POST'])
def predict():
    prediction = model.predict([[request.form.get('temperature')]])
    #prediction = model.predict([[28]])
    output = round(prediction[0],2)
    print(output)
    return render_template('index.html') """

@app.route('/predict',methods=['GET','POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    prediction = model.predict(features)
    output = round(prediction[0],2)
    #print(output)
    return render_template('index.html', prediction_text =f'Total revenue generated is Rs. {output}/-')


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000)