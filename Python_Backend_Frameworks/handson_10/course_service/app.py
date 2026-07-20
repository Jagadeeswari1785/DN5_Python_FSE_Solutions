from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "courses.db"


def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        code TEXT,
        credits INTEGER,
        department_id INTEGER
    )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route("/")
def home():
    return "Course Service Running"


# Create Course
@app.route("/api/courses", methods=["POST"])
def create_course():

    data = request.get_json()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO courses(name,code,credits,department_id)
        VALUES(?,?,?,?)
    """, (
        data["name"],
        data["code"],
        data["credits"],
        data["department_id"]
    ))

    conn.commit()

    course_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "id": course_id,
        "message": "Course Created"
    }), 201


# Get Course
@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM courses WHERE id=?",
        (id,)
    )

    course = cursor.fetchone()

    conn.close()

    if course is None:
        return jsonify({
            "message": "Course not found"
        }), 404

    return jsonify({
        "id": course[0],
        "name": course[1],
        "code": course[2],
        "credits": course[3],
        "department_id": course[4]
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)