'''model declaration'''
from flask_sqlalchemy import SQLAlchemy
from example import APP

DB = SQLAlchemy(APP) 

class User(DB.Model):
    '''User model'''
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String)
    message = DB.Column(DB.String)
    
    def __init__(self, username, message):
        self.username = username
        self.message = message 