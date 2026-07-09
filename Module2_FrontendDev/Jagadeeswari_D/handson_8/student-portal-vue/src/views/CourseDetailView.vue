<template>

<div>

<h1>Course Details</h1>

<div v-if="course">

<h2>{{course.name}}</h2>

<p>
Code: {{course.code}}
</p>

<p>
Credits: {{course.credits}}
</p>

<p>
Grade: {{course.grade}}
</p>


<button @click="enroll">
Enroll
</button>


</div>


<div v-else>

<h3>Course not found</h3>

</div>


</div>

</template>


<script setup>

import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";


const route = useRoute();

const router = useRouter();


const courses = [

{
id:1,
name:"Data Structures",
code:"CS101",
credits:4,
grade:"A"
},

{
id:2,
name:"Database Management",
code:"CS102",
credits:3,
grade:"B"
}

]


const course = ref(
 courses.find(
 c => c.id == route.params.id
 )
)



function enroll(){

 router.push('/profile')

}


</script>