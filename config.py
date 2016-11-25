import os
basedir = os.path.abspath(os.path.dirname(__file__))

##activates the cross-site request forgery prevention
WTF_CSRF_ENABLED = True
##only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form
SECRET_KEY = 'you-will-never-guess'

##providers for openID
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

##required by the Flask-SQLAlchemy extension. Path to our database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
##folder where we will store SQLAlchemy-migrate files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')