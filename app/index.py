from flask import render_template
from app import app

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	competions = [
		{'name': 'VK Cup', 'author': 'ВКонтакте', 'time': 84931981},
		{'name': 'Школа анализа данных', 'author': 'Яндекс', 'time': 59257233},
	]

	users = [
		{'name': 'Иван', 'surname': 'Тюрин', 'login': 'ivantt'},
		{'name': 'Алексей', 'surname': 'Полоз', 'login': 'kosyachniy'},
	]

	user = {
		'login': 'kosyachniy',
	}

	return render_template('index.html',
		#title = 'Main',
		#description = '',
		competions = competions,
		users = users,
		user = user,
	)