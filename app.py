
import pickle
import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)
model = pickle.load(open('./model/model.pkl', 'rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/", methods = ['POST'])
def predict():

    age_group = request.form['age_group']
    total_deaths = request.form['total_deaths']
    data = [[age_group,total_deaths]]
    out = model.predict(data)

    return "Covid-19 deaths:"+str(np.round((out[0])))

if __name__ == "__main__":

    app.run()
   
    
   
