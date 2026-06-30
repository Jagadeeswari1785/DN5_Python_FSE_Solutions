-- HANDS-ON 1: SQL Basics
-- hands-on 1

create table departments (
    department_id serial primary key,
    dept_name varchar(100) not null,
    hod_name varchar(100),
    budget decimal(12,2)
);

create table students (
    student_id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    date_of_birth date,
    department_id int,
    enrollment_year int,
    constraint fk_student_department
        foreign key (department_id)
        references departments(department_id)
);

create table courses (
    course_id serial primary key,
    course_name varchar(150) not null,
    course_code varchar(20) unique,
    credits int,
    department_id int,
    constraint fk_course_department
        foreign key (department_id)
        references departments(department_id)
);

create table enrollments (
    enrollment_id serial primary key,
    student_id int,
    course_id int,
    enrollment_date date,
    grade char(2),
    constraint fk_enrollment_student
        foreign key (student_id)
        references students(student_id),
    constraint fk_enrollment_course
        foreign key (course_id)
        references courses(course_id)
);

create table professors (
    professor_id serial primary key,
    prof_name varchar(100) not null,
    email varchar(100) unique,
    department_id int,
    salary decimal(10,2),
    constraint fk_professor_department
        foreign key (department_id)
        references departments(department_id)
);

-- normalization analysis

-- 1nf:
-- all columns contain atomic values.
-- there are no repeating groups.

-- 2nf:
-- every non-key attribute depends on the primary key.

-- 3nf:
-- no transitive dependencies.
-- department details are stored only in the departments table.
