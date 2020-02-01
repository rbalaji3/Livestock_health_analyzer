#!flask/bin/python
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/livestock-analyzer/api/v1.0/predict', methods=['POST'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):

    if request.method == 'POST':
        # values  = parse(request.get_json())
        return request.get_json()
    else:
        return "ASS"

if __name__ == '__main__':
    app.run(debug=True)
