# Hands-On 1 – QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

### 1. Test Cases for Different Testing Levels

#### Unit Testing
**Objective:** Verify the `create_course()` function creates a course object correctly.

**Test Case:**
- Input:
  - Course Code: CS101
  - Course Name: Data Structures
  - Credits: 4
- Expected Result:
  - The function returns a valid Course object with the provided details.

**Testing Type:** Functional Testing

---

#### Integration Testing

**Objective:** Verify that the POST `/api/courses/` endpoint correctly stores data in the database.

**Test Case:**
- Send a POST request with valid course details.
- Verify the API returns **HTTP 201 Created**.
- Verify the course is stored in the database.

**Testing Type:** Functional Testing

---

#### System Testing

**Objective:** Test the complete course creation process.

**Test Case:**
1. User sends a POST request.
2. API validates the request.
3. Data is stored in the database.
4. API returns the created course.

**Expected Result:**
The entire workflow completes successfully.

**Testing Type:** Functional Testing

---

#### User Acceptance Testing (UAT)

**Objective:** Verify the feature from a college administrator's perspective.

**Test Case:**
- Login as College Admin.
- Create a new course.
- Search for the course.
- Verify it appears correctly.

**Expected Result:**
The administrator can successfully create and manage courses.

**Testing Type:** Functional Testing

---

### 2. Functional vs Non-Functional Testing

| Test | Type |
|------|------|
| Unit Testing | Functional |
| Integration Testing | Functional |
| System Testing | Functional |
| User Acceptance Testing | Functional |

### Non-Functional Test Example

**Performance Testing**

Objective:
Measure how the Course Management API performs under heavy load.

Example:
- Simulate 1000 users sending requests simultaneously.
- Verify response time remains below 2 seconds.
- Ensure the server does not crash.

---

### 3. Black-Box Testing vs White-Box Testing

| Black-Box Testing | White-Box Testing |
|-------------------|-------------------|
| Internal code is not visible. | Internal code is known. |
| Focuses on inputs and outputs. | Focuses on program logic and code paths. |
| Performed mainly by QA Engineers. | Performed mainly by Developers. |
| Tests functionality. | Tests code coverage, conditions, loops, and branches. |

**QA Tester:** Black-Box Testing

**Developer:** White-Box Testing

---

### 4. Formal Test Cases for POST `/api/courses/`

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|--------------|-------------|---------------|------------|-----------------|---------------|-----------|
| TC001 | Create course with valid data | API running | Send POST request with valid details | HTTP 201 Created and course stored | | |
| TC002 | Missing mandatory course name | API running | Send POST request without course name | HTTP 400 Bad Request | | |
| TC003 | Duplicate course code | Existing course CS101 exists | Send POST request with same course code | Duplicate course error returned | | |

---

# Task 2 – Defect Lifecycle & Severity Classification

## 5. Defect Lifecycle

New
↓
Assigned
↓
Open
↓
Fixed
↓
Retest
↓
Verified
↓
Closed

### Alternate Paths

**Rejected**
- Bug is invalid.
- Cannot be reproduced.
- Works as designed.
- Duplicate defect.

**Deferred**
- Bug is accepted but postponed.
- Will be fixed in a future release due to time or business priorities.

---

## 6. Severity and Priority Classification

### a) POST `/api/courses/` returns HTTP 500 for all requests

**Severity:** Critical

**Priority:** P1

**Justification:**
The API is completely unusable, preventing all users from creating courses.

---

### b) Course names longer than 150 characters are silently truncated

**Severity:** Medium

**Priority:** P3

**Justification:**
The application still functions, but data integrity is affected.

---

### c) Swagger documentation contains a typo

**Severity:** Low

**Priority:** P4

**Justification:**
No impact on application functionality.

---

### d) Login occasionally returns HTTP 401 despite valid credentials

**Severity:** High

**Priority:** P1

**Justification:**
Intermittent authentication failures affect usability and indicate possible instability.

---

## 7. Defect Report

| Field | Details |
|------|---------|
| Defect ID | BUG-001 |
| Title | POST `/api/courses/` returns HTTP 500 Internal Server Error |
| Environment | Windows 11, Chrome 138, FastAPI, SQLite |
| Build Version | v1.0.0 |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Start API. 2. Send POST request with valid course data. |
| Expected Result | Course created successfully with HTTP 201. |
| Actual Result | API returns HTTP 500 Internal Server Error. |
| Attachments | Screenshot of HTTP 500 error. |

---

## 8. Difference Between Severity and Priority

### Severity

Severity measures how much the defect impacts the system.

Example:
A login failure that prevents all users from accessing the application is **Critical Severity**.

### Priority

Priority measures how urgently the defect should be fixed.

Example:
A spelling mistake on the CEO's dashboard has **Low Severity** because it does not affect functionality, but it may have **High Priority (P1)** because it is highly visible before an important client presentation.

### Example Where High Severity ≠ High Priority

A rarely used reporting feature crashes when exporting reports.

- Severity: High (feature crashes)
- Priority: Low (very few users use it and there is an alternative method)

The defect significantly affects one feature but does not require an immediate fix.