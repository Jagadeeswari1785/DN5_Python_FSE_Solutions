from flask import Flask, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

DATABASE = "students.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER
    )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return "Student Service Running"


# Create Student
@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students(first_name,last_name,email)
        VALUES(?,?,?)
    """, (
        data["first_name"],
        data["last_name"],
        data["email"]
    ))

    conn.commit()

    student_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": student_id,
        "message": "Student Created"
    }), 201


# Enroll Student
@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    data = request.get_json()

    course_id = data["course_id"]

    try:
        response = requests.get(
            f"http://127.0.0.1:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO enrollments(student_id,course_id)
        VALUES(?,?)
    """, (id, course_id))

    conn.commit()

    enrollment_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": enrollment_id,
        "message": "Enrollment Successful"
    })


if __name__ == "__main__":
    app.run(port=5002, debug=True)