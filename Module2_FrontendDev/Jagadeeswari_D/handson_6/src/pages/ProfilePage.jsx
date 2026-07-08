import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <>
      <h2>Student Profile</h2>

      <h3>Enrolled Courses</h3>

      {enrolledCourses.length === 0 ? (
        <p>No enrolled courses.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div key={course.id}>
            <p>
              {course.name} ({course.code})
            </p>

            <button onClick={() => dispatch(unenroll(course.id))}>
              Remove
            </button>

            <hr />
          </div>
        ))
      )}
    </>
  );
}

export default ProfilePage;