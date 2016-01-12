from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from uwaterlooapi import UWaterlooAPI as UW
from config import UW_API_KEY

uw = UW(api_key=UW_API_KEY)

from app import views