from flask import render_template
from app import app

@app.route('/login')
def login():
	pass

	return render_template('login.html',
		title = 'Логин', #Аккаунт
		description = 'Регистрация / авторизация',
	)