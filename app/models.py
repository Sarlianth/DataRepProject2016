##creating the database model of user with 3 fields (id, nickname and email [where id is the primary key])	
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

	##method that tells Python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)