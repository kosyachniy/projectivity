from flask import render_template, session, request
from app import app

from requests import post
from json import loads

@app.route('/cabinet')
def cabinet():
	#получить параметры
	#получить пользователя

	return render_template('cabinet.html',
		title = 'Личный кабинет',
		description = 'Личный кабинет, настройки, аккаунт, профиль',
		url = 'cabinet',
		user = {'login': session['login'] if 'token' in session else None},
	)