from .models import Task
from .app import app
from task_organizer.app import db
from flask import request, jsonify

@app.route('/tasks', methods=['POST'])
def create_task():
   """
    Create a task in the database. This is a POST request to / api / v1 / tasks
    
    
    Returns: 
    	 a JSON with the id of the task that was created or an error message if something went wrong ( HTTP 201
   """
   title = request.json['title']
   description = request.json.get('description', '')
   new_task = Task(title=title, description=description)
   db.session.add(new_task)
   db.session.commit()
   return jsonify({'id': new_task.id}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
   """
    Get all tasks in JSON format. This is used to render a list of tasks that can be viewed by the front end.
    
    
    Returns: 
    	 JSON with a list of tasks in JSON format. Example request **. : http Example response **. :
   """
   tasks = Task.query.all()
   return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
   """
    Get information about a task. This is a REST call to the task. json endpoint. It will return a JSON object with the following fields.
    
    Args:
    	 task_id: The id of the task to get.
    
    Returns: 
    	 A JSON object with the following fields : id title description error ( if exists ) id ( int )
   """
   task = Task.query.get(task_id)
   # Returns a 404 if task is not found
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
   """
    Update task title and / or description. This endpoint is used to update the title and / or description of a task.
    
    Args:
    	 task_id: id of task to update. It is the primary key of the task table.
    
    Returns: 
    	 status code 200 if task updated successfully status code 404 if task not found or not found with json data
   """
   task = Task.query.get(task_id)
   # Returns a 404 if task is not found
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   task.title = request.json.get('title', task.title)
   task.description = request.json.get('description', task.description)
   db.session.commit()
   return jsonify({'id': task.id, 'title': task.title, 'description': task.description})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
   """
    Delete task by task_id. This will be used by ajax call to delete a task. The task must exist in the database before it can be deleted.
    
    Args:
    	 task_id: id of task to delete. It is required
    
    Returns: 
    	 json with result of
   """
   task = Task.query.get(task_id)
   # Returns a 404 if task is not found
   if task is None:
       return jsonify({'error': 'Task not found'}), 404
   db.session.delete(task)
   db.session.commit()
   return jsonify({'result': 'Task deleted'})
