# Hands-On 10: Microservices Architecture

## Objective

This hands-on demonstrates how to decompose a monolithic Course Management API into independent microservices, implement inter-service communication, and create a simple API Gateway.

---

## Service Decomposition

| Service Name | Responsibility | Endpoints | Database |
|--------------|---------------|-----------|----------|
| Course Service | Manage course information | /api/courses | courses.db |
| Student Service | Manage students and enrollments | /api/students, /api/students/<id>/enroll | students.db |
| Auth Service | User registration and login | /api/v1/auth/register, /api/v1/auth/login | users.db |
| Notification Service | Sends confirmation emails (concept) | Background task | notification.db (concept) |

---

## Architecture

Client
↓
API Gateway (Port 5000)
├── Course Service (Port 5001)
└── Student Service (Port 5002)

The API Gateway receives client requests and forwards them to the appropriate microservice.

---

## Inter-Service Communication

The Student Service communicates with the Course Service using the Python `requests` library.

Flow:

1. Client sends an enrollment request.
2. API Gateway forwards the request to Student Service.
3. Student Service calls Course Service to verify that the course exists.
4. If the course exists, enrollment is completed.
5. If Course Service is unavailable, Student Service returns **503 Service Unavailable**.

---

## Synchronous vs Asynchronous Communication

### Synchronous (HTTP)

**Advantages**
- Simple to implement
- Immediate response
- Easy to understand

**Disadvantages**
- Services are tightly coupled
- Failure of one service affects another
- Increased response time

---

### Asynchronous (Message Queue)

**Advantages**
- Loose coupling
- Better scalability
- Improved reliability
- Services work independently

**Disadvantages**
- More complex implementation
- Eventual consistency

Examples:
- RabbitMQ
- Apache Kafka

---

## API Gateway Pattern

The API Gateway acts as a single entry point for all client requests.

Responsibilities:
- Routes requests to the correct service.
- Hides internal service URLs.
- Simplifies client communication.
- Can provide authentication, logging, and rate limiting.

---

## Project Structure

```
handson_10/
│
├── course_service/
│   ├── app.py
│   └── courses.db
│
├── student_service/
│   ├── app.py
│   └── students.db
│
├── gateway/
│   └── app.py
│
└── README.md
```

---

## Technologies Used

- Python
- Flask
- SQLite
- Requests
- REST API

---

## Result

- Successfully decomposed the monolithic application into independent microservices.
- Implemented synchronous communication between services.
- Implemented an API Gateway for request routing.
- Handled service unavailability using HTTP 503 responses.