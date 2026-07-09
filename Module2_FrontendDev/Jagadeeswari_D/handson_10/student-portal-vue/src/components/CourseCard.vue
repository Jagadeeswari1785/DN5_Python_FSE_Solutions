<template>
  <div class="course-card">
    <h2>{{ name }}</h2>
    <p><strong>Code:</strong> {{ code }}</p>
    <p><strong>Credits:</strong> {{ credits }}</p>
    <p><strong>Grade:</strong> {{ grade }}</p>
  </div>
</template>

<script setup>
defineProps({
  name: String,
  code: String,
  credits: Number,
  grade: String
});
</script>

<style scoped>
.course-card{

background:white;
padding:20px;

border-radius:10px;
border:1px solid #ddd;

box-shadow:0 2px 8px rgba(0,0,0,.1);

transition:.3s;

cursor:pointer;

}

.course-card:hover{

transform:translateY(-4px);

}

.course-card h3{

margin-bottom:10px;

}

.course-card p{

margin-bottom:8px;

}
</style>