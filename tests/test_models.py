import unittest
from task_organizer.app import db
from task_organizer.models import Task

class TestModels(unittest.TestCase):
   def setUp(self):
       """
        Create app and app_context for testing. This is called at the beginning of the test and should not be called directly
       """
       self.app = create_app('testing')
       self.app_context = self.app.app_context()
       self.app_context.push()
       db.create_all()

   def tearDown(self):
       """
        Remove session and drop all tables in app_context. This is called after each test to ensure that we don't accidentally drop tables
       """
       db.session.remove()
       db.drop_all()
       self.app_context.pop()

   def test_task_creation(self):
       """
        Test creating a task and committing it to the database. 
       """
       task = Task(title='Test Task', description='Test Description')
       db.session.add(task)
       db.session.commit()
       self.assertEqual(Task.query.count(), 1)
