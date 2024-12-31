import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# create objects
login_manager = LoginManager()
app = Flask(__name__) # __name__ is the name of the current Python module (a folder with __init__.py)

app.config['SECRET_KEY'] = 'mysecretkey' # used for securely signing the session cookie
basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db) # for database version control

login_manager.init_app(app)
login_manager.login_view = 'login'
