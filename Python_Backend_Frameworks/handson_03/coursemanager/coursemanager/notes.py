"""
Hands-on 1 Notes

1. Request-Response Cycle
Browser
   ↓
URL Router
   ↓
View
   ↓
Model (Database)
   ↓
Response
   ↓
Browser

2. Middleware
Middleware sits between the request and the view.
Examples:
- SecurityMiddleware: Provides security features.
- AuthenticationMiddleware: Identifies the logged-in user.

3. WSGI vs ASGI
WSGI:
- Used for synchronous applications.
- Django uses WSGI by default.

ASGI:
- Supports asynchronous applications.
- Used for WebSockets, chat apps, and real-time applications.

4. MVC vs MVT

MVC
Model      → Django Model
View       → Django Template
Controller → Django View

Django follows the MVT (Model-View-Template) architecture.
"""