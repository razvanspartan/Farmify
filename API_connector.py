from flask import Flask, jsonify, request, session
from flask_cors import CORS
from controller import get_all_farms, get_farm, update_produce, get_farms, add_user, add_farm, get_user, update_user, update_farm, add_produce, get_produce, add_order, get_orders, delete_produce


app = Flask(__name__)
CORS(app)

sqlConnector = None

def runFlask(sqlConnectorInit):
    global sqlConnector
    sqlConnector = sqlConnectorInit
    sqlConnector.connect()
    app.run(host='0.0.0.0', debug=True)

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

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

@app.route('/api/add_farm', methods=['POST'])
def add_farm_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = add_farm(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

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

@app.route('/api/get_farms', methods=['POST'])
def get_farms_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = get_farms(requestData, sqlConnector)

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

@app.route('/api/get_user', methods=['POST'])
def get_user_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = get_user(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405


@app.route('/api/update_user', methods=['POST'])
def update_user_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = update_user(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/update_farm', methods=['POST'])
def update_farm_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = update_farm(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/add_produce', methods=['POST'])
def add_produce_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = add_produce(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/get_produce', methods=['POST'])
def get_produce_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = get_produce(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405


@app.route('/api/add_order', methods=['POST'])
def add_order_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = add_order(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/get_orders', methods=['POST'])
def get_orders_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = get_orders(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405

@app.route('/api/delete_produce', methods=['POST'])
def delete_produce_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = delete_produce(requestData, sqlConnector)
        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405



@app.route('/api/update_produce', methods=['POST'])
def update_produce_route():
    if request.method == 'POST':
        requestData = request.get_json()
        resultData = update_produce(requestData, sqlConnector)

        return jsonify(resultData)
    else:
        return jsonify({"message": "Method not allowed"}), 405