from flask import Flask, render_template, request
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__,template_folder='template')
model = pickle.load(open('decision_tree.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':        
        Jan_June = int(request.form['Jan_June'])
        July_Dec = int(request.form['July_Dec'])

        prediction=model.predict([[Jan_June,July_Dec]])
        output=round(prediction[0],2)

        if (output == 0.0):
            result = "Active"
        elif (output == 1.0):
            result = "Going to be Dormant"
        elif (output == 2.0):
            result = "Dormant"


        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="Account is {}".format(result))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
#https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH    