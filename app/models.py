##creating the database model of user with 3 fields (id, nickname and email [where id is the primary key])	
from app import db
##user class with (id, nickname, email and post object)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
	##method that tells Python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)
##post class with (id, body, timestamd and user_id as a foreignKey so we know which user wrote the post)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
	##this is a foreignKey relating on ID from user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)