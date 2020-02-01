#!flask/bin/python
from flask import Flask, jsonify, request


app = Flask(__name__)


def predict(data):
    return "test"

@app.route('/livestock-analyzer/api/v1.0/predict', methods=['POST'])
def get_tasks():
    return predict(request.get_json())


if __name__ == '__main__':
    app.run(debug=True)
