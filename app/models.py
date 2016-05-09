from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
from app import db

classes = db.Table('classes',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('schedule_id', db.Integer, db.ForeignKey('schedules.id'))
)

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(100))
  lastname = db.Column(db.String(100))
  email = db.Column(db.String(120), unique=True)
  pwdhash = db.Column(db.String(54))
  followed = db.relationship("Schedule", secondary=classes)
   
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
  id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.String(50))
  subject = db.Column(db.String(10))
  catalog_number = db.Column(db.String(10))
  title = db.Column(db.String(200))
  description = db.Column(db.String(1000))

  def __init__(self, course_id, subject, catalog_number, title, description):
    self.course_id = course_id
    self.subject = subject
    self.catalog_number = catalog_number
    self.title = title
    self.description = description

  def __repr__(self):
    return self.subject + self.catalog_number

class Schedule(db.Model):
  __tablename__ = 'schedules'
  id = db.Column(db.Integer, primary_key=True)
  class_number = db.Column(db.Integer)
  enrollment_total = db.Column(db.Integer)
  enrollment_capacity = db.Column(db.Integer)
  followers = db.relationship("User", secondary=classes)

  def __init__(self, class_number, enrollment_total, enrollment_capacity):
    self.class_number = class_number
    self.enrollment_total = enrollment_total
    self.enrollment_capacity = enrollment_capacity
  



