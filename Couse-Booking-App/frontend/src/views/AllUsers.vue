<template>
	<section class="w-full py-12 pr-0 flex justify-center">
		<Heading heading="All Users" color="#4E32BA" />
	</section>
	<section class="w-full py-12 pr-0 flex justify-center">
		<div class="w-[1320px] flex flex-wrap justify-between items-center">
			<div v-for="user in allUsers" :key="user.id">
				<UserCard :user="user" />
			</div>
		</div>
	</section>
</template>

<script setup>
	import axios from "axios";
	import { ref } from "vue";
	import { toast } from "vue3-toastify";
	import Heading from "@/components/Heading.vue";
	import UserCard from "@/components/UserCard.vue";

	const token = localStorage.getItem("access_token");
	let allUsers = ref([]);

	const getAllUsers = async () => {
		try {
			const response = await axios.get(`/api/admin/get-users`, {
				headers: {
					Authorization: `Bearer ${token}`, // Dodajemo token u header
				},
			});
			allUsers.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	getAllUsers();
</script>

<style>
</style>