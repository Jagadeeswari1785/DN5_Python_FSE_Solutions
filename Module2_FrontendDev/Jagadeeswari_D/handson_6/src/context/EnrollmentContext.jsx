import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  function enroll(course) {
    setEnrolledCourses((prev) => [...prev, course]);
  }

  function remove(courseId) {
    setEnrolledCourses((prev) =>
      prev.filter((course) => course.id !== courseId)
    );
  }

  return (
    <EnrollmentContext.Provider
      value={{
        enrolledCourses,
        enroll,
        remove,
      }}
    >
      {children}
    </EnrollmentContext.Provider>
  );
}