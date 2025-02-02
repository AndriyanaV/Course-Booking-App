<template>
	<section class="w-full flex flex-col items-center">
		<section class="w-full py-12 pr-0 flex justify-center pt-[140px]">
			<Heading heading="All Users" color="#4E32BA" />
		</section>
		<section class="w-[1320px] py-12 pr-0 flex justify-end">
			<Button
				text="Add User"
				@buttonClicked="$router.push({ name: 'AddUser' })"
			/>
		</section>
		<section class="w-full py-12 pr-0 flex justify-center">
			<div class="w-[1320px] flex flex-wrap gap-[30px] items-center">
				<div v-for="user in allUsers" :key="user.id">
					<UserCard :user="user" @userDeleted="deleteUser" />
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
	import Button from "@/components/Button.vue";

	let allUsers = ref([]);

	const getAllUsers = async () => {
		try {
			const response = await axios.get("/api/admin/get-users");
			allUsers.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	const deleteUser = async (deletedUser) => {
		if (confirm("Are you sure?")) {
			try {
				const response = await axios.delete(
					`api/admin/delete-user/${deletedUser.id}`
				);
				allUsers.value = allUsers.value.filter(
					(user) => user.id != deletedUser.id
				);
				toast.success(response.data.message);
			} catch (error) {
				toast.error(error.message);
			}
		}
	};

	onMounted(() => {
		getAllUsers();
	});
</script>

<style>
</style>