import asyncio
from contextlib import asynccontextmanager

from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Response
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, create_tables
from models import Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Course Management API",
    description="API for managing courses, students and enrollments.",
    version="1.0",
    contact={
        "name": "Your Name",
        "email": "yourname@example.com"
    },
    lifespan=lifespan
)
def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


@app.get("/", tags=["Home"])
async def home():
    return {"message": "API running"}


# CREATE
@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new course",
    response_description="Course created successfully"
)
async def create_course(
    response: Response,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    response.headers["Location"] = f"/api/courses/{new_course.id}"
    return {
        "id": new_course.id,
        "name": new_course.name,
        "code": new_course.code,
        "credits": new_course.credits,
        "department_id": new_course.department_id
    }


# GET ONE
@app.get(
    "/api/courses/{course_id}", tags=["Courses"],
    response_model=CourseResponse
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "id": course.id,
        "name": course.name,
        "code": course.code,
        "credits": course.credits,
        "department_id": course.department_id
    }


# GET ALL


@app.get(
    "/api/courses/", tags=["Courses"],
    response_model=List[CourseResponse]
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    courses = result.scalars().all()

    return [
        {
            "id": c.id,
            "name": c.name,
            "code": c.code,
            "credits": c.credits,
            "department_id": c.department_id
        }
        for c in courses
    ]


# UPDATE
@app.put(
    "/api/courses/{course_id}", tags=["Courses"],
    response_model=CourseResponse
)
async def update_course(
    course_id: int,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db_course.name = course.name
    db_course.code = course.code
    db_course.credits = course.credits
    db_course.department_id = course.department_id

    await db.commit()
    await db.refresh(db_course)

    return {
        "id": db_course.id,
        "name": db_course.name,
        "code": db_course.code,
        "credits": db_course.credits,
        "department_id": db_course.department_id
    }



@app.patch(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if course.name is not None:
        db_course.name = course.name

    if course.code is not None:
        db_course.code = course.code

    if course.credits is not None:
        db_course.credits = course.credits

    if course.department_id is not None:
        db_course.department_id = course.department_id

    await db.commit()
    await db.refresh(db_course)

    return db_course


# DELETE
@app.delete(
    "/api/courses/{course_id}", tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()

    return 

@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Courses"]
)
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    # Check if the course exists
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    # Join Student and Enrollment
    result = await db.execute(
        select(Student)
        .join(Enrollment, Student.id == Enrollment.student_id)
        .where(Enrollment.course_id == course_id)
    )

    students = result.scalars().all()

    return [
        {
            "id": s.id,
            "first_name": s.first_name,
            "last_name": s.last_name,
            "email": s.email
        }
        for s in students
    ]

# -----------------------------
# STUDENT CRUD
# -----------------------------

@app.post(
    "/api/students/",
    tags=["Students"],
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_student(response:Response,
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):
    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email
    )

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    
    response.headers["Location"] = f"/api/students/{new_student.id}"

    return new_student


@app.get(
    "/api/students/",
    tags=["Students"],
    response_model=List[StudentResponse]
)
async def get_students(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Student))
    return result.scalars().all()


@app.get(
    "/api/students/{student_id}",
    tags=["Students"],
    response_model=StudentResponse
)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.put(
    "/api/students/{student_id}",
    tags=["Students"],
    response_model=StudentResponse
)
async def update_student(
    student_id: int,
    student: StudentCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    db_student = result.scalar_one_or_none()

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db_student.first_name = student.first_name
    db_student.last_name = student.last_name
    db_student.email = student.email

    await db.commit()
    await db.refresh(db_student)

    return db_student


@app.delete(
    "/api/students/{student_id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await db.delete(student)
    await db.commit()

    return

@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    # Check student
    student_result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )
    student = student_result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Check course
    course_result = await db.execute(
        select(Course).where(Course.id == enrollment.course_id)
    )
    course = course_result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        grade=enrollment.grade
    )

    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    response.headers["Location"] = f"/api/enrollments/{new_enrollment.id}"
    
    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment

@app.get(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=List[EnrollmentResponse]
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Enrollment))
    return result.scalars().all()

@app.get(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    response_model=EnrollmentResponse
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment

@app.delete(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)
    await db.commit()

    return

