from flask import render_template, session, request
from app import app, LINK, get_user

from requests import post
from json import loads

@app.route('/login')
def login():
	return render_template('login.html',
		title = 'Логин', #Аккаунт
		description = 'Регистрация / авторизация',
		url = request.args.get('url'),
		user = user,
	)