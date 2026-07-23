# SDLC vs TDLC – V-Model & Agile QA Integration

## Task 1 – V-Model Mapping

### 9. V-Model Diagram

```text
                     SDLC (Development)

Requirements Specification      <----------------->     Acceptance Testing

        ↓

System Design                   <----------------->     System Testing

        ↓

Architecture Design             <----------------->     Integration Testing

        ↓

Module Design                   <----------------->     Unit Testing

        ↓

                     Coding
```

### 10. SDLC Phase to TDLC Phase Mapping

| SDLC Phase | Corresponding TDLC Phase | Test Artifact Produced |
|------------|--------------------------|------------------------|
| Requirements | Acceptance Testing | Acceptance Test Plan |
| System Design | System Testing | System Test Cases |
| Architecture Design | Integration Testing | Integration Test Plan |
| Module Design | Unit Testing | Unit Test Cases |
| Coding | Test Execution | Source Code and Executable Build |

### Explanation

- **Requirements → Acceptance Testing:** QA prepares acceptance test scenarios based on business requirements.
- **System Design → System Testing:** QA creates system test cases to verify complete system functionality.
- **Architecture Design → Integration Testing:** QA prepares integration test plans to validate communication between modules.
- **Module Design → Unit Testing:** Developers write unit test cases for individual modules.
- **Coding:** Developers implement the code, after which testing begins.

---

### 11. Entry Criteria and Exit Criteria

#### Unit Testing

**Entry Criteria**
- Module coding completed
- Unit test cases prepared

**Exit Criteria**
- All unit tests executed
- No Critical or High severity defects remain

---

#### Integration Testing

**Entry Criteria**
- Unit testing completed successfully
- Modules integrated

**Exit Criteria**
- Module interactions verified
- No major integration defects remain

---

#### System Testing

**Entry Criteria**
- Complete application deployed
- Test environment available

**Exit Criteria**
- All functional requirements verified
- Critical and High severity defects fixed

---

#### Acceptance Testing

**Entry Criteria**
- System testing completed
- Customer or college admin available for testing

**Exit Criteria**
- Customer approves the application
- Product is ready for deployment

---

### 12. Early QA Involvement in the V-Model

QA should participate before testing begins at these two stages:

#### 1. Requirements Review

- Review business requirements.
- Identify ambiguous or missing requirements.
- Ensure every requirement can be tested.

#### 2. System Design Review

- Review the application design.
- Suggest improvements for easier testing.
- Identify possible risks before development starts.



## Task 2 – Agile QA and Shift-Left Testing

### 13. Problems with Waterfall Testing

In the Waterfall model, testing starts only after development is completed. This creates several problems:

1. **Late defect detection** – Bugs are discovered at the end of the project, making them more expensive to fix.

2. **Delayed feedback** – Developers receive feedback only after completing the entire application.

3. **Project delays** – Fixing major defects late in the project may delay the release schedule.

---

### 14. QA Role in Agile Ceremonies

| Agile Ceremony | QA Responsibilities |
|----------------|---------------------|
| Sprint Planning | Review user stories, define acceptance criteria, estimate testing effort. |
| Daily Stand-up | Share testing progress, report blockers, discuss defects with developers. |
| Sprint Review | Validate completed features and demonstrate testing results. |
| Retrospective | Discuss testing challenges and suggest process improvements for future sprints. |

---

### 15. Shift-Left Testing Practices

Shift-Left Testing means performing testing activities as early as possible during software development.

#### a) Requirement Review
QA reviews requirements to ensure they are complete, clear, and testable before development begins.

#### b) Writing Test Cases Early (TDD/BDD)
QA prepares test cases before coding starts so developers understand expected behavior.

#### c) Static Code Analysis
Developers use static analysis tools to identify coding issues before running the application.

#### d) API Contract Testing
API request and response formats are verified before integrating different modules, reducing integration defects.

---

### 16. Acceptance Criteria (Given–When–Then)

#### Scenario 1 – Successful Course Creation

**Given** the college admin is logged into the Course Management System

**When** the admin enters valid course details and submits the form

**Then** the course should be created successfully and a confirmation message should be displayed.

---

#### Scenario 2 – Duplicate Course Code

**Given** a course with the same course code already exists

**When** the admin submits another course using that course code

**Then** the system should display an error message indicating that the course code already exists.

---

#### Scenario 3 – Missing Required Fields

**Given** the admin opens the Create Course page

**When** one or more mandatory fields are left empty and the form is submitted

**Then** the system should display validation messages and should not create the course.