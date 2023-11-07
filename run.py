from task_organizer.app import app
from task_organizer.db import create_db
import task_organizer.routes  # Add this line


if __name__ == "__main__":
   with app.app_context():
       create_db()
   app.run(debug=True)