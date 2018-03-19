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
			if all([i in x for i in ('login', 'pass', 'mail')]):
				return '3'

			#Логин существует
			if not len(list(db['users'].find({'login': x['login']}))):
				return '5'

			#Почта зарегистрирована
			if not len(list(db['users'].find({'mail': x['mail']}))):
				return '8'

			del x['cm']
			db['users'].insert(x)
			return '0'

#Авторизация
		elif x['cm'] == 'auth':
			pass

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'