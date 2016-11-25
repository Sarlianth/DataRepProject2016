from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
##importing models module

app = Flask(__name__)
app.config.from_object('config')
##creating db object that will be our database
db = SQLAlchemy(app)

from app import views, models