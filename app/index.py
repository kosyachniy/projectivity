from flask import render_template
from app import app

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	competions = [
		{'id': 1, 'name': 'VK Cup', 'author': 'ВКонтакте', 'time': 84931981},
		{'id': 2, 'name': 'Школа анализа данных', 'author': 'Яндекс', 'time': 59257233},
	]

	users = [
		{'name': 'Иван', 'surname': 'Тюрин', 'login': 'ivantt', 'photo': 1},
		{'name': 'Алексей', 'surname': 'Полоз', 'login': 'kosyachniy', 'photo': 2},
	]

	user = {
		'login': 'kosyachniy',
	}

	return render_template('index.html',
		#title = 'Главная',
		#description = '',
		competions = competions,
		users = users,
		user = user,
	)