#!usr/bin/env python
""" Welcome to my tiny flask app"""
from flask import Flask, render_template, request, redirect, url_for, abort, session

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'secret';

DS = "postgresql://tim:password@bitnami-postgresql-0ef4.cloudapp.net/todoapp"

APP.config['SQLALCHEMY_DATABASE_URI'] = DS

@APP.route('/')
def home():
    '''home'''
    return render_template('index.html')

@APP.route('/signup', methods=['POST'])
def signup():
    '''signup'''
    session['username'] = request.form['username']
    session['message'] = request.form['message']
    return redirect(url_for('message'))

@APP.route('/message')
def message():
    ''' message username '''
    if 'username' not in session:
        return abort(403)
    return render_template('message.html', username=session['username'], message=session['message'])

if __name__ == "__main__":
    APP.run(debug=True)
    