from flask import render_template, flash, redirect
from app import app, db
from .forms import LoginForm

# index view function suppressed for brevity
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Adrian'}
    posts = [
        {
            'author': {'nickname': 'Michael'},
            'body': 'This app is so cool!'
        },
        {
            'author': {'nickname': 'Paddy'},
            'body': 'Wow, just got 95% in my java exam!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])

##creating the database model of user with 3 fields (id, nickname and email [where id is the primary key])

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

	##method that tells Python how to print objects of this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)