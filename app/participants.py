from flask import render_template, session
from app import app, LINK

from requests import post
from json import loads

@app.route('/participants')
def participants():
	x = loads(post(LINK, json={'cm': 'participants.gets'}).text)

	return render_template('participants.html',
		title = 'Участники',
		description = 'Участники, набор команды, поиск людей в команду',
		url = 'participants',
		users = x,
		user = {'login': session['login'] if 'token' in session else None},
	)