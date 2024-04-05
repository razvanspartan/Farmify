from flask import Flask, jsonify, request, session
from flask_cors import CORS


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