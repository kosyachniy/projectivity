from flask import redirect, request
from app import app

@app.route('/out')
def out():
	#логаут

	print(request.data)
	return '<script>document.location.href = document.referrer</script>' #redirect(request.url, code=302)