import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '@/views/Homepage.vue';
import CourseInfo from '@/views/CourseInfo.vue';
import AllCourses from '@/views/AllCourses.vue';
import AllCurrentCourses from '@/views/AllCurrentCourses.vue';
import Login from '@/views/Login.vue';




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Homepage",
      component: Homepage,
    },
    {
      path: "/course-info",
      name: "CourseInfo",
      component: CourseInfo,
    },
    {
      path: "/login",
      name: "LogIn",
      component: Login,
    },
    {
      path: "/all-courses",
      name: "AllCourses",
      component: AllCourses,
    },
    {
      path: "/all-current-courses/:id",
      name: "AllCurrentCourses",
      component: AllCurrentCourses,
      props: true,
    },

  ]
    
  
})

export default router;
