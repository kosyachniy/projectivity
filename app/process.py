from flask import request, jsonify
from app import app

from mongodb import *
from re import findall, match
from hashlib import md5

import rsa
(pubkey, privkey) = rsa.newkeys(512)

@app.route('/', methods=['POST'])
def process():
	x = request.json
	print(x)

	if 'cm' not in x:
		return '2'

	try:
#Получение публичного ключа
		if x['cm'] == 'key':
			return str(str(pubkey.n) + ',' + str(pubkey.e))

#Регистрация
		if x['cm'] == 'reg':
			#Не все поля заполнены
			if not all([i in x for i in ('login', 'pass', 'mail')]):
				return '3'

			x['login'] = x['login'].lower()

			#Логин существует
			if len(list(db['users'].find({'login': x['login']}))):
				return '5'

			#Недопустимый логин
			if not 3 <= len(x['login']) <= 20 or len(findall('[^a-z0-9]', x['login'])):
				return '4'

			#Почта зарегистрирована
			if len(list(db['users'].find({'mail': x['mail']}))):
				return '8'

			#Недопустимый пароль
			if not 6 <= len(x['pass']) <= 40 or len(findall('[^a-zA-z0-9!@#$%^&*()-_+=;:,./?\|`~\[\]{}]', x['pass'])):
				return '6'

			#Это не почта
			if match('.+@.+\..+', x['mail']) == None:
				return '7'

			pas = rsa.decrypt(x['pass'], privkey)
			print(pas)
			pas = md5(bytes(pas, 'utf-8')).hexdigest()

			query = db['users'].insert({
				'login': x['login'],
				'password': pas,
				'mail': x['mail'],
			})
			#print(query)
			return '0'

#Авторизация
		elif x['cm'] == 'auth':
			#Не все поля заполнены
			if not all([i in x for i in ('login', 'pass')]):
				return '3'

			x['login'] = x['login'].lower()

			#Логин не существует
			if not len(list(db['users'].find({'login': x['login']}))):
				return '4'

			pas = rsa.decrypt(x['pass'], privkey)
			print(pas)
			pas = md5(bytes(pas, 'utf-8')).hexdigest()

			#Неправильный пароль
			query = list(db['users'].find({'login': x['login'], 'password': pas}))
			if not len(query):
				return '5'

			#print(query[0]['_id'])
			return '0'

#Изменение личной информации
		elif x['cm'] == 'profile':
			pass

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'