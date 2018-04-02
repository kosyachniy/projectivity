from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import process
from app import index
from app import login
from app import signup
from app import signin
from app import out
from app import errors