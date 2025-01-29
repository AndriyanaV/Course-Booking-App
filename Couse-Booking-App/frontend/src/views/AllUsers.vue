<template>
	<section class="w-full flex flex-col items-center">
		<section class="w-full py-12 pr-0 flex justify-center pt-[140px]">
			<Heading heading="All Users" color="#4E32BA" />
		</section>
		<section class="w-[1320px] py-12 pr-0 flex justify-end">
			<div class="h-[60px] w-[200px]">
				<button
					class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full w-[200px]"
					@click="$router.push({ name: 'AddUser' })"
				>
					Add User
				</button>
			</div>
		</section>
		<section class="w-full py-12 pr-0 flex justify-center">
			<div class="w-[1320px] flex flex-wrap justify-between items-center">
				<div v-for="user in allUsers" :key="user.id">
					<UserCard :user="user" @userDeleted="filterUsers" />
				</div>
			</div>
		</section>
	</section>
</template>

<script setup>
	import axios from "axios";
	import { ref, onMounted } from "vue";
	import { toast } from "vue3-toastify";
	import Heading from "@/components/Heading.vue";
	import UserCard from "@/components/UserCard.vue";

	const token = localStorage.getItem("access_token");
	let allUsers = ref([]);

	const getAllUsers = async () => {
		try {
			const response = await axios.get("/api/admin/get-users");
			allUsers.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	const filterUsers = (deltedUser) => {
		allUsers.value = allUsers.value.filter((user) => user.id != deltedUser.id);
	};

	onMounted(() => {
		getAllUsers();
	});
</script>

<style>
</style>