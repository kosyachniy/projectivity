from flask import redirect, request
from app import app

@app.route('/out')
def out():
	user = {'login': None}

	return redirect(request.url, code=302)