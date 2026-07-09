import { courses } from "./data.js";

/* ES6 FEATURES */

courses.forEach(course => {
    const { name, credits } = course;

    console.log(`${name} - ${credits} credits`);
});

const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log(formattedCourses);

const filteredCourses =
    courses.filter(course => course.credits >= 4);

console.log(
    "Courses with credits >= 4:",
    filteredCourses.length
);

const totalCredits =
    courses.reduce(
        (sum, course) => sum + course.credits,
        0
    );

console.log("Total Credits:", totalCredits);

/* DOM ELEMENTS */

const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsElement =
    document.getElementById("total-credits");

const selectedCourse =
    document.getElementById("selected-course");

const loadingMessage =
    document.getElementById("loading-message");

const notificationList =
    document.getElementById("notification-list");

const notificationLoading =
    document.getElementById("notification-loading");

const notificationError =
    document.getElementById("notification-error");

const retryBtn =
    document.getElementById("retry-btn");

let currentCourses = [...courses];

/* RENDER FUNCTION */

function renderCourses(courseList){

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const card =
            document.createElement("article");

        card.className = "course-card";

        card.dataset.id = course.id;

        // Accessibility
        card.tabIndex = 0;

        card.addEventListener("keydown", (event) => {

            if (event.key === "Enter") {

                card.dispatchEvent(
                    new MouseEvent("click", { bubbles: true })
                );

            }

        });

        card.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <p>Credits: ${course.credits}</p>
            <p>Grade: ${course.grade}</p>
        `;

        courseGrid.appendChild(card);
    });

    const total =
        courseList.reduce(
            (sum, course) => sum + course.credits,
            0
        );

    totalCreditsElement.textContent =
        `Total Credits: ${total}`;

    // Accessibility: announce number of search results
    document.getElementById("results-count").textContent =
        `${courseList.length} courses found`;
}

/* INITIAL RENDER */

//renderCourses(currentCourses);
function fetchAllCourses() {

    return new Promise(resolve => {

        setTimeout(() => {

            resolve(courses);

        }, 1000);

    });

}

loadingMessage.style.display = "block";

fetchAllCourses().then(courseData => {

    currentCourses = [...courseData];

    renderCourses(currentCourses);

    loadingMessage.style.display = "none";

});

/* SEARCH */

document
.getElementById("search-courses")
.addEventListener("input", event => {

    const keyword =
        event.target.value.toLowerCase();

    currentCourses = courses.filter(course =>
        course.name
            .toLowerCase()
            .includes(keyword)
    );

    renderCourses(currentCourses);
});

/* SORT */

document
.getElementById("sort-btn")
.addEventListener("click", () => {

    currentCourses.sort(
        (a,b) => b.credits - a.credits
    );

    renderCourses(currentCourses);
});

/* EVENT DELEGATION */

courseGrid.addEventListener("click", event => {

    const card =
        event.target.closest(".course-card");

    if(!card) return;

    const id =
        Number(card.dataset.id);

    const course =
        courses.find(course => course.id === id);

    selectedCourse.textContent =
        `Selected Course: ${course.name} | Grade: ${course.grade}`;
});

function fetchUser(id) {

    return fetch(
        `https://jsonplaceholder.typicode.com/users/${id}`
    )

    .then(response => response.json())

    .then(user => {

        console.log("User Name:", user.name);

    });

}
fetchUser(1);

async function fetchUserAsync(id) {

    try {

        const response = await fetch(
            `https://jsonplaceholder.typicode.com/users/${id}`
        );

        const user = await response.json();

        console.log("Async User Name:", user.name);

    } catch (error) {

        console.error("Error fetching user:", error);

    }

}
fetchUserAsync(2);

async function fetchMultipleUsers() {

    try {

        const [user1, user2] = await Promise.all([

            fetch("https://jsonplaceholder.typicode.com/users/1")
                .then(response => response.json()),

            fetch("https://jsonplaceholder.typicode.com/users/2")
                .then(response => response.json())

        ]);

        console.log("User 1:", user1.name);
        console.log("User 2:", user2.name);

    }

    catch(error){

        console.error(error);

    }

}
fetchMultipleUsers();


async function apiFetch(url) {

    const response = await axios.get(url);

    return response.data;

}

axios.interceptors.request.use(config => {

    console.log(`API call started: ${config.url}`);

    return config;

});

apiFetch("https://jsonplaceholder.typicode.com/posts")

.then(posts => {

    console.log("Posts Loaded:", posts.length);

})

.catch(error => {

    console.error(error.message);

});

async function loadNotifications(
    url = "https://jsonplaceholder.typicode.com/posts"
) {

    try {

        notificationError.textContent = "";

        retryBtn.style.display = "none";
        notificationLoading.style.display = "block";

        notificationList.innerHTML = "";

const response = await axios.get(
    "https://jsonplaceholder.typicode.com/posts",
    {
        params: {
            userId: 1
        }
    }
);

const posts = response.data;
        notificationLoading.style.display = "none";

        posts.slice(0,5).forEach(post => {

            const card = document.createElement("div");

            card.className = "notification-card";

            card.innerHTML = `
                <h3>${post.title}</h3>
                <p>${post.body}</p>
            `;

            notificationList.appendChild(card);

        });

    }

    catch(error){

    notificationLoading.style.display = "none";

    notificationError.textContent =
        "Unable to load notifications. Please try again.";

    retryBtn.style.display = "block";

}

}
loadNotifications();

retryBtn.addEventListener("click", () => {

    loadNotifications();

});