explain
select s.first_name,
       c.course_name
from students s
join enrollments e
on s.student_id = e.student_id
join courses c
on e.course_id = c.course_id;

create index idx_students_department
on students(department_id);

create index idx_courses_code
on courses(course_code);

create index idx_enrollments_student
on enrollments(student_id);

select indexname,
       tablename
from pg_indexes
where schemaname = 'public';

explain
select s.first_name,
       c.course_name
from students s
join enrollments e
on s.student_id = e.student_id
join courses c
on e.course_id = c.course_id;
