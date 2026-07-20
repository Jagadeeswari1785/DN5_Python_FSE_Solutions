from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

COURSE_SERVICE = "http://127.0.0.1:5001"
STUDENT_SERVICE = "http://127.0.0.1:5002"


# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return "API Gateway Running"


# -----------------------------
# Route Course Requests
# -----------------------------
@app.route("/api/courses", methods=["POST"])
def create_course():

    response = requests.post(
        f"{COURSE_SERVICE}/api/courses",
        json=request.get_json()
    )

    return jsonify(response.json()), response.status_code


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    response = requests.get(
        f"{COURSE_SERVICE}/api/courses/{id}"
    )

    return jsonify(response.json()), response.status_code


# -----------------------------
# Route Student Requests
# -----------------------------
@app.route("/api/students", methods=["POST"])
def create_student():

    response = requests.post(
        f"{STUDENT_SERVICE}/api/students",
        json=request.get_json()
    )

    return jsonify(response.json()), response.status_code


@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    response = requests.post(
        f"{STUDENT_SERVICE}/api/students/{id}/enroll",
        json=request.get_json()
    )

    return jsonify(response.json()), response.status_code


if __name__ == "__main__":
    app.run(port=5000, debug=True)