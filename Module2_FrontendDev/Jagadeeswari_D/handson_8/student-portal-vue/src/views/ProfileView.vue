<template>
  <div>

    <h1>Profile</h1>

    <h3>Enrolled Courses</h3>

    <ul>
      <li
        v-for="course in store.enrolledCourses"
        :key="course.id"
      >
        {{ course.name }}
      </li>
    </ul>

    <h3>
      Total Credits:
      {{ store.totalCredits }}
    </h3>

  </div>
</template>

<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>