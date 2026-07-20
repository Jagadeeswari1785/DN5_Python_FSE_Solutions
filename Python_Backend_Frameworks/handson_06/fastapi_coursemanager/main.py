import asyncio
from contextlib import asynccontextmanager

from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, create_tables
from models import Course
from schemas import CourseCreate

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Course Management API",
    version="1.0",
    lifespan=lifespan
)


@app.get("/")
async def home():
    return {"message": "API running"}


# CREATE
@app.post("/api/courses/")
async def create_course(
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

    return {
        "id": new_course.id,
        "name": new_course.name,
        "code": new_course.code,
        "credits": new_course.credits,
        "department_id": new_course.department_id
    }


# GET ONE
@app.get("/api/courses/{course_id}")
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
@app.get("/api/courses/")
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
@app.put("/api/courses/{course_id}")
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


# DELETE
@app.delete("/api/courses/{course_id}")
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

    return {"message": "Course deleted"}