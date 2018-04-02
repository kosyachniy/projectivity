from flask import render_template, session
from app import app

from requests import post
from json import loads

LINK = 'http://167.99.128.56/'

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	competions = loads(post(LINK, json={'cm': 'competions.gets'}).text)
	users = loads(post(LINK, json={'cm': 'users.gets'}).text)

	if 'token' in session:
		user = {'login': session['login']}
	else:
		user = {'login': None}

	return render_template('index.html',
		#title = 'Главная',
		#description = '',
		competions = competions,
		users = users,
		user = user,
	)