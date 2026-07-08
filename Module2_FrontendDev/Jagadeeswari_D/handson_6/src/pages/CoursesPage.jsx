import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";
import CourseCard from "../components/CourseCard";

function CoursesPage() {
  const [courses, setCourses] = useState([]);
  const navigate = useNavigate();
  const dispatch = useDispatch();

  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

        const data = await response.json();

        const firstFive = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3,
          grade: "A",
        }));

        setCourses(firstFive);
      } catch (error) {
        console.error(error);
      }
    }

    fetchCourses();
  }, []);

  function handleEnroll(course) {
    dispatch(enroll(course));
    navigate("/profile");
  }

  return (
    <>
      <h2>Courses</h2>

      {courses.map((course) => (
        <CourseCard
          key={course.id}
          id={course.id}
          name={course.name}
          code={course.code}
          credits={course.credits}
          grade={course.grade}
          onEnroll={handleEnroll}
        />
      ))}
    </>
  );
}

export default CoursesPage;