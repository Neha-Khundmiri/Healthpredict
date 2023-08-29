from flask import Flask, render_template, request, flash, redirect
import pickle
import numpy as np
import tensorflow 



app = Flask(__name__)

error_msg = "Please Enter Valid Details.." 

def predict(values, dic):
    if len(values) == 8:
        model = pickle.load(open('models/diabetes.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/cancer.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    else:
        return error_msg


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/home")
def home():
    return render_template('/home.html')

@app.route("/help")
def help():
    return render_template('/help.html')

@app.route("/tc")
def tc():
    return render_template('/tc.html')

@app.route("/login")
def loginPage():
    return render_template('/login.html')

@app.route("/signup")
def signupPage():
    return render_template('/signup.html')

@app.route("/dashboard")
def dashboard():
    return render_template('/dashboard.html')

@app.route("/disindex")
def disindex():
    return render_template('/disindex.html')

@app.route("/diabetes", methods=['GET', 'POST'])
def diabetesPage():
    return render_template('diabetes.html')

@app.route("/cancer", methods=['GET', 'POST'])
def cancerPage():
    return render_template('breast_cancer.html')

@app.route("/heart", methods=['GET', 'POST'])
def heartPage():
    return render_template('heart.html')

@app.route("/kidney", methods=['GET', 'POST'])
def kidneyPage():
    return render_template('kidney.html')

@app.route("/liver", methods=['GET', 'POST'])
def liverPage():
    return render_template('liver.html')


@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
            return render_template('predict.html', pred = pred)
    except Exception as e:
        message = "Please enter valid Data.."
        return render_template("home.html", error_msg = message)

    return render_template('index.html')



if __name__ == '__main__':
	app.run(debug = True)