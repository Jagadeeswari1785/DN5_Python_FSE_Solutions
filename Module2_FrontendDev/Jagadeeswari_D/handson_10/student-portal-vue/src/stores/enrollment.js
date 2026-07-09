import { defineStore } from "pinia";
import { ref, computed } from "vue";

import { getCourseById } from "../api/courseApi";

export const useEnrollmentStore = defineStore("enrollment", () => {

  const enrolledCourses = ref([]);

  const totalCredits = computed(() => {

    return enrolledCourses.value.reduce(
      (sum, course) => sum + course.credits,
      0
    );

  });

  function enroll(course) {

    if (!enrolledCourses.value.find(c => c.id === course.id)) {

      enrolledCourses.value.push(course);

    }

  }

  function unenroll(courseId) {

    enrolledCourses.value =
      enrolledCourses.value.filter(
        course => course.id !== courseId
      );

  }

  // Step 149
  async function fetchAndEnroll(courseId) {

    try {

      const course = await getCourseById(courseId);

      enroll({
        id: course.id,
        name: course.title,
        code: `CS${course.id}`,
        credits: 4,
        grade: "A"
      });

    }

    catch(error){

      console.error(error);

    }

  }

  function resetEnrollment(){

    enrolledCourses.value = [];

  }

  return {

    enrolledCourses,
    totalCredits,
    enroll,
    unenroll,
    fetchAndEnroll,
    resetEnrollment

  };

});