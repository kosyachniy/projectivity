from flask import render_template
from app import app

@app.route('/index')
def login():
	pass

	return render_template('index.html',
		title = 'Логин',
		description = 'Регистрация / авторизация',
	)