from flask import render_template
from app import app

from requests import post
from json import loads

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	x = post('/', json={'cm': 'competions.gets'}).text
	print(x)
	competions = json.loads(x)

	'''
	x = post('/', json={'cm': 'users.gets'}).text
	print(x)
	competions = json.loads(x)
	'''
	users = [
		{'name': 'Иван', 'surname': 'Тюрин', 'login': 'ivantt', 'photo': 1},
		{'name': 'Алексей', 'surname': 'Полоз', 'login': 'kosyachniy', 'photo': 2},
	]

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