from flask import Flask, jsonify, request, session
from flask_cors import CORS
from controller import get_all_farms, get_farm, add_user, add_farm


app = Flask(__name__)
CORS(app)

sqlConnector = None

def runFlask(sqlConnectorInit):
    global sqlConnector
    sqlConnector = sqlConnectorInit
    sqlConnector.connect()
    app.run(host='0.0.0.0', debug=True)

@app.route('/api/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        data = {"test": "test2"}
        return jsonify(data)
    elif request.method == 'POST':
        requestData = request.get_json()
        resultData = {"receivedData": requestData}
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

# @app.route('/api/add_farm', methods=['POST'])
# def add_farm():
#     if request.method == 'POST':
#         requestData = request.get_json()
#         resultData = add_farm(requestData, sqlConnector)
#
#         return jsonify(resultData)
#     else:
#         return jsonify({"message": "Method not allowed"}), 405


@app.route('/api/get_all_farms', methods=['GET'])
def get_all_farms_route():
    if request.method == 'GET':
        resultData = get_all_farms(sqlConnector)
        for row in resultData:
            print(row)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/get_farm', methods=['POST'])
def get_farm_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = get_farm(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405


@app.route('/api/add_user', methods=['POST'])
def add_user_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = add_user(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/add_farm', methods=['POST'])
def add_farm_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = add_farm(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405