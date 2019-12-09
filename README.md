# Flask Kickstart

* pip3 install pipenv
* pipenv shell
* pip3 install Flask
* python app.py
* pip3 install flask-wtf
* pip3 install flask-sqlalchemy

import secrets
secrets.token_hex(16)

from flaskblog import db
db.create_all()
