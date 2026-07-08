# Hands-On 3 - Django REST Views, URL Routing & Forms

## Python Backend Frameworks – Digital Nurture 5.0

### Objective

This hands-on demonstrates how to build RESTful APIs using Django REST Framework (DRF). It includes creating serializers, API views, URL routing, ViewSets, routers, and custom actions for the Course Management API.

---

## Topics Covered

- Django REST Framework (DRF)
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- APIView
- ModelSerializer
- URL Routing
- ViewSets
- Routers
- CRUD Operations
- Custom Actions
- JSON Request & Response

---

## Features Implemented

- Course CRUD API
- Student CRUD API
- Enrollment CRUD API
- DRF Serializers
- APIView-based endpoints
- ModelViewSet implementation
- Automatic URL routing using DefaultRouter
- Custom endpoint to list students enrolled in a course
- JSON responses with proper HTTP status codes

---

## Project Structure

```
hands_on_3/
│
├── README.md
├── task1.md
├── task2.md
└── coursemanager/
    ├── manage.py
    ├── coursemanager/
    └── courses/
        ├── models.py
        ├── serializers.py
        ├── views.py
        ├── urls.py
        └── admin.py
```

---

## Installation

Install the required packages:

```bash
pip install django
pip install djangorestframework
```

---

## Run the Project

```bash
python manage.py runserver
```

---

## API Endpoints

### Courses

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/courses/ | List all courses |
| POST | /api/courses/ | Create a course |
| GET | /api/courses/{id}/ | Get course by ID |
| PUT | /api/courses/{id}/ | Update course |
| DELETE | /api/courses/{id}/ | Delete course |

### Students

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/students/ | List students |
| POST | /api/students/ | Create student |

### Enrollments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/enrollments/ | Enroll a student |

---

## Technologies Used

- Python 3.x
- Django
- Django REST Framework (DRF)
- SQLite

---

## Learning Outcomes

After completing this hands-on, I learned:

- How to build REST APIs using Django REST Framework
- How to create serializers for models
- How to use APIView and ModelViewSet
- How to configure routers and URL patterns
- How to perform CRUD operations using REST APIs
- How to test APIs using Postman or DRF Browsable API

---

## Author

**Name:** Jagadeeswari

**Program:** Digital Nurture 5.0 – Python Full Stack Engineer Track
