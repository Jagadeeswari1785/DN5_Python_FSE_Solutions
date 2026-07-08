# Hands-On 9 – Authentication & Security (JWT, OAuth2 & OWASP)

## Objective

The objective of this hands-on is to implement secure authentication and authorization for the Course Management API using FastAPI. This exercise demonstrates password hashing, JWT token generation, and security best practices.

---

## Technologies Used

- Python 3.x
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- Uvicorn
- python-jose
- Passlib (bcrypt)
- python-multipart
- Pydantic

---

## Packages Installed

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install python-jose[cryptography]
pip install passlib[bcrypt]
pip install python-multipart
```

---

## Features Implemented

### Task 1 – User Registration

- Created User model
- Email validation
- Password hashing using bcrypt
- Duplicate email validation
- Secure password storage
- Registration endpoint

Endpoint:

```
POST /api/v1/auth/register
```

Sample Request

```json
{
    "email": "student@example.com",
    "password": "Password@123"
}
```

Sample Response

```json
{
    "message": "User registered successfully"
}
```

---

### Password Hashing

Implemented helper functions:

- get_password_hash()
- verify_password()

bcrypt is used because:

- Slow hashing algorithm
- Salted passwords
- Resistant to brute-force attacks
- More secure than MD5 or SHA-256

---

### Task 2 – JWT Login

Implemented login endpoint.

Endpoint

```
POST /api/v1/auth/login
```

Sample Request

```json
{
    "username": "student@example.com",
    "password": "Password@123"
}
```

Sample Response

```json
{
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer"
}
```

---

## JWT Authentication

Implemented

- JWT token generation
- Token expiration (30 minutes)
- Token verification
- Current user dependency
- Unauthorized access handling

Protected routes require a valid Bearer Token.

Example

```
Authorization:
Bearer <access_token>
```

---

## Protected Endpoints

Examples

```
POST /api/v1/courses/

DELETE /api/v1/courses/{id}
```

Unauthenticated requests return

```
401 Unauthorized
```

---

## CORS Configuration

Configured CORS middleware to allow requests from

```
http://localhost:3000
```

Example

```python
allow_origins=["http://localhost:3000"]
```

---

## OWASP Security Practices Followed

- Password hashing using bcrypt
- JWT authentication
- No plain-text password storage
- Token expiration
- Input validation using Pydantic
- Proper HTTP status codes
- Secure API authentication
- CORS protection

---

## OAuth2 Concept

OAuth2 Authorization Code Flow allows users to authenticate through an authorization server before receiving an access token.

In this project, a simpler JWT authentication approach is implemented where:

- User logs in with email and password
- Server validates credentials
- JWT token is generated
- Token is used for authenticated requests

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------------------------|-----------------------|
| POST | /api/v1/auth/register | Register new user |
| POST | /api/v1/auth/login | Login user |
| POST | /api/v1/courses/ | Protected Create Course |
| DELETE | /api/v1/courses/{id} | Protected Delete Course |

---

## Expected Output

- User registration successful
- Password stored as bcrypt hash
- JWT token generated successfully
- Protected routes accessible only with valid token
- Unauthorized requests return HTTP 401
- CORS configured successfully

---

## Project Structure

```
handson_09/
│
├── main.py
├── auth.py
├── security.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
└── README.md
```

---

## Learning Outcome

After completing this hands-on, I learned to:

- Implement JWT authentication
- Secure passwords using bcrypt
- Protect API endpoints
- Configure CORS
- Follow OWASP security best practices
- Build secure REST APIs using FastAPI
