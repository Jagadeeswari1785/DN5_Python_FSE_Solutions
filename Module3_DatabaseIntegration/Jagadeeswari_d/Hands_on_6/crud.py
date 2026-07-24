from datetime import date

from sqlalchemy.orm import sessionmaker, joinedload
from models import (
    engine,
    Department,
    Student,
    Course,
    Enrollment
)

# --------------------------------------------------
# Hands-On 6
# N+1 Query Comparison
#
# Without joinedload:
# Multiple SQL queries are executed (N+1 problem).
#
# With joinedload:
# Only one SQL query is executed using JOINs.
# This improves performance.
# --------------------------------------------------

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------------------------
# INSERT Departments
# --------------------------------------------------

if session.query(Department).count() == 0:

    cs = Department(dept_name="Computer Science")
    it = Department(dept_name="Information Technology")
    ece = Department(dept_name="Electronics")

    session.add_all([cs, it, ece])
    session.commit()

    print("Departments inserted.")

# --------------------------------------------------
# INSERT Students
# --------------------------------------------------

if session.query(Student).count() == 0:

    departments = session.query(Department).all()

    students = [
        Student(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            enrollment_year=2022,
            department=departments[0]
        ),
        Student(
            first_name="Alice",
            last_name="Smith",
            email="alice@example.com",
            enrollment_year=2023,
            department=departments[0]
        ),
        Student(
            first_name="Bob",
            last_name="Johnson",
            email="bob@example.com",
            enrollment_year=2022,
            department=departments[1]
        ),
        Student(
            first_name="David",
            last_name="Lee",
            email="david@example.com",
            enrollment_year=2024,
            department=departments[2]
        ),
        Student(
            first_name="Emma",
            last_name="Wilson",
            email="emma@example.com",
            enrollment_year=2023,
            department=departments[1]
        )
    ]

    session.add_all(students)
    session.commit()

    print("Students inserted.")

# --------------------------------------------------
# INSERT Courses
# --------------------------------------------------

if session.query(Course).count() == 0:

    courses = [

        Course(
            course_name="Database Systems",
            credits=4
        ),

        Course(
            course_name="Python Programming",
            credits=3
        ),

        Course(
            course_name="Operating Systems",
            credits=4
        )
    ]

    session.add_all(courses)
    session.commit()

    print("Courses inserted.")

# --------------------------------------------------
# INSERT Enrollments
# --------------------------------------------------

if session.query(Enrollment).count() == 0:

    students = session.query(Student).all()
    courses = session.query(Course).all()

    enrollments = [

        Enrollment(
            student=students[0],
            course=courses[0],
            enrollment_date=date(2024, 1, 10),
            grade="A"
        ),

        Enrollment(
            student=students[1],
            course=courses[1],
            enrollment_date=date(2024, 1, 15),
            grade="B"
        ),

        Enrollment(
            student=students[2],
            course=courses[2],
            enrollment_date=date(2024, 1, 20),
            grade="A"
        ),

        Enrollment(
            student=students[3],
            course=courses[0],
            enrollment_date=date(2024, 1, 25),
            grade="C"
        )

    ]

    session.add_all(enrollments)
    session.commit()

    print("Enrollments inserted.")

# --------------------------------------------------
# READ
# Students in Computer Science
# --------------------------------------------------

print("\nStudents in Computer Science:\n")

students = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
    .all()
)

for student in students:
    print(student.first_name, student.last_name)

# --------------------------------------------------
# READ
# Enrollment Details
# --------------------------------------------------

print("\nEnrollment Details:\n")

enrollments = session.query(Enrollment).all()

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )

# --------------------------------------------------
# UPDATE
# --------------------------------------------------

student = (
    session.query(Student)
    .filter(Student.email == "john@example.com")
    .first()
)

if student:
    student.enrollment_year = 2025
    session.commit()
    print("\nStudent updated.")

# --------------------------------------------------
# DELETE
# --------------------------------------------------

enrollment = session.query(Enrollment).first()

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("One enrollment deleted.")

# --------------------------------------------------
# joinedload (Fix N+1)
# --------------------------------------------------

print("\nUsing joinedload:\n")

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        "->",
        e.course.course_name
    )

session.close()