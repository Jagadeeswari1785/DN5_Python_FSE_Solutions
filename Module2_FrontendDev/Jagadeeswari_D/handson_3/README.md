# Handson_03
## HTML
```<!DOCTYPE html>
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

        <section class="stats">
    <div class="stat-item">
        <h3>3</h3>
        <p>Courses Enrolled</p>
    </div>

    <div class="stat-item">
        <h3>3.8</h3>
        <p>GPA</p>
    </div>

    <div class="stat-item">
        <h3>6</h3>
        <p>Semester</p>
    </div>
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
## CSS
```
/* RESET */
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    font-family:Arial,sans-serif;
    background:#f4f6f9;
    color:#333;
}

/* HEADER */

header{
    background:#1f4e79;
    color:white;
    padding:15px 25px;

    display:flex;
    flex-direction:column;
    align-items:center;
    gap:15px;
}

header h2{
    font-size:clamp(1.5rem,3vw,2.5rem);
}

nav ul{
    list-style:none;

    display:flex;
    flex-direction:column;
    gap:10px;
}

nav a{
    color:white;
    text-decoration:none;
}

/* HERO */

#hero{
    min-height:40vh;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    text-align:center;
    padding:40px 20px;
    background:#e8f1fb;
}

#hero p{
    margin:15px 0;
}

#hero button{
    padding:12px 24px;
    border:2px solid #1f4e79;
    background:white;
    cursor:pointer;
}

#hero button:hover{
    background:#1f4e79;
    color:white;
}

/* STATS */

.stats{
    display:flex;
    flex-direction:column;
    gap:20px;

    padding:30px;
    background:white;
}

.stat-item{
    text-align:center;
}

/* COURSES */

#courses{
    padding:40px 20px;
}

#courses h2{
    text-align:center;
    margin-bottom:25px;
}

.course-grid{
    display:grid;
    grid-template-columns:1fr;
    gap:20px;
}

.course-card{
    background:white;
    padding:20px;
    border-radius:10px;
    border:1px solid #ddd;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);

    min-height:220px;
    align-self:stretch;
}

.course-card h3{
    margin-bottom:10px;
}

.course-card p{
    margin-bottom:15px;
}

/* FOOTER */

footer{
    text-align:center;
    background:#1f4e79;
    color:white;
    padding:20px;
}

/* TABLET */

@media (min-width:768px){

    header{
        flex-direction:row;
        justify-content:space-between;
    }

    nav ul{
        flex-direction:row;
        gap:25px;
    }

    .stats{
        flex-direction:row;
        justify-content:space-around;
    }

    .course-grid{
        grid-template-columns:repeat(2,1fr);
    }
}

/* DESKTOP */

@media (min-width:1024px){

    #hero{
        padding:80px 20px;
    }

    .course-grid{
        grid-template-columns:repeat(3,1fr);
    }
}
```
