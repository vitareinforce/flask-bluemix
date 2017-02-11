# Copyright 2015 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from flask import Flask, jsonify, Response, json
from flask_cors import CORS, cross_origin
from flightdata import flightdata

app = Flask(__name__)
app.register_blueprint(flightdata)
CORS(app)

@app.route('/')
def Welcome():
    return app.send_static_file('index.html')

@app.route('/myapp')
def WelcomeToMyapp():
    return 'Welcome again to my app running on Bluemix!'

@app.route('/api/people', methods = ['GET'])
def GetPeople():
    list_data = [
        {'name': 'Vitradisa Pratama', 'nim': '23215331'},
        {'name': 'Ridwan Suhud', 'nim': '23215343'}
    ]
    json_data = json.dumps(list_data)
    resp = Response(json_data, status=200, mimetype="application/json")
    return resp

@app.route('/api/people/<name>')
def SayHello(name):
    message = {
        'message': 'Hello ' + name
    }
    return jsonify(results=message)

@app.route('/api/temp/<suhu>')
def UkurSuhu(suhu):
    suhu_akhir = {
        'message': 'Suhu input : ' + suhu
    }
    return jsonify(results=suhu_akhir)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
