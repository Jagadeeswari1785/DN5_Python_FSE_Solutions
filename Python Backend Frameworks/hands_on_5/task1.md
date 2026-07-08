Step 1: Open app.py
If you don't already have SQLAlchemy initialized, install the required packages:

pip install flask-sqlalchemy flask-migrate
Step 2: Initialize SQLAlchemy
In app.py, add:

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
Inside create_app():

db.init_app(app)

migrate = Migrate(app, db)
Step 3: Create courses/models.py
Inside the courses folder, create a new file:

courses/
    models.py
Step 4: Define the models
In courses/models.py, create the following models:

Department

Course

Student

Enrollment

Use db.Model as the base class and include the same fields you used in the Django project:

Department: name, head_of_dept, budget

Course: name, code (unique), credits, department_id

Student: first_name, last_name, email (unique), department_id, enrollment_year

Enrollment: student_id, course_id, enrollment_date, grade

Step 5: Add relationships
Add relationships such as:

Department ↔ Courses

Student ↔ Enrollments

Course ↔ Enrollments

Example:

courses = db.relationship(
    "Course",
    back_populates="department"
)
Step 6: Save the file
Press Ctrl + S.

Step 7: Initialize migrations
Open the terminal in your project folder and run:

flask db init
Step 8: Create the migration
flask db migrate -m "initial schema"
Step 9: Apply the migration
flask db upgrade
This creates the database tables.

Step 10: Open the Flask shell
flask shell
Step 11: Insert sample data
Inside the Flask shell, create:

2 Departments

3 Courses

Then save them using:

db.session.add(...)
db.session.commit()
Step 12: Verify the data
Run:

Course.query.all()
You should see the inserted courses.

Expected Outcome
SQLAlchemy models created.

Database tables created.

Sample data inserted successfully.
