#!flask/bin/python

from OpenSSL import SSL
context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')

from app import app
app.run(host='0.0.0.0', port=80, debug=True, ssl_context=context)