# Task Organizer Application
This is a simple Flask application that provides a RESTful API for managing tasks. The application uses SQLite as its database and SQLAlchemy as the ORM.

## File Structure
- `app.py`: This file sets up the Flask application and the SQLAlchemy database connection.
- `db.py:` This file defines a function to create the database tables.
- `models.py`: This file defines the Task model, which represents a task in the database.
- `routes.py`: This file defines the routes for the Flask application, which provide the API for managing tasks.
- `run.py`: This file is the entry point for running the Flask application.

### Models
#### Task
- `id`: The unique identifier for the task. This is the primary key in the database.
- `title`: The title of the task. This field is required.
- `description`: The description of the task. This field is optional.

### Routes
- `POST /tasks`: Creates a new task. The request body should be a JSON object with a title field and optionally a description field. Returns the ID of the new task.
- `GET /tasks`: Retrieves all tasks. Returns a JSON array of tasks.
- `GET /tasks/<task_id>`: Retrieves a specific task by its ID. Returns a JSON object representing the task. If the task is not found, returns an error message.
- `PUT /tasks/<task_id>`: Updates a specific task by its ID. The request body should be a JSON object with the new title and/or description. Returns a JSON object representing the updated task. If the task is not found, returns an error message.
- `DELETE /tasks/<task_id>`: Deletes a specific task by its ID. Returns a success message. If the task is not found, returns an error message.

## Running the Application
To run the application, use the command python run.py. This will start the Flask development server on http://127.0.0.1:5000.

