import unittest
from task_organizer.app import db
from task_organizer.models import Task

class TestModels(unittest.TestCase):
   def setUp(self):
       self.app = create_app('testing')
       self.app_context = self.app.app_context()
       self.app_context.push()
       db.create_all()

   def tearDown(self):
       db.session.remove()
       db.drop_all()
       self.app_context.pop()

   def test_task_creation(self):
       task = Task(title='Test Task', description='Test Description')
       db.session.add(task)
       db.session.commit()
       self.assertEqual(Task.query.count(), 1)
