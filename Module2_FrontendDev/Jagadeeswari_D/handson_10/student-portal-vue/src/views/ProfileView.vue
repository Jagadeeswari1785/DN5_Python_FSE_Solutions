<template>
  <div class="page">

    <div class="profile">

      <h1>Student Profile</h1>

      <h2>Enrolled Courses</h2>

      <ul>
        <li
          v-for="course in enrolledCourses"
          :key="course.id"
        >
          {{ course.name }}
        </li>
      </ul>

      <h3>Total Credits: {{ totalCredits }}</h3>

      <button @click="store.resetEnrollment()">
        Clear Enrollments
      </button>

    </div>

  </div>
</template>


<script setup>
import { storeToRefs } from "pinia";
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();

const { enrolledCourses, totalCredits } =
storeToRefs(store);
</script>