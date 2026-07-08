Step 1: Install DRF
pip install djangorestframework
Open coursemanager/settings.py and add:

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Step 2: Create courses/serializers.py
Create a new file named serializers.py inside the courses app.

from rest_framework import serializers
from .models import Department, Course, Student, Enrollment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
Step 3: Update courses/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


class CourseListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)

        if not course:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)

        if not course:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        course = self.get_object(pk)

        if not course:
            return Response(status=status.HTTP_404_NOT_FOUND)

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
Step 4: Create courses/urls.py
from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
]
Step 5: Update coursemanager/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]
Step 6: Run the server
python manage.py runserver
Step 7: Test using Postman or Thunder Client
GET all courses

GET http://127.0.0.1:8000/api/courses/
POST a course

POST http://127.0.0.1:8000/api/courses/
JSON Body:

{
    "name": "Python Programming",
    "code": "CS101",
    "credits": 4,
    "department": 1
}
GET a course

GET http://127.0.0.1:8000/api/courses/1/
PUT (update)

PUT http://127.0.0.1:8000/api/courses/1/
DELETE

DELETE http://127.0.0.1:8000/api/courses/1/
