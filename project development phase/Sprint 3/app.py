from flask import Flask,render_template,request,redirect
import numpy as np
import joblib
from keras.models import load_model

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    if request.method == "POST":
        string = request.form['val']
        if(string ==""):
            return render_template('predict.html')            
        string = string.split(',')
        x_input = [eval(i) for i in string]    
        sc = joblib.load("scaler.save") 
        x_input = sc.fit_transform(np.array(x_input).reshape(-1,1))
        x_input = np.array(x_input).reshape(1,-1)
        x_input = x_input.reshape(1,-1)
        x_input = x_input.reshape((1,10,1))
        model = load_model('model.h5')
        output = model.predict(x_input)
        val = sc.inverse_transform(output)
        return render_template('predict.html' , prediction = round(val[0][0],2))  
    if request.method == "GET":    
        return render_template('predict.html')       

if __name__=="__main__":
    model = load_model('model.h5')
    app.run(debug=True)
