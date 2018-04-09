from flask import render_template, session
from app import app, LINK

from requests import post
from json import loads

@app.route('/competions/<id>')
def competion(id):
	x = loads(post(LINK, json={'cm': 'competions.get', 'id': int(id)}).text)

	return render_template('competion.html',
		title = x['name'],
		description = 'Конкурс, стартап, конференция, хакатон, олимпиада, соревнование',
		url = 'competions/' + id,
		competion = x,
		user = {'login': session['login'] if 'token' in session else None},
	)