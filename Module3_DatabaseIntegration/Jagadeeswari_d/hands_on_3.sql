select first_name,
       last_name
from students
where department_id = (
    select department_id
    from departments
    where dept_name = 'computer science'
);

select first_name,
       last_name
from students
where department_id = (
    select department_id
    from departments
    where dept_name = 'computer science'
);

select *
from professors
where salary = (
    select max(salary)
    from professors
);

select *
from courses
where credits >
(
    select avg(credits)
    from courses
);

select first_name,
       last_name
from students
where student_id in
(
    select student_id
    from enrollments
    where grade = 'a'
);

create view student_department_view as
select s.student_id,
       s.first_name,
       s.last_name,
       d.dept_name
from students s
join departments d
on s.department_id = d.department_id;

select *
from student_department_view;

create view professor_department_view as
select p.prof_name,
       d.dept_name,
       p.salary
from professors p
join departments d
on p.department_id = d.department_id;

select *
from professor_department_view;

drop view student_department_view;

drop view professor_department_view;

create or replace function get_total_students()
returns integer
language sql
as $$
    select count(*) from students;
$$;

select get_total_students();

create or replace function get_average_salary()
returns numeric
language sql
as $$
    select avg(salary) from professors;
$$;

select get_average_salary();
begin;

update professors
set salary = 100000
where professor_id = 1;

select * from professors;
rollback;
begin;

update professors
set salary = 98000
where professor_id = 1;

commit;
begin;

update professors
set salary = 99000
where professor_id = 2;

savepoint sp1;

update professors
set salary = 105000
where professor_id = 3;

rollback to sp1;

commit;

