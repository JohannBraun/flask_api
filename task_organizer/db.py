from task_organizer.app import db
from task_organizer.models import Task

def create_db():
  db.create_all()