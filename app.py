""" import pickle
from flask import Flask,render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    prediction = model.predict([[28]])
    print(prediction)
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True) """