#!/usr/bin/env python
""" Welcome to my tiny flask app"""
from flask.ext.script import Manager, Shell, Server
from example import APP

MANAGER = Manager(APP)
MANAGER.add_command("runserver", Server())
MANAGER.add_command("shell", Shell())

@MANAGER.command
def createdb():
    '''create db command'''
    from example.models import DB
    DB.create_all()

MANAGER.run()
