#!/usr/bin/python
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import calendar,datetime, hashlib
from datetime import datetime
import json
from bson import json_util

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from app import views, models


def flot(timestamp):
    
    return calendar.timegm(timestamp.timetuple()) * 1000

app.jinja_env.globals.update(flot=flot)


def hash(anything):
    return '_' + hashlib.md5(anything).hexdigest()

app.jinja_env.globals.update(hash=hash)


def d2s(datetime):
    return datetime.strftime("%D %H %M")
app.jinja_env.globals.update(d2s = d2s)

def jsoni(uni):
    return json.loads(uni, object_hook=json_util.object_hook)
app.jinja_env.globals.update(jsoni = jsoni)