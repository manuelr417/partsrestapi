from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.parts import BaseParts

app = Flask(__name__)
#apply CORS
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dude')
def hello_dude():
    return 'Que es la q hay!!'

# This route make two things
# 1. List of all parts in the systems - GET
# 2. Add a new part to the system - POST
@app.route('/PartApp/parts', methods=['GET', 'POST'])
def handleParts():
    if request.method == 'POST':
        return BaseParts().addNewPart(request.json)
    else:
        return BaseParts().getAllParts()

@app.route('/PartApp/parts/<int:pid>', methods=['GET'])
def handlePartById(pid):
    if request.method == 'GET':
        return BaseParts().getPartById(pid)
    else:
        return jsonify("Method Not Allowed"), 405

if __name__ == '__main__':
    app.run(DEBUG=True)
