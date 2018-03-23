from flask import request, jsonify
from app import app

from mongodb import *
from re import findall, match
from hashlib import md5
from json import dumps

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
'''
#Получение публичного ключа
		if x['cm'] == 'key':
			return str(str(pubkey.n) + ',' + str(pubkey.e))
'''

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

			try:
				id = db['users'].find().sort('id', -1)[0]['id'] + 1
			except:
				id = 1

			query = db['users'].insert({
				'id': id,
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
			return '0' #сессионный код

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

			try:
				id = db['competions'].find().sort('id', -1)[0]['id'] + 1
			except:
				id = 1

			query = db['competions'].insert({
				'id': x['id'],
				'name': x['name'],
				'description': x['description'] if 'description' in x else None,
				'cont': x['cont'] if 'cont' in x else None,
				'time': x['time'] if 'time' in x else None,
				'durability': x['durability'] if 'durability' in x else None,
				'author': x['author'] if 'author' in x else None,
				'quantity': x['quantity'] if 'quantity' in x else None,
				'type': x['type'] if 'type' in x else None,
				'prize': x['prize'] if 'prize' in x else None,
				'url': x['url'] if 'url' in x else None,
				'geo': x['geo'] if 'geo' in x else None,
				'stage': x['stage'] if 'stage' in x else None,
			})
			return query

#Получить соревнования
		elif x['cm'] == 'competions.gets':
			return dumps([str(i['id']) for i in db['competions'].find()])

#Получить соревнование
		elif x['cm'] == 'competions.get':
			#Не все поля заполнены
			if not all([i in x for i in ('id',)]):
				return '3'

			x = db['competions'].find_one({'id': x['id']})
			print(x)
			return x

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'