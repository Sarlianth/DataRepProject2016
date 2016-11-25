from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
##creating db object that will be our database
db = SQLAlchemy(app)

##importing models module
from app import views, models