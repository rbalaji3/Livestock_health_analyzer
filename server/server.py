#!flask/bin/python
from flask import Flask, jsonify, request
from flask_cors import CORS
from fin_model import Model

app = Flask(__name__)
CORS(app)

def predict(data):
    return jsonify(data)

@app.route('/api', methods=['POST'])
def get_tasks():
    model = Model('../Data/data_clean_final.csv')
    return predict(request.get_json())


if __name__ == '__main__':
    app.run()
