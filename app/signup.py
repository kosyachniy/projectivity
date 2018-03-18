from flask import render_template, request, jsonify
from app import app
from mongodb import *

@app.route('/', methods=['POST'])
def hello():
	x = request.json
	print(x)
	try:
		if x['cm'] == 'reg':
			del x['cm']
			db['users'].insert(x)
		return 'Yep'
	except:
		return 'Error'