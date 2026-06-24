Exercise 1
HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Portal - Home</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <header>
        <h2>Student Portal</h2>

        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Courses</a></li>
                <li><a href="#">Profile</a></li>
                <li><a href="#">Grades</a></li>
            </ul>
        </nav>
    </header>

    <main>

        <section id="hero">
            <h1>Welcome to the Student Portal</h1>
            <p>
                Access your courses, track academic progress,
                and stay connected with your learning journey.
            </p>
            <button>Explore Courses</button>
        </section>

        <section id="courses">
            <h2>Available Courses</h2>

            <article class="course-card">
                <h3>Frontend Development</h3>
                <p>
                    Learn HTML5, CSS3, JavaScript, and responsive
                    web design fundamentals.
                </p>
                <span>Credits: 4</span>
            </article>

            <article class="course-card">
                <h3>Database Management Systems</h3>
                <p>
                    Understand relational databases, SQL queries,
                    normalization, and transactions.
                </p>
                <span>Credits: 3</span>
            </article>

            <article class="course-card">
                <h3>Computer Networks</h3>
                <p>
                    Explore networking concepts, protocols,
                    routing, and network security basics.
                </p>
                <span>Credits: 3</span>
            </article>

        </section>

    </main>

    <footer>
        <p>&copy; 2026 Student Portal. All Rights Reserved.</p>
    </footer>

</body>
</html>
```
<img width="1920" height="1080" alt="Screenshot (63)" src="https://github.com/user-attachments/assets/22862d69-d538-49e9-8469-74fa341ed5c7" />

CSS
```css
/* CSS Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f6f9;
    color: #333;
    line-height: 1.6;
}

/* Header */
header {
    background-color: #1f1f5d;
    color: white;
    padding: 20px 40px;

    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* Navigation */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline-block;
    margin-left: 20px;
}

nav ul li a {
    text-decoration: none;
    color: white;
    font-weight: bold;
}

nav ul li a:hover {
    text-decoration: underline;
}

/* Hero Section */
#hero {
    text-align: center;
    padding: 80px 20px;
    background-color: #e8f1fb;
}

#hero h1 {
    margin-bottom: 15px;
}

#hero p {
    margin-bottom: 20px;
}

#hero button {
    padding: 12px 24px;
    border: 2px solid #1f4e79;
    background-color: white;
    color: #1f4e79;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
}

#hero button:hover {
    background-color: #1f4e79;
    color: white;
}

/* Courses Section */
#courses {
    padding: 40px;
}

#courses h2 {
    margin-bottom: 20px;
    text-align: center;
}

/* Course Cards */
.course-card {
    background-color: whitesmoke;
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.course-card h3 {
    margin-bottom: 10px;
}

.course-card p {
    margin-bottom: 10px;
}

.course-card span {
    font-weight: bold;
    color: #1f4e79;
}

/* Footer */
footer {
    text-align: center;
    padding: 20px;
    background-color: #1f1f5d;
    color: white;
}
```
<img width="1920" height="1080" alt="Screenshot (64)" src="https://github.com/user-attachments/assets/3a9fb184-818a-472f-9046-824ef7f3a623" />

OUTPUT
<img width="1920" height="1080" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/6298745a-f568-49f2-a874-6ce69b882d7d" />


