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
nav {
  display: flex;
  gap: 15px;
  margin: 15px 0;
}
</style>