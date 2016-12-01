##creating the form models
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from app.models import User

##login form model
class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

##edit form model
class EditForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

	##determine if the nickname has changed or not
    def validate(self):
        if not Form.validate(self):
            return False
        ##If hasn't changed then it accepts it
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        ##makes sure the new nickname does not exist in the database
        if user != None:
            self.nickname.errors.append('This nickname already exists. Try again..')
            return False
        return True