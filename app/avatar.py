from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post
import base64

@app.route('/avatar', methods=['POST'])
def avatar():
	x = request.files['file'].stream.read()
	x = str(base64.b64encode(x))

	if 'token' not in session:
		return render_template('message.html', cont='3')

	req = post(LINK, json={'cm': 'profile.settings', 'token': session['token'], 'photo': x}).text

	if len(req) < 3:
		return render_template('message.html', cont=req)

	return redirect(LINK + 'cabinet')