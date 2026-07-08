import { Link, useNavigate } from "react-router-dom";

function CourseCard(props) {
  const navigate = useNavigate();

  function handleEnroll() {
    props.onEnroll(props);
    navigate("/profile");
  }

  return (
    <div className="course-card">
      <Link to={`/courses/${props.id}`} style={{ textDecoration: "none", color: "black" }}>
        <h2>{props.name}</h2>
      </Link>

      <p>Code: {props.code}</p>
      <p>Credits: {props.credits}</p>
      <p>Grade: {props.grade}</p>

      <button onClick={handleEnroll}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;