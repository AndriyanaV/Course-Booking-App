<template>
	<nav :class="[
		'w-full h-[90px] flex justify-center fixed z-40 top-0 transition-all duration-300 text-white ',
		isScrolled ? 'backdrop-blur-md bg-white/30 shadow-md text-black' : 'bg-transparent'
	]">
		<div class="container max-w-[1320px] mx-auto h-full flex items-center justify-between  px-[40px] 
">
			<div class="h-full flex items-center">
				<div>
					<RouterLink :class="[
						'font-poppins block no-underline py-2 px-3 rounded hover:scale-105 hover:bg-transparent  transition-colors duration-300',
						isScrolled ? 'text-black' : 'text-white'
					]" active-class=" font-bold" to="/">Homepage</RouterLink>
				</div>
				<div v-if="userRole === 'admin'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						isScrolled ? 'text-black' : 'text-white'
					]" to="/all-courses" active-class="text-blue-600 font-bold">Courses</RouterLink>
				</div>
				<div v-if="userRole === 'admin'">
					<RouterLink :class="[
						'block no-underline py-2 px-3 rounded hover:bg-gray-100  transition-colors duration-300 hover:scale-105 hover:bg-transparent ',
						isScrolled ? 'text-black' : 'text-white'
					]" to="/all-users" active-class="text-blue-600 font-bold">Users</RouterLink>
				</div>
				<div v-if="userRole === 'user'">
					<RouterLink
						class="block no-underline py-2 px-3 text-white rounded hover:bg-gray-100 hover:scale-105 hover:bg-transparent "
						to="/user-courses" active-class="text-blue-600 font-bold">My Courses</RouterLink>
				</div>
				<div v-if="userRole === 'professor'">
					<RouterLink
						class="block no-underline py-2 px-3 text-white rounded hover:bg-gray-100 hover:scale-105 hover:bg-transparent "
						to="/professor-courses" active-class="text-blue-600 font-bold">My Courses</RouterLink>
				</div>
			</div>

			<div class="flex h-full items-center gap-[15px]">
				<button v-if="!isLoggedIn" @click="$router.push({ name: 'Login' })"
					class="bg-main-blue  text-white font-semibold py-2 px-4 rounded-[16px] border-0 h-[47px] w-[130px] hover:scale-105">
					Sign In
				</button>
				<button v-if="isLoggedIn" @click="handleLogOut"
					class="bg-main-blue  text-white font-semibold py-2 px-4 rounded-[16px] border-0 h-[47px] w-[130px] hover:scale-105">
					Sign Out
				</button>
				<div v-if="isLoggedIn">
					<div @click="$router.push({ name: 'UserProfile' })"
						class="w-[43px] h-[43px]  cursor-pointer  hover:scale-105 bg-transparent flex items-center">
						<img :src="isScrolled ? '/images/social-scrolled.png' : '/images/social.png'"
							class="w-[90%] h-[90%]  object-cover transition-all" />
					</div>
				</div>
			</div>
		</div>
	</nav>
</template>

<script setup>
import { useUserRole } from "@/composables/useUserRole.js";
import { RouterLink, useRouter } from "vue-router";
import { toast } from "vue3-toastify";
import { ref, onMounted, watchEffect, watch, onUnmounted } from "vue";

const isLoggedIn = ref(false);
const isScrolled = ref(false)

const router = useRouter();
const { userRole, checkUserRole } = useUserRole();
console.log(userRole.value);

const handleLogOut = () => {
	if (confirm("Are you sure?")) {
		try {
			localStorage.removeItem("access_token");
			localStorage.removeItem("user_id");
			localStorage.removeItem("rola");
			localStorage.removeItem("token_expiration");

			isLoggedIn.value = false;

			checkUserRole();

			router
				.push("/")
				.then(() => toast.success("You have successfully logged out!"));
		} catch (error) {
			toast.error(error.message);
		}
	}
};

const handleScroll = () => {
	isScrolled.value = window.scrollY > 10;
};

onMounted(() => {
	checkUserRole();
	isLoggedIn.value = !!localStorage.getItem("access_token");
	window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
	window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped></style>