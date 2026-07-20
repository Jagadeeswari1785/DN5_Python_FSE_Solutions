from flask import Blueprint, jsonify, request
from extensions import db
from courses.models import Course, Student

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def success_response(data, status=200):
    return jsonify({
        "status": "success",
        "data": data
    }), status


def error_response(message, status):
    return jsonify({
        "status": "error",
        "message": message
    }), status


@courses_bp.route("/", methods=["GET"])
def get_courses():
    all_courses = Course.query.all()
    return success_response([course.to_dict() for course in all_courses])


@courses_bp.route("/", methods=["POST"])
def create_course():
    payload = request.get_json(silent=True)

    if not payload:
        return error_response("No JSON data received", 400)

    required_fields = ["name", "code", "credits"]

    for field in required_fields:
        if field not in payload:
            return error_response(f"{field} is required", 400)

    new_course = Course(
        name=payload["name"],
        code=payload["code"],
        credits=payload["credits"]
    )

    db.session.add(new_course)
    db.session.commit()

    return success_response(new_course.to_dict(), 201)


@courses_bp.route("/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get(course_id)

    if course is None:
        return error_response("Course not found", 404)

    return success_response(course.to_dict())


@courses_bp.route("/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    course = Course.query.get(course_id)

    if course is None:
        return error_response("Course not found", 404)

    payload = request.get_json(silent=True)

    if not payload:
        return error_response("No JSON data received", 400)

    course.name = payload.get("name", course.name)
    course.code = payload.get("code", course.code)
    course.credits = payload.get("credits", course.credits)

    db.session.commit()

    return success_response(course.to_dict())


@courses_bp.route("/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get(course_id)

    if course is None:
        return error_response("Course not found", 404)

    db.session.delete(course)
    db.session.commit()

    return success_response({"message": "Course deleted"})


@courses_bp.route("/<int:course_id>/students/", methods=["GET"])
def get_students(course_id):
    course = Course.query.get(course_id)

    if course is None:
        return error_response("Course not found", 404)

    students = (
        db.session.query(Student)
        .join(Student.enrollments)
        .filter_by(course_id=course_id)
        .all()
    )

    return success_response(
        [student.to_dict() for student in students]
    )