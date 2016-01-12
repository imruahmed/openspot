from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from app import db
 
class User(db.Model):
  __tablename__ = 'users'
  uid = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
   
  def __init__(self, firstname, lastname, email, password):
    self.firstname = firstname.title()
    self.lastname = lastname.title()
    self.email = email.lower()
    self.set_password(password)
     
  def set_password(self, password):
    self.pwdhash = generate_password_hash(password)
   
  def check_password(self, password):
    return check_password_hash(self.pwdhash, password)

  def __repr__(self):
    return '<User %r>' % (self.email)

class Course(db.Model):
  __tablename__ = 'courses'
  uid = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.String(50))
  subject = db.Column(db.String(10))
  catalog_number = db.Column(db.String(10))
  title = db.Column(db.String(200))
  description = db.Column(db.String(1000))
  schedule = db.relationship()

  def __init__(self, course_id, subject, catalog_number, title, description):
    self.course_id = course_id
    self.subject = subject
    self.catalog_number = catalog_number
    self.title = title
    self.description = description

  def __repr__(self):
    return self.subject + self.catalog_number

class Schedule(db.Model):
  uid = db.Column(db.Integer, primary_key=True)
  section = db.Column(db.String(10))
  class_id = db.Column(db.Integer)
  campus = db.Column(db.String(5))
  enroll_cap = db.Column(db.Integer)
  enroll_tot = db.Column(db.Integer)
  start_time = db.Column(db.String(10))
  end_time = db.Column(db.String(10))
  weekdays = db.Column(db.String(10))
  instructors = db.Column(db.String(64))
  




