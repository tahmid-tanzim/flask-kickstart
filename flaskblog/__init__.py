from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e3f6db2fe4ec99f04db9b1c1ab0cc55f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-blog.bd'
db = SQLAlchemy(app)


from flaskblog import routes

