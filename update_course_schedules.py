from flask.ext.mail import Message
from app import app, db, uw, mail
from app.models import User, Schedule
from config import ADMINS as A

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# Cron job for updating db
def cron_update_db():
	
	schedules = Schedule.query.all()
	for s in schedules:
		emails = ['im.ahmed97@gmail.com']
		msg = Message("YO", sender=A[0], recipients=emails)
    	msg.body = "workgin on it"
    	msg.html = "body"

    	thr = Thread(target=send_async_email, args=[app, msg])
    	thr.start()

cron_update_db()