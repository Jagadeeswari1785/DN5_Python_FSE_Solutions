# Test Automation Process, Lifecycle & Framework Types

## Task 1 – Automation Decision and Test Case Selection

### 17. Criteria for Automating Test Cases

A test case should be automated based on the following criteria:

| Criteria | Explanation | Application to POST /api/courses/ |
|----------|-------------|-----------------------------------|
| Repetitive Execution | Tests executed frequently should be automated. | This API is tested repeatedly after every code change, making it suitable for automation. |
| Stable Functionality | Features that rarely change are good automation candidates. | The POST endpoint is a stable core API feature. |
| High Business Impact | Critical business functions should be automated. | Creating a course is an important business operation. |
| Data-Driven Testing | Tests requiring multiple input values benefit from automation. | Different course names, codes, and credits can be tested automatically. |
| Regression Testing | Regression tests should always be automated. | The endpoint should be verified after every release to ensure no new defects are introduced. |

---

### 18. Automate or Manual Decision

| Test Case | Decision | Justification |
|-----------|----------|---------------|
| Regression test for all CRUD endpoints | **Automate** | Frequently executed after every code change. |
| Exploratory testing of a new search feature | **Manual** | Requires human observation and creativity. |
| Performance test with 100 concurrent users | **Automate** | Performance testing requires automation tools. |
| UI test for login form | **Automate** | Repeated in regression testing. |
| Verify Swagger documentation | **Manual** | Usually reviewed manually for accuracy and readability. |
| Smoke test after deployment | **Automate** | Ensures deployment success quickly after every release. |

---

### 19. Test Automation ROI

#### Definition

**Test Automation ROI (Return on Investment)** measures whether the time and cost spent creating automated tests are recovered through reduced manual testing effort.

#### Calculation

- Automation development time = **4 hours**
- Manual execution time = **30 minutes (0.5 hour)**

Break-even calculation:

4 ÷ 0.5 = **8 runs**

After the 10th run:

- Maintenance overhead = **20%**
- 20% of 30 minutes = **6 minutes**

Automation continues to save time even after maintenance because automated execution is much faster than manual testing.

**Result:** Automation pays for itself after approximately **8 executions**.

---

### 20. Flaky Test

#### Definition

A flaky test is a test that sometimes passes and sometimes fails even though the application has not changed.

#### Example

A Selenium test attempts to click a button before it becomes clickable, causing random failures depending on page loading speed.

#### Ways to Prevent Flaky Tests

1. Use Explicit Waits instead of fixed delays (`time.sleep()`).
2. Use stable locators such as ID or Name.
3. Reset test data and ensure each test starts with a clean environment.


---

# Task 2 – Compare Automation Framework Types

## 21. Comparison of Automation Framework Types

### 1. Linear Framework

**Description:**
The Linear Framework is the simplest automation framework where test scripts are written in sequence without separating data or reusable components.

**Advantage:**
Easy to create and understand.

**Disadvantage:**
Difficult to maintain as the project grows.

**Example:**
Suitable for automating a simple login page of the Course Management System.

---

### 2. Modular Framework

**Description:**
The application is divided into independent modules, and each module has its own test script.

**Advantage:**
Reusable code and easier maintenance.

**Disadvantage:**
Requires more planning than a Linear Framework.

**Example:**
Separate modules for Login, Courses, Students, and Enrollments.

---

### 3. Data-Driven Framework

**Description:**
Test data is stored outside the scripts (Excel, CSV, JSON, etc.), allowing the same test to run with multiple inputs.

**Advantage:**
Supports testing with many different datasets.

**Disadvantage:**
Requires additional code to read external data.

**Example:**
Testing course creation with multiple course names and codes.

---

### 4. Keyword-Driven Framework

**Description:**
Test actions are represented by keywords such as Login, Click, Enter Text, and Submit.

**Advantage:**
Non-technical users can create test cases.

**Disadvantage:**
Framework implementation is more complex.

**Example:**
Business analysts create test cases using predefined keywords.

---

### 5. Hybrid Framework

**Description:**
The Hybrid Framework combines Linear, Modular, Data-Driven, and Keyword-Driven approaches to improve flexibility and maintainability.

**Advantage:**
Highly reusable, scalable, and suitable for large projects.

**Disadvantage:**
Takes more time to design and maintain initially.

**Example:**
Complete automation of the Course Management System using Page Object Model, reusable utilities, and external test data.

---

## 22. Recommended Framework

For the Course Management frontend, I recommend a **Hybrid Framework**.

### Justification

- Login can be tested with **50 different user credentials** using the Data-Driven approach.
- Login functionality can be reused across **20 test cases** using the Modular/Page Object Model approach.
- Keyword-driven features allow **non-technical team members** to create or understand test cases.
- The Hybrid Framework is scalable, reusable, and easy to maintain, making it suitable for real-world automation projects.

---

## 23. Hybrid Framework Folder Structure

```text
CourseManagementAutomation/
│
├── config/
│   └── config.py
│
├── test_data/
│   └── login_data.xlsx
│
├── pages/
│   ├── login_page.py
│   ├── course_page.py
│   ├── student_page.py
│   └── base_page.py
│
├── utilities/
│   ├── driver_factory.py
│   ├── logger.py
│   └── helpers.py
│
├── tests/
│   ├── test_login.py
│   ├── test_courses.py
│   └── test_students.py
│
├── reports/
│
└── requirements.txt
```

### Explanation

- **config/** – Stores project configuration files.
- **test_data/** – Contains Excel, CSV, or JSON files used for Data-Driven testing.
- **pages/** – Contains Page Object Model classes.
- **utilities/** – Contains reusable helper functions, driver setup, and logging.
- **tests/** – Contains all Selenium test cases.
- **reports/** – Stores HTML test reports and screenshots.
- **requirements.txt** – Lists all required Python packages.

---

## Conclusion

The Hybrid Framework is the most suitable choice because it combines the advantages of Modular, Data-Driven, and Keyword-Driven frameworks. It improves code reusability, simplifies maintenance, supports multiple datasets, and is ideal for large Selenium automation projects.