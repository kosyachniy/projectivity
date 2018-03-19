from flask import render_template, request, jsonify
from app import app
from mongodb import *

@app.route('/', methods=['POST'])
def hello():
	x = request.json
	print(x)

	if 'cm' not in x:
		return '2'

	try:
#Регистрация
		if x['cm'] == 'reg':
			#Не все поля заполнены
			if not all([i in x for i in ('login', 'pass', 'mail')]):
				return '3'

			#Логин существует
			if len(list(db['users'].find({'login': x['login']}))):
				return '5'

			#Почта зарегистрирована
			if len(list(db['users'].find({'mail': x['mail']}))):
				return '8'

			db['users'].insert({
				'login': x['login'],
				'password': x['pass'],
				'mail': x['mail'],
			})
			return '0'

#Авторизация
		elif x['cm'] == 'auth':
			#Не все поля заполнены
			if not all([i in x for i in ('login', 'pass')]):
				return '3'

			#Логин не существует
			if not len(list(db['users'].find({'login': x['login']}))):
				return '4'

			#Неправильный пароль
			if not len(list(db['users'].find({'login': x['login'], 'password': x['pass']}))):
				return '5'

			return '0'

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'