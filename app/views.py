from flask import render_template, request, redirect, session, url_for, flash
from app import app, db, uw

from models import User, Course, Schedule
from forms import SignupForm, SigninForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()

  if 'email' in session:
    return redirect(url_for('profile')) 
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:   
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
      
      session['email'] = newuser.email
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()

  if 'email' in session:
    return redirect(url_for('profile')) 
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('index'))

@app.route('/profile')
def profile():
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html', user=user)

@app.route('/courses')
def courses():
    return render_template('courses.html', courses=Course.query.all())

@app.route('/courses/<course_id>')
def course(course_id):
  course = Course.query.filter_by(course_id=course_id).first();
  return render_template('course.html', course=course)

@app.route('/search/<subject>/<catalog_number>')
def search(subject, catalog_number):
  if 'email' not in session:
    return redirect(url_for('signin')) 

  user = User.query.filter_by(email = session['email']).first()

  if user is None:
    return redirect(url_for('signin'))

  stuff = [i.class_number for i in user.followed]
  course = uw.course(subject, catalog_number)
  sched = uw.course_schedule(subject, catalog_number)
  return render_template('search.html', stuff=stuff, course=course, sched=sched)

@app.route('/search/followed/<cn>/<et>/<ec>')
def follow(cn, et, ec):
  if 'email' not in session:
    return redirect(url_for('signin'))

  user = User.query.filter_by(email = session['email']).first()

  if user is None:
    return redirect(url_for('signin'))

  if Schedule.query.filter_by(class_number=cn).first() is None:
    s = Schedule(class_number=cn, enrollment_total=et, enrollment_capacity=ec)
  else:
    s = Schedule.query.filter_by(class_number=cn).first() 

  user.followed.append(s)
  db.session.commit()
    
  return redirect(url_for('profile'))

@app.route('/search/unfollowed/<cn>/<et>/<ec>')
def unfollow(cn, et, ec):
  if 'email' not in session:
    return redirect(url_for('signin'))

  user = User.query.filter_by(email = session['email']).first()

  if user is None:
    return redirect(url_for('signin'))

  if Schedule.query.filter_by(class_number=cn).first() is None:
    return redirect(url_for('profile'))
  else:
    s = Schedule.query.filter_by(class_number=cn).first() 

  user.followed.remove(s)
  db.session.delete(s)
  db.session.commit()
    
  return redirect(url_for('profile'))


