<template>
  <header>

    <h1>
      Student Portal ({{ store.enrolledCourses.length }})
    </h1>

    <nav>
      <RouterLink to="/">Home</RouterLink>

      |

      <RouterLink to="/courses">Courses</RouterLink>

      |

      <RouterLink to="/profile">Profile</RouterLink>
    </nav>

    <hr />

  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<style scoped>
header{
    background:#1f4e79;
    color:white;
    padding:20px;

    display:flex;
    flex-direction:column;
    align-items:center;
    gap:15px;
}

nav{
    display:flex;
    gap:25px;
    flex-wrap:wrap;
}

nav a{
    color:white;
    font-weight:bold;
}

nav a.router-link-active{
    text-decoration:underline;
}

hr{
    width:100%;
    margin-top:15px;
}

@media(min-width:768px){

header{
flex-direction:row;
justify-content:space-between;
}

}
</style>