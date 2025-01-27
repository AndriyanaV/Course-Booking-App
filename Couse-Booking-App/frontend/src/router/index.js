import { createRouter, createWebHistory } from 'vue-router'
import Homepage from '@/views/Homepage.vue';
import CourseInfo from '@/views/CourseInfo.vue';
import AllCourses from '@/views/AllCourses.vue';
import AllCurrentCourses from '@/views/AllCurrentCourses.vue';
import AllUsers from '@/views/AllUsers.vue';
import AddCourse from '@/views/AddCourse.vue';
import UpdateCourse from '@/views/UpdateCourse.vue';
import CourseCardInfo from '@/views/CourseCardInfo.vue';
import AddCurrentCourse from '@/views/AddCurrentCourse.vue'
import UpdateCurrentCourse from '@/views/UpdateCurrentCourse.vue'
import UpdateUser from '@/views/UpdateUser.vue'
import AddUser from '@/views/AddUser.vue'
import UserInfo from '@/views/UserInfo.vue'
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
    {
      path: "/all-users",
      name: "AllUsers",
      component: AllUsers
     
    },
    {
      path: "/add-course",
      name: "AddCourse",
      component: AddCourse
     
    },
    {
      path: "/update-course",
      name: "UpdateCourse",
      component: UpdateCourse,
      props: true,
     
    },
    {
      path: "/course-card-info/:id",
      name: "CourseCardInfo",
      component: CourseCardInfo,
      props: true,
     
    },
    {
      path: "/add-current-course",
      name: "AddCurrentCourse",
      component: AddCurrentCourse,
      
      
     
    },
    {
      path: "/update-current-course",
      name: "UpdateCurrentCourse",
      component: UpdateCurrentCourse,
      
      
     
    },
    {
      path: "/user-info",
      name: "UserInfo",
      component: UserInfo,
    },
    {
      path: "/add-user",
      name: "AddUser",
      component: AddUser,
    },
    {
      path: "/update-user",
      name: "UpdateUser",
      component: UpdateUser,
    }



  ]
    
  
})

export default router;
