##creating the database model of user with 3 fields (id, nickname and email [where id is the primary key])	
from app import db
from hashlib import md5
##user class with (id, nickname, email and post object)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    about_me = db.Column(db.String(800))
    last_seen = db.Column(db.DateTime)
	
	##return True unless the object represents a user that should not be allowed to authenticate for some reason.
    @property
    def is_authenticated(self):
        return True
	
	##return True for users unless they are inactive
    @property
    def is_active(self):
        return True
	
	##return True only for fake users
    @property
    def is_anonymous(self):
        return False
		
	##return a unique identifier for the user
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3
			
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % \
            (md5(self.email.encode('utf-8')).hexdigest(), size)
		
##method to create unique nickname, in case of a duplicate
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() is None:
            return nickname
        ver = 2
        while True:
            new_nickname = nickname + str(ver)
            if User.query.filter_by(nickname=new_nickname).first() is None:
                break
            ver += 1
        return new_nickname
		
	##method that tells Python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)