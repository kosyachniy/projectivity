from flask import render_template, request, jsonify
from app import app
from db import *

@app.route('/', methods=['POST'])
def hello():
	x = request.json
	if x['cm'] == 'reg':
		del x['cm']
		db.insert(x)