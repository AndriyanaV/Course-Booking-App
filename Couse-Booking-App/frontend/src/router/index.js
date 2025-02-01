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
import UserCourses from '@/views/UserCourses.vue'
import UserInfo from '@/views/UserInfo.vue'
import ProfessorCourses from '@/views/ProfessorCourses.vue'
import UserProfile from '@/views/UserProfile.vue'
import UserProfileUpdate from '@/views/UserProfileUpdate.vue'
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
      name: "Login",
      component: Login,
    },
    {
      path: "/all-courses",
      name: "AllCourses",
      component: AllCourses,
      meta: { requiresRole: ["admin"] },
    },
    {
      path: "/all-current-courses/:id",
      name: "AllCurrentCourses",
      component: AllCurrentCourses,
      props: true,
      meta: { requiresRole: ["admin"] },
    },
    {
      path: "/all-users",
      name: "AllUsers",
      component: AllUsers,
      meta: { requiresRole: ["admin"] },
     
    },
    {
      path: "/add-course",
      name: "AddCourse",
      component: AddCourse,
      meta: { requiresRole: ["admin"] },
     
    },
    {
      path: "/update-course",
      name: "UpdateCourse",
      component: UpdateCourse,
      props: true,
      meta: { requiresRole: ["admin"] },
     
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
      meta: { requiresRole: ["admin"] },
      
      
     
    },
    {
      path: "/update-current-course",
      name: "UpdateCurrentCourse",
      component: UpdateCurrentCourse,
      meta: { requiresRole: ["admin"] },
      
      
     
    },
    {
      path: "/user-info",
      name: "UserInfo",
      component: UserInfo,
      meta: { requiresRole: ["admin"] },
    },
    {
      path: "/add-user",
      name: "AddUser",
      component: AddUser,
      meta: { requiresRole: ["admin"] },
    },
    {
      path: "/update-user",
      name: "UpdateUser",
      component: UpdateUser,
      meta: { requiresRole: ["admin"] },
    },
    {
      path: "/user-courses",
      name: "UserCourses",
      component: UserCourses,
      meta: { requiresRole: ["user"] },
    },
    {
      path: "/professor-courses",
      name: "ProfessorCourses",
      component: ProfessorCourses,
      meta: { requiresRole: ["professor"] },
    },
    {
      path: "/user-profile",
      name: "UserProfile",
      component: UserProfile,
    },
    {
      path: "/user-profile-update",
      name: "UserProfileUpdate",
      component: UserProfileUpdate,
    }





  ]
    
  
})


router.beforeEach((to, from, next) => {
  const role = localStorage.getItem("rola");

  if (role) {
    if (to.meta.requiresRole && !to.meta.requiresRole.includes(role)) {
      return next("/studenti");
    }
  } else if (to.meta.requiresRole) {
    return next("/login");
  }

  next();
});

export default router;
