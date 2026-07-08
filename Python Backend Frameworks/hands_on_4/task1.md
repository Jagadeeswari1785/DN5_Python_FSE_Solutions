Step 1: Install the required packages
pip install flask flask-sqlalchemy flask-migrate
Step 2: Create the project structure
handson_04/
│
├── app.py
├── config.py
├── requirements.txt
└── courses/
    ├── __init__.py
    └── routes.py
Step 3: Create config.py
class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///coursemanager.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
Step 4: Create courses/routes.py
from flask import Blueprint, jsonify, request

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)

courses = []


@courses_bp.route("/", methods=["GET"])
def get_courses():
    return jsonify(courses)


@courses_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()
    courses.append(data)
    return jsonify(data), 201
Step 5: Create app.py
from flask import Flask
from config import Config
from courses.routes import courses_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(courses_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
Step 6: Create courses/__init__.py
# Empty file
Step 7: Run the application
python app.py
Step 8: Test
Open:

GET http://127.0.0.1:5000/api/courses/
Output:

[]
Create a course:

POST http://127.0.0.1:5000/api/courses/
Body:

{
    "name": "Python",
    "code": "CS101",
    "credits": 4
}
Expected response:

{
    "name": "Python",
    "code": "CS101",
    "credits": 4
}
