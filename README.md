# ARDA Blog WebApp
#### Data Representation and Querying Project 2016

This repository contains code and documentation about our third year project for Dara Representation and Querying module.

### Project Overview
We have created a Single-Page Web Application (SPA) that is a blog allowing users to post and read entries.
This application was selected after some deliberation.
Initially, we considered three different applications:

1. A [Twitter](http://twitter.com/) alternative.
2. A [Pastebin](http://pastebin.com/) alternative.
3. A [Stackoverflow](https://www.stackoverflow.com/) alternative.

In our early discussions, we excluded option 1 as it would be too difficult to construct in the short time we had to complete the project.
That left option 1 and 2.
We chose 1 after some consideration, as we were more interested in the idea. However, we decided it's not going to be identical to Twitter but we will highly base on it.

The project was guided by the following excerpt from the project instructions:
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

### Architecture
This web application runs in [Python 3](https://www.python.org) using the [Flask](http://flask.pocoo.org/) web micro-framework and uses SQLite as a database.
Python 3 and Flask were requirements for the project, but SQLite was selected by the team.
We chose SQLite as it is easy to use and does not require much setup to get the web application up and running.