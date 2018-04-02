from flask import render_template, session, request
from app import app, LINK

from requests import post
from json import loads

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
		url = request.args.get('url'),
		user = user,
	)