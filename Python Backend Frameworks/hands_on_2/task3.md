### HANDSON 2 TASK 2 
# Task 2: Django ORM Queries

"""
Hands-On 2 - Task 2
Django ORM Queries

Run these commands inside:
python manage.py shell

Then execute:
exec(open("handson2_task2.py").read())
"""

```
from courses.models import Department, Course, Student
from django.db.models import Count, F

# -----------------------------
# Create Departments
# -----------------------------
cs = Department.objects.create(
    name="Computer Science",
    head_of_dept="Dr. Kumar",
    budget=500000
)

it = Department.objects.create(
    name="Information Technology",
    head_of_dept="Dr. Priya",
    budget=400000
)

# -----------------------------
# Create Courses
# -----------------------------
Course.objects.create(
    name="Python Programming",
    code="CS101",
    credits=4,
    department=cs
)

Course.objects.create(
    name="Data Structures",
    code="CS102",
    credits=4,
    department=cs
)

Course.objects.create(
    name="Web Development",
    code="IT101",
    credits=3,
    department=it
)

Course.objects.create(
    name="Cloud Computing",
    code="IT102",
    credits=4,
    department=it
)

# -----------------------------
# Create Students
# -----------------------------
Student.objects.create(
    first_name="Rahul",
    last_name="Sharma",
    email="rahul@example.com",
    department=cs,
    enrollment_year=2024
)

Student.objects.create(
    first_name="Anjali",
    last_name="Singh",
    email="anjali@example.com",
    department=cs,
    enrollment_year=2024
)

Student.objects.create(
    first_name="Arun",
    last_name="Kumar",
    email="arun@example.com",
    department=it,
    enrollment_year=2023
)

Student.objects.create(
    first_name="Priya",
    last_name="Ravi",
    email="priya@example.com",
    department=it,
    enrollment_year=2024
)

Student.objects.create(
    first_name="Karthik",
    last_name="Raj",
    email="karthik@example.com",
    department=it,
    enrollment_year=2025
)

print("\nDepartments, Courses and Students created successfully.\n")

# -----------------------------
# Query Courses
# -----------------------------
print("Courses in Computer Science:")
courses = Course.objects.filter(department__name="Computer Science")

for course in courses:
    print(course.name)

# -----------------------------
# Count Courses per Department
# -----------------------------
print("\nCourse Count by Department:")

counts = Department.objects.annotate(
    course_count=Count("course")
)

for dept in counts:
    print(dept.name, "-", dept.course_count)

# -----------------------------
# select_related()
# -----------------------------
print("\nStudents with Departments:")

students = Student.objects.select_related("department")

for student in students:
    print(student.first_name, "-", student.department.name)

# -----------------------------
# Update Budget
# -----------------------------
Department.objects.update(
    budget=F("budget") * 1.10
)

print("\nDepartment budgets increased by 10%.")

print("\nHands-On 2 Task 2 Completed Successfully.")
```

# output :

Django ORM Queries executed successfully.
