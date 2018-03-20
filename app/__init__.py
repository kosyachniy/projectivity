from flask import Flask

app = Flask(__name__)

from app import process
from app import index
from app import login
from app import out
from app import errors