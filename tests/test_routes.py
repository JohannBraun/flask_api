import unittest
from task_organizer.app import app
from task_organizer.models import Task

class TestRoutes(unittest.TestCase):
   def setUp(self):
       """
        Create database if needed before test runs. This is called by setUp () so we don't have to worry about it
       """
       self.app = app.test_client()
       db.create_all()

   def tearDown(self):
       """
        Remove database connections and drop all tables in the test database. This is called after each test method to ensure that the tests are clean
       """
       db.session.remove()
       db.drop_all()

   def test_create_task(self):
       """
        Test creating a task in Crowdin. This is a test for issue #441 and the task should be
       """
       response = self.app.post('/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
       self.assertEqual(response.status_code, 201)
       self.assertEqual(Task.query.count(), 1)
