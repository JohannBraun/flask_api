# A task organizer with no data. It is used to store data in the database for testing purposes
from task_organizer.app import db

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(500), nullable=True)