import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  useEffect(() => {
    async function fetchCourses() {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

  useEffect(() => {
  console.log("Courses updated");

  // This effect runs only when the 'courses' state changes.
  // The dependency array [courses] prevents it from running after every render.
}, [courses]);

        const data = await response.json();

        const firstFiveCourses = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: "A",
        }));

        setCourses(firstFiveCourses);
        setLoading(false);
      } 
      catch (error) {
  console.error(error);
  setError("Failed to load courses.");
  setLoading(false);
}
    }

    fetchCourses();
  }, []);

  function handleEnroll(course) {
    setEnrolledCourses((prev) => [...prev, course]);
  }

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <input
        type="text"
        placeholder="Search courses..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
      />

    <StudentProfile />

      {loading ? (
  <h2>Loading...</h2>
) : error ? (
  <h2>{error}</h2>
) : (
  filteredCourses.map((course) => (
    <CourseCard
      key={course.id}
      name={course.name}
      code={course.code}
      credits={course.credits}
      grade={course.grade}
      onEnroll={handleEnroll}
    />
  ))
)}

      <Footer />
    </>
  );
}

export default App;