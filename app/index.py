from flask import render_template, session
from app import app, LINK

from requests import post
from json import loads

@app.route('/', methods=['GET'])
@app.route('/index')
def index():
	categories = loads(post(LINK, json={'method': 'categories.gets'}).text)
	user = loads(post(LINK, json={'method': 'users.get', 'id': session['id']}).text) if 'id' in session else {'id': 0, 'admin': 2}

	articles = loads(post(LINK, json={'method': 'articles.gets', 'count': 6}).text)

	return render_template('index.html',
		title = 'Главная',
		description = '',
		url = 'index',
		categories = categories,
		user = user,

		articles = articles,
	)