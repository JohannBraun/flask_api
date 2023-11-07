import unittest
from task_organizer.app import app
from task_organizer.models import Task

class TestRoutes(unittest.TestCase):
   def setUp(self):
       self.app = app.test_client()
       db.create_all()

   def tearDown(self):
       db.session.remove()
       db.drop_all()

   def test_create_task(self):
       response = self.app.post('/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
       self.assertEqual(response.status_code, 201)
       self.assertEqual(Task.query.count(), 1)
