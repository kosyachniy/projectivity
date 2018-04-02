from flask import render_template
from app import app, LINK, get_user

from requests import post
from json import loads

@app.route('/participants')
def participants():
	x = loads(post(LINK, json={'cm': 'users.gets'}).text)

	return render_template('participants.html',
		title = 'Участники',
		description = 'Участники, набор команды, поиск людей в команду',
		url = 'competions',
		users = x,
		user = get_user(),
	)