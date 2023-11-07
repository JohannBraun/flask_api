# Task Organizer
Task Organizer is a simple Flask application that provides a RESTful API for managing tasks. It uses SQLite as its database and SQLAlchemy as the ORM.

## Installation
Clone the repository:

```
git clone https://github.com/JohannBraun/flask_api.git
```


Navigate to the project directory:
```
cd task_organizer
```
Install the required packages:
```
pip install -r requirements.txt
```
## Usage

To run the application, use the following command:
```
python run.py
```
This will start the Flask development server on `http://127.0.0.1:5000.`

## API Endpoints

- `POST /tasks`: Creates a new task. The request body should be a JSON object with a title field and optionally a description field. Returns the ID of the new task.
- `GET /tasks`: Retrieves all tasks. Returns a JSON array of tasks.
- `GET /tasks/<task_id>`: Retrieves a specific task by its ID. Returns a JSON object representing the task. If the task is not found, returns an error message.
- `PUT /tasks/<task_id>`: Updates a specific task by its ID. The request body should be a JSON object with the new title and/or description. Returns a JSON object representing the updated task. If the task is not found, returns an error message.
- `DELETE /tasks/<task_id>`: Deletes a specific task by its ID. Returns a success message. If the task is not found, returns an error message.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
MIT

