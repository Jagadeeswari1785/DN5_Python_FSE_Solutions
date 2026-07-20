from contextlib import asynccontextmanager
from datetime import timedelta
from typing import Optional, List

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    BackgroundTasks,
    Response
)

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from jose import JWTError, jwt

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, create_tables

from models import (
    Course,
    Student,
    Enrollment,
    User
)

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    StudentResponse,
    EnrollmentCreate,
    EnrollmentResponse,
    UserRegister,
    UserLogin,
    Token
)

from security import (
    get_password_hash,
    verify_password,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Course Management API",
    description="API for managing courses, students and enrollments.",
    version="1.0",
    lifespan=lifespan
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# -----------------------------
# CURRENT USER
# -----------------------------
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    result = await db.execute(
        select(User).where(User.email == email)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise credentials_exception

    return user


# -----------------------------
# HOME
# -----------------------------
@app.get("/", tags=["Home"])
async def home():
    return {
        "message": "Course Management API Running"
    }


# =====================================================
# AUTH
# =====================================================

# Register
@app.post(
    "/api/v1/auth/register",
    tags=["Authentication"],
    status_code=201
)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == user.email)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=1
    )

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "email": new_user.email
    }


# Login
@app.post(
    "/api/v1/auth/login",
    response_model=Token,
    tags=["Authentication"]
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =====================================================
# COURSE APIs
# =====================================================

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"]
)
async def create_course(
    response: Response,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    try:
        await db.commit()
        await db.refresh(new_course)
    except Exception:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail={
                "error": {
                    "code": "COURSE_EXISTS",
                    "message": "Course code already exists",
                    "field": "code"
                }
            }
        )

    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"

    return new_course


@app.get(
    "/api/v1/courses/",
    response_model=dict,
    tags=["Courses"]
)
async def get_courses(
    page: int = 1,
    page_size: int = 10,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if search:
        query = query.where(
            (Course.name.ilike(f"%{search}%")) |
            (Course.code.ilike(f"%{search}%"))
        )

    result = await db.execute(query)
    all_courses = result.scalars().all()

    total = len(all_courses)

    start = (page - 1) * page_size
    end = start + page_size

    courses = all_courses[start:end]

    next_page = (
        f"/api/v1/courses/?page={page+1}&page_size={page_size}"
        if end < total else None
    )

    previous_page = (
        f"/api/v1/courses/?page={page-1}&page_size={page_size}"
        if page > 1 else None
    )

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }


@app.get(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    return course


@app.put(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def update_course(
    course_id: int,
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    db_course.name = course.name
    db_course.code = course.code
    db_course.credits = course.credits
    db_course.department_id = course.department_id

    await db.commit()
    await db.refresh(db_course)

    return db_course


@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def patch_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    update_data = course.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_course, key, value)

    await db.commit()
    await db.refresh(db_course)

    return db_course


@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    await db.delete(course)
    await db.commit()

    return Response(status_code=204)


@app.get(
    "/api/v1/courses/{course_id}/students/",
    tags=["Courses"]
)
async def get_course_students(
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
            detail={
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Course with id {course_id} does not exist",
                    "field": None
                }
            }
        )

    result = await db.execute(
        select(Student)
        .join(
            Enrollment,
            Student.id == Enrollment.student_id
        )
        .where(
            Enrollment.course_id == course_id
        )
    )

    students = result.scalars().all()

    return students


# ==========================
# ENROLLMENT APIs
# ==========================

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


# ==========================
# USER REGISTRATION (JWT)
# ==========================

@app.post(
    "/api/v1/auth/register",
    status_code=status.HTTP_201_CREATED,
    tags=["Authentication"]
)
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    # Check if email already exists
    result = await db.execute(
        select(User).where(User.email == user.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    # bcrypt is intentionally slow, making brute-force attacks harder than MD5/SHA256.
    hashed_password = get_password_hash(user.password)

    new_user = User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=1
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "email": new_user.email
    }


from jose import jwt
from jose.exceptions import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# -----------------------------------------------------
# CORS Configuration
# -----------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------------------------
# Create JWT Token
# -----------------------------------------------------
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

# -----------------------------------------------------
# OAuth2 Note
# -----------------------------------------------------
"""
OAuth2 Authorization Code Flow:

The Authorization Code Flow redirects the user to an external
identity provider (Google, Microsoft, GitHub, etc.) for login.

After successful authentication, the provider returns an
authorization code.

The application exchanges this code for an access token.

In this project, we are using simple JWT authentication where
users log in directly with email and password.
"""