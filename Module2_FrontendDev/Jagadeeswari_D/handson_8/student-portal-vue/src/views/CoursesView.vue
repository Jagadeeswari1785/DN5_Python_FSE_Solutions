<template>
  <div>
    <h1>Courses</h1>

    <div class="search">
      <input
        v-model="searchTerm"
        placeholder="Search courses..."
      />
    </div>

    <div
      v-for="course in filteredCourses"
      :key="course.id"
    >
      <CourseCard
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
      />

      <button @click="store.enroll(course)">
        Enroll
      </button>

      <br><br>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import CourseCard from "../components/CourseCard.vue";
import { useEnrollmentStore } from "../stores/enrollment";

const store = useEnrollmentStore();

const searchTerm = ref("");

const courses = ref([
  {
    id: 1,
    name: "Data Structures",
    code: "CS101",
    credits: 4,
    grade: "A"
  },
  {
    id: 2,
    name: "Database Management",
    code: "CS102",
    credits: 3,
    grade: "B"
  },
  {
    id: 3,
    name: "Web Development",
    code: "CS103",
    credits: 4,
    grade: "A"
  },
  {
    id: 4,
    name: "Computer Networks",
    code: "CS104",
    credits: 3,
    grade: "B"
  },
  {
    id: 5,
    name: "Operating Systems",
    code: "CS105",
    credits: 4,
    grade: "A"
  }
]);

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())
  );
});
</script>

<style scoped>
.search {
  margin-bottom: 20px;
}

input {
  padding: 10px;
  width: 300px;
}

button {
  margin-left: 10px;
  padding: 6px 12px;
}
</style>