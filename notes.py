# Task 1: Understand the Request-Response Cycle

# 1. Journey of GET /api/courses/ request through Django

# Browser sends GET /api/courses/
# ↓
# URL Router:
# Django checks urls.py and matches the request URL.

# ↓
# View:
# The mapped view function/class receives the request
# and processes business logic.

# ↓
# Model:
# The view interacts with the model.
# Model performs database query to retrieve course data.

# ↓
# Response:
# The view returns JSON or HTML response.
# Browser displays the result.



# 2. Middleware in Django

# Middleware sits between receiving the request
# and sending back the response.

# Example Middleware 1:
# SessionMiddleware
# Handles session management and stores user data.

# Example Middleware 2:
# AuthenticationMiddleware
# Identifies logged-in users and attaches user information
# to requests.



# 3. Difference between WSGI and ASGI

# WSGI (Web Server Gateway Interface):
# Supports synchronous request processing.
# Best for traditional web applications.

# ASGI (Asynchronous Server Gateway Interface):
# Supports asynchronous processing.
# Enables WebSockets, real-time updates,
# and handling many concurrent requests.

# Django uses WSGI by default.

# Switch to ASGI when:
# - Building chat applications
# - Using WebSockets
# - Creating real-time systems
# - Heavy async operations



# 4. MVC Pattern and Django MVT Mapping

# MVC:
# Model → Handles data
# View → Handles user interface
# Controller → Handles business logic

# Django uses MVT:

# Model → Model
# View → Controller
# Template → View

# In Django:
# Model manages database
# View contains application logic
# Template displays output to users