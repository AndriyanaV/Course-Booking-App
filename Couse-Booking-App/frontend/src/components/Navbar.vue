<template>
	<nav
		class="w-full h-[90px] flex justify-center bg-[#f4f8ff] fixed z-40 top-0"
	>
		<div
			class="content w-[1320px] h-full flex items-center justify-between bg-[#f4f8ff]"
		>
			<div class="h-full flex items-center">
				<div>
					<RouterLink
						class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
						active-class="text-blue-600 font-bold"
						to="/"
						>Homepage</RouterLink
					>
				</div>
				<div v-if="userRole === 'admin'">
					<RouterLink
						class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
						to="all-courses"
						active-class="text-blue-600 font-bold"
						>All Courses</RouterLink
					>
				</div>
				<div v-if="userRole === 'admin'">
					<RouterLink
						class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
						to="all-users"
						active-class="text-blue-600 font-bold"
						>All Users</RouterLink
					>
				</div>
				<div v-if="userRole === 'user'">
					<RouterLink
						class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
						to="/user-courses"
						active-class="text-blue-600 font-bold"
						>My Courses</RouterLink
					>
				</div>
				<div v-if="userRole === 'professor'">
					<RouterLink
						class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
						to="/professor-courses"
						active-class="text-blue-600 font-bold"
						>My Courses</RouterLink
					>
				</div>
			</div>

			<div class="flex h-full items-center gap-[15px]">
				<button
					@click="$router.push({ name: 'Login' })"
					class="bg-[#090DE7] hover:bg-blue-800 text-white font-semibold py-2 px-4 border border-gray-400 rounded h-[47px] w-[130px]"
				>
					Sign In
				</button>
				<button
					class="bg-gray-100 hover:bg-gray-300 text-black font-semibold py-2 px-4 border border-gray-400 rounded h-[47px] w-[130px]"
				>
					Sign Out
				</button>
				<div>
					<div
						@click="$router.push({ name: 'UserProfile' })"
						class="w-[45px] h-[45px] rounded-full cursor-pointer"
					>
						<img
							src="/images/user.png"
							class="w-[98%] h-[98%] rounded-full border"
						/>
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
	import { onMounted } from "vue";

	const router = useRouter();
	const { userRole, checkUserRole } = useUserRole();
	console.log(userRole.value);

	onMounted(() => {
		checkUserRole();
	});
</script>

<style scoped>
</style>