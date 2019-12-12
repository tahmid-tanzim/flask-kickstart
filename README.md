# Flask Kickstart

* pip3 install pipenv
* pip3 install Flask
* pip3 install flask-wtf
* pip3 install flask-sqlalchemy
* pip3 install flask-bcrypt
* pip3 install flask-login

import secrets
secrets.token_hex(16)

from flaskblog import db
db.create_all()

pipenv shell
python run.py
