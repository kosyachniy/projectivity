from flask import render_template
from app import app
from requests import get

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	competions = json.loads(get(src).text)

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