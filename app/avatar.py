from flask import session, request, render_template, redirect
from app import app, LINK

from requests import post

@app.route('/avatar', methods=['POST'])
def avatar():
	x = request.files['file']

	if 'token' not in session:
		return render_template('message.html', cont='3')

	req = post(LINK, json={'cm': 'profile.settings', 'token': session['token'], 'photo': x, 'type_img': 'byte'}).text

	if len(req) < 3:
		return render_template('message.html', cont=req)

	return redirect(LINK + 'cabinet')