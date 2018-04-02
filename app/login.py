from flask import render_template, session
from app import app

from requests import post
from json import loads

LINK = 'http://167.99.128.56/'

@app.route('/login')
def login():
	pass

	if 'token' in session:
		user = {'login': session['login']}
	else:
		user = {'login': None}

	return render_template('login.html',
		title = 'Логин', #Аккаунт
		description = 'Регистрация / авторизация',
		user = user,
	)