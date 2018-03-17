from flask import render_template, request, jsonify
from app import app
from db import *

@app.route('/', methods=['POST'])
def hello():
	x = request.json
	if x['cm'] == 'reg':
		with db:
			db.execute("INSERT INTO users (name, surname, mail, password, login) VALUES (?, ?, ?, ?, ?)", (x['name'], x['surname'], x['mail'], x['pass'], x['login']))