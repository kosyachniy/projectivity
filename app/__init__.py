from flask import Flask

app = Flask(__name__)

import rsa
pubkey, privkey = rsa.newkeys(512)

from app import process
from app import index
from app import login
from app import out