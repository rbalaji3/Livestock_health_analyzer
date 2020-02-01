from flask import Flask, jsonify, request
from flask_cors import CORS
from fin_model import Model
import json as json_2
import numpy as np
import datetime


app = Flask(__name__)
CORS(app)

def predict(data):
    return jsonify(data)

@app.route('/api', methods=['POST'])
def get_tasks():
    model = Model('../data/data_clean_final.csv')
    json = request.get_json()

    start_date = json['cycle_start_date'].split('/')
    current_date = json['current_date'].split('/')
    cycle_length = json['cycle_length']

    start_dt = datetime.date(2000+int(start_date[2]), int(start_date[0]), int(start_date[1]))
    current_dt = datetime.date(2000+int(current_date[2]), int(current_date[0]), int(current_date[1]))
    difference = int((start_dt - current_dt).days)
    percent = difference / int(cycle_length)


    # print("HELLO ", start_date, current_date, difference, percent, type(difference))

    prediction = model.predict([float(json['inside_humidity']), float(json['inside_temperature']), percent])

    output_dict = {
        'predict_weight': prediction['predict_weight'][0],
        'optimal_weight': prediction['optimal_weight'][0],
        'optimal_parameter_humidity' : prediction['optimal_parameter_humidity'],
        'optimal_parameter_temperature' : prediction['optimal_parameter_temperature']
    }

    return json_2.dumps(output_dict)

if __name__ == '__main__':
    app.run()
