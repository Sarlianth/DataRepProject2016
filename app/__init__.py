import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
##importing models module

app = Flask(__name__)
app.config.from_object('config')
##creating db object that will be our database
db = SQLAlchemy(app)
##configurating Flask-Login and Flask-OpenID
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
##path to a temp folder where files can be stored
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models