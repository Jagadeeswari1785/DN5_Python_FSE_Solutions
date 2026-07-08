# Handson-6: JWT Authentication using Django REST Framework

## Objective

The objective of this hands-on is to secure REST APIs using JSON Web Token (JWT) authentication with Django REST Framework Simple JWT.

---

## Technologies Used

- Python 3.13.7
- Django 6.0.6
- Django REST Framework
- Simple JWT
- SQLite
- Swagger UI

---

## Step 1: Install Simple JWT

**Command**

```bash
pip install djangorestframework-simplejwt
```

**Output**

```text
Successfully installed djangorestframework-simplejwt
```

---

## Step 2: Configure Django Settings

Add the following to `settings.py`:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

---

## Step 3: Configure JWT URLs

Add the following URLs in `backend/urls.py`:

```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```

---

## Step 4: Protect APIs

Secure the API by adding the following permission class:

```python
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]
```

Example:

```python
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
```

---

## Step 5: Generate JWT Token

**Request**

```
POST /api/token/
```

Sample Request

```json
{
    "username": "admin",
    "password": "admin123"
}
```

Sample Response

```json
{
    "refresh": "eyJhbGc...",
    "access": "eyJhbGc..."
}
```

---

## Step 6: Access Protected APIs

Add the Access Token in the Authorization header.

```
Authorization: Bearer <access_token>
```

Example

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

## Step 7: Test Protected API

**Request**

```
GET /api/courses/
```

**Response**

```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Python",
            "code": "19CS31",
            "credits": 3,
            "department": 2
        }
    ]
}
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/token/ | Generate Access and Refresh Token |
| POST | /api/token/refresh/ | Refresh Access Token |
| GET | /api/courses/ | Access Protected API |

---

## Learning Outcome

- Installed Django REST Framework Simple JWT.
- Configured JWT authentication.
- Generated Access and Refresh Tokens.
- Secured REST APIs using `IsAuthenticated`.
- Successfully accessed protected APIs using Bearer Token.
