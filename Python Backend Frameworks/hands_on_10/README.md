# Hands-On 10 – Microservices Architecture (Flask)

## Objective

The objective of this hands-on is to understand Microservices Architecture by decomposing a monolithic Course Management API into multiple independent services. The implementation demonstrates service decomposition, API Gateway, and inter-service communication.

---

## Technologies Used

- Python 3.x
- Flask
- SQLAlchemy
- SQLite / PostgreSQL
- Requests Library
- REST APIs

---

## Packages Installed

```bash
pip install flask
pip install sqlalchemy
pip install requests
```

---

## Project Structure

```
handson_10/
│
├── course_service/
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   └── course.db
│
├── student_service/
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   └── student.db
│
├── gateway/
│   ├── app.py
│
├── requirements.txt
└── README.md
```

---

## Service Decomposition

| Service | Responsibility | Endpoints |
|----------|----------------|----------|
| Course Service | Manage courses and departments | `/api/courses/*` |
| Student Service | Manage students and enrollments | `/api/students/*` |
| API Gateway | Routes client requests | `/api/*` |

Each service owns its own database and runs independently.

---

## Microservices Implemented

### Course Service

Runs on

```
http://localhost:5001
```

Responsibilities

- Create Course
- Update Course
- Delete Course
- View Courses

---

### Student Service

Runs on

```
http://localhost:5002
```

Responsibilities

- Student CRUD
- Enrollment
- Calls Course Service to verify course availability

---

### API Gateway

Runs on

```
http://localhost:5000
```

Responsibilities

- Receives client requests
- Routes requests to appropriate service
- Acts as a single entry point

---

## Inter-Service Communication

Student Service communicates with Course Service using the Python Requests library.

Example Flow

```
Client
   │
   ▼
API Gateway
   │
   ▼
Student Service
   │
   ▼
Course Service
```

Before enrolling a student, the Student Service verifies whether the course exists by making an HTTP request to the Course Service.

---

## Error Handling

If Course Service is unavailable

```
503 Service Unavailable
```

is returned with an appropriate error message.

---

## API Endpoints

### Course Service

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/courses | List Courses |
| POST | /api/courses | Create Course |
| GET | /api/courses/{id} | Get Course |
| PUT | /api/courses/{id} | Update Course |
| DELETE | /api/courses/{id} | Delete Course |

---

### Student Service

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /api/students | List Students |
| POST | /api/students | Create Student |
| POST | /api/students/{id}/enroll | Enroll Student |

---

### API Gateway

Routes

```
/api/courses/*
```

to Course Service

and

```
/api/students/*
```

to Student Service.

---

## Expected Output

- Course Service runs independently.
- Student Service runs independently.
- API Gateway routes requests correctly.
- Student Service communicates with Course Service.
- Enrollment succeeds when Course Service is available.
- Returns HTTP 503 if Course Service is unavailable.

---

## Advantages of Microservices

- Independent deployment
- Better scalability
- Separate databases
- Easier maintenance
- Fault isolation
- Technology independence

---

## Synchronous vs Asynchronous Communication

### Synchronous Communication

- Uses HTTP requests.
- Immediate response.
- Services are tightly coupled.
- Failure of one service affects another.

### Asynchronous Communication

- Uses Message Queues (RabbitMQ/Kafka).
- Services communicate through events.
- Better fault tolerance.
- Improved scalability.
- Eventual consistency.

---

## Learning Outcome

After completing this hands-on, I learned to:

- Understand Microservices Architecture.
- Decompose a monolithic application into services.
- Build independent Flask services.
- Implement API Gateway routing.
- Perform inter-service communication using HTTP.
- Handle service failures gracefully.
- Understand synchronous vs asynchronous communication.
