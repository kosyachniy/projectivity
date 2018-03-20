from flask import redirect
from app import app

@app.route('/out')
def out():
	user = {login: None}

	return '<script>document.location.href = document.referrer</script>' #redirect('')