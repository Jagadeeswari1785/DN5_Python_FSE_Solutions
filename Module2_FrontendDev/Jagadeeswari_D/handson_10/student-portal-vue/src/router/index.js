import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import CoursesView from '../views/CoursesView.vue'
import CourseDetailView from '../views/CourseDetailView.vue'


const router = createRouter({

history:createWebHistory(),

routes:[

{
path:'/',
component:HomeView
},

{
path:'/courses',
component:CoursesView
},

{
path:'/courses/:id',
component:CourseDetailView
},

{
path:'/profile',
component:ProfileView
}

]

})


router.beforeEach((to) => {
  console.log("Navigating to:", to.path)
  return true
})


export default router