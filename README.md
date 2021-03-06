# ARDA Project Web Application
#### Data Representation and Querying Project 2016

This repository contains code and documentation about our third year project for Dara Representation and Querying module.

### Project Overview
We have created a Single-Page Web Application (SPA) 
This web application is a database that stores various user profiles upon creation using the login method, it allows you to view other users profiles aswell as play games on the web application.
Initially, we considered three different applications:

1. A [Twitter](http://twitter.com/) alternative.
2. A [Pastebin](http://pastebin.com/) alternative.
3. A [Stackoverflow](https://www.stackoverflow.com/) alternative.

In our early discussions, we excluded option three as it would be too difficult to construct in the short time we had to complete the project.
That left option one and two or our own idea.
We chose our own idea as none of the other applications seemed appealing for the project.
We thought that own idea would show more of our ability to create a web application rather than reuse other examples.

The project was guided by the following except from the project instructions:
>You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.


### Team Members
We elected to complete this project as a team.
The team members are:
- Adrian Sypos
- Robert Kiliszewski
- Dominykas Urbonas
- Adrian Golias

All team members contributed to all aspects of the project.
However, Dominykas was given the lead in documentation, Adrian Sypos the lead in Python coding, and Robert with Adrian Golias was given the lead in front-end development (HTML, CSS) and user experience.

### Meetings
Team meetings were held every Tuesday (1pm-5am) and Wednesday (1pm-3pm) in the library room at GMIT's Dublin Road campus for the duration of the project.
At these meetings, the management of the project was discussed, among other topics.
The project was divided into separate tasks, and each task was assigned to team members - usually on an individual basis.
At each meeting, Dominykas took notes using their laptop and assigned the tasks using GitHub Issues.


### How to run the application

The following extensions have to be installed in order to run the web application:

pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf

The application is written using the [Flask](http://flask.pocoo.org/) library in [Python 3](https://www.python.org).
Both must be installed to run the project.

We use the [sqlite3](https://docs.python.org/2/library/sqlite3.html) package for persistence in the application.
This must also be installed.
However, no further configuration our setup is required, as the database is fully contained in the db directory in this repository.

Once these prerequisites are installed, the application can be run locally:
```bash
$ python run.py
```
Once the application is running, it can be accessed by pointing your browser at http://127.0.0.1:5000/ .


## How to use application

Within opening the web application page you are asked to sign into the web appllication using one of the following as username OpenID -
Flickr,Yahoo,AOL.

Select one of the providers and select login.

Once logged in there is a drop down menu right under the welcoming paragraph with information of all the users within the database.

You can edit your own profile and view other peoples profiles  that are on the database aswell.

Login in will also give you acess to the game on the web page and you can play it.



### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
We chose SQLite as it is easy to use and does not require much setup to get the web application up and running.

## References
The project was based upon tutorial of Miquel Grinberg https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world which we give a credit for helping us understand the Flask a lightweight Python web framework and teach us how to work with it using his tutorials.

Through the duration of the entire project Stack Overflow http://stackoverflow.com/ has been used to help us with little bugs or mistakes that we might have made or encouneterd. Also helped us alot with understanding certain concepts of working with Flask and Python itself.

We as a group recommend to use both of above references as a baseline to learn how to work with Flask, Python and understand how it works, which will make it extremely easy to do more advanced and complex programming afterwards.
