from flask import session, request, render_template
from app import app, LINK, get_url

from requests import post
from time import sleep

@app.route('/signup', methods=['POST'])
def signup():
	x = request.form

	if not all([i in x for i in ('login', 'pass', 'name', 'surname', 'mail')]):
		return render_template('message.html', cont='3')

	req = post(LINK, json={'cm': 'profile.reg', 'login': x['login'], 'pass': x['pass'], 'mail': x['mail'], 'name': x['name'], 'surname': x['surname']}).text

	if len(req) < 3:
		return render_template('message.html', cont=req)

	session['token'] = req
	session['login'] = x['login']

	return get_url(request.args.get('url'))