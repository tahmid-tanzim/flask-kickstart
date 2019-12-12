from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3f6db2fe4ec99f04db9b1c1ab0cc55f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-blog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'
login_manager.login_message_category = 'info'

from flaskblog import routes

