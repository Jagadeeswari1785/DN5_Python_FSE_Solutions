import { useParams } from "react-router-dom";

function CourseDetailPage() {
  const { courseId } = useParams();

  return (
    <div>
      <h2>Course Details</h2>
      <p>Course ID: {courseId}</p>
    </div>
  );
}

export default CourseDetailPage;