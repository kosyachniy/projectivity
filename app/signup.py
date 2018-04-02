from flask import session, request, redirect, url_for
from app import app

from requests import post
from time import sleep

LINK = 'http://167.99.128.56/'

@app.route('/signup', methods=['POST'])
def out():
	x = request.form

	if not all([i in x for i in ('login', 'pass', 'name', 'surname', 'mail')]):
		return render_template('message.html', cont='3')

	req = post(LINK, json={'cm': 'profile.auth', 'login': x['login'], 'pass': x['pass'], 'mail': x['mail'], 'name': x['name'], 'surname': x['surname']}).text

	if len(req) < 3:
		return render_template('message.html', cont=req)

	session['token'] = req
	session['login'] = x['login']

	return redirect(url_for('competions'))