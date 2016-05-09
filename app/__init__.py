from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from uwaterlooapi import UWaterlooAPI as UW
from config import UW_API_KEY

uw = UW(api_key=UW_API_KEY)
mail = Mail(app)

from app import views