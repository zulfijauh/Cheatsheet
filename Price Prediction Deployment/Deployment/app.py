# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import joblib
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

#load result.html. the result of prediction is presented here. 
@app.route('/result/', methods=["POST"])
def prediction_result():
    #receiving parameters sent by client
    bedrooms = int(request.form.get('bedrooms'))
    bathrooms = int(request.form.get('bathrooms'))
    sqft_living = int(request.form.get('sqft_living'))
    sqft_lot = int(request.form.get('sqft_lot'))
    floors = int(request.form.get('floors'))
    waterfront = int(request.form.get('waterfront'))
    view = int(request.form.get('view'))
    condition = int(request.form.get('condition'))
    sqft_above = int(request.form.get('sqft_above'))
    sqft_basement = int(request.form.get('sqft_basement'))
    yr_built = int(request.form.get('yr_built'))
    city = int(request.form.get('city'))

    
    
    #load the trained model.
    filename = 'house_prediction_trained_model.pkl'
    loaded_model= joblib.load(filename)
    #create new dataframe
    new_data = [{'bedrooms':bedrooms, 'bathrooms':bathrooms, 'sqft_living':sqft_living, 'sqft_lot':sqft_lot, 'floors':floors,
       'waterfront':waterfront, 'view':view, 'condition':condition, 'sqft_above':sqft_above, 'sqft_basement':sqft_basement,
       'yr_built':yr_built, 'city':city}]
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.max_rows', None)
    new_df = pd.DataFrame(new_data, index=[0])
    price = loaded_model.predict(new_df)
    price_result = round(float(price),2)
    #return the output and load result.html
    return render_template('result.html', status=price_result)

if __name__ == "__main__":
    #host= ip address, port = port number
    #app.run(host='127.0.0.1', port='5001')
    app.run()