from flask import render_template
from app import app

from requests import post
from json import loads

LINK = 'http://167.99.128.56/'

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	x = post(LINK, json={'cm': 'competions.gets'}).text
	print(x)
	competions = loads(x)
	print(competions)

	users = loads(post(LINK, json={'cm': 'users.gets'}).text)

	user = {
		'login': None,
	}

	return render_template('index.html',
		#title = 'Главная',
		#description = '',
		competions = competions,
		users = users,
		user = user,
	)