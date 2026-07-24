from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Date,
    Numeric
)
from sqlalchemy.orm import declarative_base, relationship

# PostgreSQL Connection
DATABASE_URL = "postgresql+psycopg2://postgres:1785@localhost:5433/college_db_orm"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()


# ---------------- Department ----------------
class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)

    students = relationship("Student", back_populates="department")


# ---------------- Student ----------------
class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100), unique=True)
    enrollment_year = Column(Integer)

    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# ---------------- Professor ----------------
class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))


# ---------------- Course ----------------
class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    credits = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course")


# ---------------- Enrollment ----------------
class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    enrollment_date = Column(Date)
    grade = Column(String(2))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All tables created successfully!")