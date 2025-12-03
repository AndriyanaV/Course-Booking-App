<template>
	<nav :class="[
		'w-full lg:h-[90px] h-auto flex flex-col lg:flex-row justify-center fixed z-40 top-0 transition-all duration-300 text-white p-[20px]',
		isScrolled ? 'backdrop-blur-md bg-white/30 shadow-md text-black' : 'bg-transparent',
		navStyle
	]">
		<div class="container max-w-[1320px] mx-auto h-full flex flex-col-reverse lg:flex-row sm:items-center sm:justify-between  sm:px-[40px] 
">
			<div :class="[
				'h-full lg:flex items-center lg:flex-row flex-col lg:bg-none mt-[20px] lg:mt-[0px]',
				mobileControl ? 'flex' : 'hidden'
			]">
				<div>
					<RouterLink :class="[
						'font-poppins block no-underline py-2 px-3 rounded hover:scale-105 hover:bg-transparent  transition-colors duration-300',
						linkColor
					]" active-class=" font-bold" to="/">Homepage</RouterLink>
				</div>
				<div v-if="userStore.userRole === 'admin'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						linkColor
					]" to="/all-courses" active-class="text-blue-600 font-bold">Courses</RouterLink>
				</div>
				<div v-if="userStore.userRole === 'admin'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						linkColor
					]" to="/all-users" active-class="text-blue-600 font-bold">Users</RouterLink>
				</div>
				<div v-if="userStore.userRole === 'user'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						linkColor
					]" to="/user-courses" active-class="text-blue-600 font-bold">My Courses</RouterLink>
				</div>
				<div v-if="userStore.userRole === 'professor'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						linkColor
					]" to="/professor-courses" active-class="text-blue-600 font-bold">My Courses</RouterLink>
				</div>
			</div>

			<div class="flex h-full items-center gap-[15px] lg:w-fit w-full lg:justify-start justify-end">
				<button v-if="!userStore.isLoggedIn" @click="$router.push({ name: 'Login' })"
					class="bg-main-blue  text-white font-semibold py-2 px-4 rounded-[16px] border-0 h-[47px] w-[130px] hover:scale-105">
					Sign In
				</button>
				<button v-if="userStore.isLoggedIn" @click="userStore.toggleLogoutPopUp"
					class="bg-main-blue  text-white sm:font-semibold font-normal py-2 px-4 rounded-[16px] border-0 sm:h-[47px] sm:w-[130px] h-[44px] w-fit hover:scale-105">
					Sign Out
				</button>
				<div v-if="userStore.isLoggedIn">
					<div @click="$router.push({ name: 'UserProfile' })"
						class="sm:w-[43px] sm:h-[43px] w-[24px] h-[24px] cursor-pointer  hover:scale-105 bg-transparent flex items-center">
						<img :src=profileImg class="w-[90%] h-[90%]  object-cover transition-all" />
					</div>
				</div>
				<div class="w-[24px] h-[24px] lg:hidden" @click="handleMobileMenu"><img :src='mobileMenuImg'
						class=" object-contain"></div>
			</div>
		</div>
	</nav>
</template>

<script setup>
import { RouterLink, useRouter, useRoute } from "vue-router";
import { ref, onMounted,  computed, onUnmounted} from "vue";
import { useUserStore } from "@/stores/user";
import { useLogout } from "@/composables/useLogout";


//Data from user store 
const userStore = useUserStore();
const { logout } = useLogout();

//Mobile vs Destop control
const isScrolled = ref(false)
const mobileControl = ref(true)
const mobileMenuImg = ref('/images/menu.svg')

//To controll visibility of navbar links by using viewport 
const checkScreen = () => {
	mobileControl.value = window.innerWidth >= 1024
}

//Show or hide mobile menu
const handleMobileMenu = () => {

	mobileControl.value = !mobileControl.value
	mobileMenuImg.value = '/images/menu.svg'

	if (mobileControl.value) {
		isScrolled.value = true
		mobileMenuImg.value = '/images/x.svg'
	}

}

const router = useRouter();
const route = useRoute()

//To handle good desing - Need to Fix due to change of design
const blackNavTextPages = ['/', '/professor-courses', '/user-courses', '/course-info', '/add-course', '/add-current-course', '/update-course', '/course-card-info/:id', '/update-current-course', '/add-user', '/user-profile-update', '/user-profile', '/all-courses', '/all-users']


//Text color in navbar 
const linkColor = computed(() => {
	if (
		isScrolled.value ||
		blackNavTextPages.includes(route.path) ||
		route.path.startsWith('/course-card-info')||
		route.path.startsWith('/all-current-courses')  
	) {
		return 'text-black'
	}

	// Default
	return 'text-white'
})

//Hanlde icon image - Navbar
const profileImg = computed(() => {

	if (
		isScrolled.value ||
		blackNavTextPages.includes(route.path) ||
		route.path.startsWith('/course-card-info')||
		route.path.startsWith('/all-current-courses')
	) {
		return '/images/social-scrolled.png'
	}

	// Default
	return '/images/social.png'
})

//Handle style for navbar 
const navStyle = computed(() => {
	if (
		blackNavTextPages.includes(route.path) ||
		route.path.startsWith('/course-card-info')
	) {
		return 'border-b border-gray-300 shadow-sm shadow-gray-400/40'
	}

})



const handleScroll = () => {

	//To set blur when we scroll on top of the page
	if (window.innerWidth < 1024 && mobileControl.value) {
		isScrolled.value = true
		return
	}

	isScrolled.value = window.scrollY > 10;
};

onMounted(() => {
	checkScreen()
	window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
	window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped></style>