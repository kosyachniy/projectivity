from flask import session, request
from app import app

from reqs import post

LINK = 'http://167.99.128.56/'

@app.route('/signin', methods=['POST'])
def out():
	x = request.json
	req = post(LINK, json={'cm': 'profile.auth', 'login': x['login'], 'pass': x['pass']}).text

	if len(req) > 2:
		session['token'] = req
		session['login'] = x['login']

		return '<script>document.location.href = document.referrer</script>'

	else:
		return req