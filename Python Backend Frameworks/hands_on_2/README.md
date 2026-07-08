# Hands-On 2 - Django Models, ORM & Admin Interface

## Python Backend Frameworks – Digital Nurture 5.0

### Objective

This hands-on focuses on creating database models using Django ORM, performing database migrations, executing CRUD operations through the Django shell, and managing data using the built-in Django Admin Interface.

---

## Topics Covered

- Django Models
- Model Fields and Constraints
- Foreign Keys and Relationships
- Migrations
- Django ORM
- CRUD Operations
- Django Admin Interface
- Model Registration
- Search and Filters

---

## Features Implemented

- Created Department model
- Created Course model
- Created Student model
- Created Enrollment model
- Added relationships using ForeignKey
- Implemented `__str__()` methods
- Applied database migrations
- Performed CRUD operations using Django ORM
- Registered all models in Django Admin
- Customized CourseAdmin with:
  - list_display
  - search_fields
  - list_filter
- Created Superuser for Admin access

---

## Project Structure

```
hands_on_2/
│
├── README.md
├── task1.md
├── task2.md
└── coursemanager/
    ├── manage.py
    ├── coursemanager/
    └── courses/
        ├── models.py
        ├── admin.py
        ├── views.py
        ├── urls.py
        └── migrations/
```

---

## Models

The following database models were implemented:

- Department
- Course
- Student
- Enrollment

Relationships between models were established using Django Foreign Keys.

---

## Technologies Used

- Python 3.x
- Django
- SQLite
- Django ORM

---

## Commands Used

### Create Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Show Applied Migrations

```bash
python manage.py showmigrations
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

### Open Django Shell

```bash
python manage.py shell
```

---

## ORM Operations Performed

- Created Department records
- Created Course records
- Created Student records
- Queried Courses by Department
- Counted Courses using annotate()
- Retrieved related data using select_related()
- Updated Department budgets using F() expressions

---

## Django Admin Features

- Registered all models
- Managed records using Django Admin
- Configured list_display
- Enabled search_fields
- Added list_filter
- Verified unique enrollment constraints

---

## Expected Output

- Database tables created successfully
- All migrations applied successfully
- Models displayed in Django Admin
- CRUD operations executed through Django ORM
- Search and filtering available in Admin
- Duplicate enrollments prevented using unique constraints

---

## Learning Outcomes

After completing this hands-on, I learned how to:

- Design relational database models in Django
- Use Django ORM for database operations
- Perform migrations safely
- Manage data using the Django Admin interface
- Configure model relationships and constraints
- Customize the Admin dashboard for better usability

---

## Author

**Name:** Jagadeeswari

**Program:** Digital Nurture 5.0 – Python Full Stack Engineer Track
