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

def del_key(dic, key='_id'):
	del dic[key]
	return dic

@app.route('/', methods=['POST'])
def process():
	x = request.json
	print(x)

	if 'cm' not in x:
		return '2'

	try:
#Регистрация
		if x['cm'] == 'profile.reg':
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
			return 'id%d' % id #сессионный код

#Авторизация
		elif x['cm'] == 'profile.auth':
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
			query = db['users'].find_one({'login': x['login'], 'password': md5(bytes(x['pass'], 'utf-8')).hexdigest()})
			if not query:
				return '5'

			return 'id%d' % query['id'] #сессионный код

#Изменение личной информации
		elif x['cm'] == 'profile.settings':
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
				'id': id,
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
			return 'id%d' % id

#Получить соревнования
		elif x['cm'] == 'competions.gets':
			num = x['num'] if 'num' in x else None
			return dumps([del_key(i) for i in db['competions'].find().sort('id', -1)[0:num]]) #str(i['id'])

#Получить соревнование
		elif x['cm'] == 'competions.get':
			#Не все поля заполнены
			if not all([i in x for i in ('id',)]):
				return '3'

			x = db['competions'].find_one({'id': x['id']})
			print(x)
			return x

#Список пользователей
		elif x['cm'] == 'users.gets':
			num = x['num'] if 'num' in x else None
			return dumps([del_key(i) for i in db['users'].find().sort('id', -1)[0:num]])

#news
#search

		else:
			return '2'

	#Серверная ошибка
	except:
		return '1'