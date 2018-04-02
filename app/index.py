from flask import render_template, session
from app import app, LINK, get_user

from requests import post
from json import loads

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	competions = loads(post(LINK, json={'cm': 'competions.gets', 'num': 2}).text)
	users = loads(post(LINK, json={'cm': 'users.gets', 'num': 2}).text)

	return render_template('index.html',
		title = 'Главная',
		description = '',
		url = 'index',
		competions = competions,
		users = users,
		user = get_user(),
	)