from .models import Task
from .app import app
from task_organizer.app import db
from flask import request, jsonify

@app.route('/tasks', methods=['POST'])
def create_task():
   title = request.json['title']
   description = request.json.get('description', '')
   new_task = Task(title=title, description=description)
   db.session.add(new_task)
   db.session.commit()
   return jsonify({'id': new_task.id}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
   tasks = Task.query.all()
   return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
   task = Task.query.get(task_id)
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
   task = Task.query.get(task_id)
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   task.title = request.json.get('title', task.title)
   task.description = request.json.get('description', task.description)
   db.session.commit()
   return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
   task = Task.query.get(task_id)
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   db.session.delete(task)
   db.session.commit()
   return jsonify({'result': 'Task deleted'})
