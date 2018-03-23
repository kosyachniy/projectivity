from flask import request, jsonify
from app import app

from mongodb import *
from re import findall, match
from hashlib import md5

'''
import rsa
(pubkey, privkey) = rsa.newkeys(512)
'''

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
			if not 3 <= len(x['login']) <= 20 or len(findall('[^a-z0-9]', x['login'])) or not len(findall('[a-z]', x['login'])):
				return '4'

			#Почта зарегистрирована
			if len(list(db['users'].find({'mail': x['mail']}))):
				return '8'

			'''
			x['pass'], = rsa.decrypt(x['pass'], privkey)
			print(x['pass'],)
			'''

			#Недопустимый пароль
			if not 6 <= len(x['pass']) <= 40 or len(findall('[^a-zA-z0-9!@#$%^&*()-_+=;:,./?\|`~\[\]{}]', x['pass'])) or not len(findall('[a-zA-Z]', x['pass'])) or not len(findall('[0-9]', x['pass'])):
				return '6'

			#Это не почта
			if match('.+@.+\..+', x['mail']) == None:
				return '7'

			query = db['users'].insert({
				'login': x['login'],
				'password': md5(bytes(x['pass'], 'utf-8')).hexdigest(),
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

			'''
			x['pass'] = rsa.decrypt(x['pass'], privkey)
			print(x['pass'])
			'''

			#Неправильный пароль
			query = list(db['users'].find({'login': x['login'], 'password': md5(bytes(x['pass'], 'utf-8')).hexdigest()}))
			if not len(query):
				return '5'

			#print(query[0]['_id'])
			return '0'

#Изменение личной информации
		elif x['cm'] == 'profile':
			#Не все поля заполнены
			if not all([i in x for i in ('name', 'surname')]):
				return '3'

			pass

#Добавление соревнований
		elif x['cm'] == 'competions.add':
			#Не все поля заполнены
			if not all([i in x for i in ('name',)]):
				return '3'

			query = db['competions'].insert({
				'name': x['name'],
				'description': x['description'] if x['description'] else None,
				'cont': x['cont'] if x['cont'] else None,
				'time': x['time'] if x['time'] else None,
				'durability': x['durability'] if x['durability'] else None,
				'author': x['author'] if x['author'] else None,
				'quantity': x['quantity'] if x['quantity'] else None,
				'type': x['type'] if x['type'] else None,
				'prize': x['prize'] if x['prize'] else None,
				'url': x['url'] if x['url'] else None,
				'geo': x['geo'] if x['geo'] else None,
				'stage': x['stage'] if x['stage'] else None,
			})
			print(query, query['_id'])
			return query

#Получить соревнования
		elif x['cm'] == 'competions.gets':
			x = [i['_id'] for i in db['competions'].find()]
			print(x)
			return x

#Получить соревнование
		elif x['cm'] == 'competions.get':
			#Не все поля заполнены
			if not all([i in x for i in ('id',)]):
				return '3'

			x = db['competions'].find_one({'_id': x['id']})
			print(x)
			return x

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'