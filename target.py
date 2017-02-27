import os
from flask import Blueprint, json, Response

target = Blueprint('target', __name__)

@target.route('/target', methods = ['GET'])
def GetTarget():
	messages = {
		'x': 200.00,
		'y': 75.00,
		'z': 400.00
	}
	json_target = json.dumps(messages)
	resp = Response(json_target, status=200, mimetype="application/json")
	return resp
