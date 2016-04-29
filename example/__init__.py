#!usr/bin/env python
""" Moduly """
from flask import Flask, render_template, request, redirect, url_for, abort, session
# from models import User
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config.from_pyfile('tokens.py')
DB = SQLAlchemy(APP)

class User(DB.Model):
    ''' user model '''
    

class User(self, DB.Model):
    '''User model'''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(60))
    message = DB.Column(DB.String)

    def __init__(self, username, message):
        self.username = username
        self.message = message

@APP.route('/')
def home():
    '''home'''
    return render_template('index.html')

@APP.route('/signup', methods=['POST'])
def signup():
    '''signup'''
    user = User(request.form['username'], request.form['message'])
    DB.session.add(user)
    DB.session.commit()
    return redirect(url_for('message', username=user.username))

@APP.route('/message')
def message():
    ''' message username '''
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('message.html', username=user.username, message=user.message)

def dbinit():
    ''' Welp '''
    DB.drop_all()
    DB.create_all()
    DB.session.add(User(username='bob'))

if __name__ == "__main__":
    APP.run(debug=True)
    