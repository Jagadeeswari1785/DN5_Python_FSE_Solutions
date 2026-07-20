from pydantic import BaseModel
from typing import Optional


class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseCreate):
    id: int

    class Config:
        from_attributes = True

class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: list[CourseResponse]

class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    email: str


class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    grade: str


class EnrollmentResponse(EnrollmentCreate):
    id: int

    class Config:
        from_attributes = True