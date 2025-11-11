<template>
	<section class="w-full flex flex-col items-center">
		<section
			class="container max-w-[1320px] mx-auto w-full py-12 pr-0 flex justify-center pt-[150px] px-[40px] bg-second-blue">
			<div class="w-1/2 flex items-center text-center">
				<Heading heading="Manage All Users" color="white" />
			</div>
			<div class="w-1/2 h-auto flex items-center justify-center">
				<img src="/images/manage-users.png" class="w-[430px] h-[400px]" />
			</div>
		</section>
		<section class="w-full flex justify-center">
			<div class="container w-[1320px] mx-0 py-12 px-[40px] flex justify-end">
			<Button
				text="Add User"
				@buttonClicked="$router.push({ name: 'AddUser' })"
			
			/>
			</div>
		</section>
		<section class="w-full  flex justify-center">
			<div class="container max-w-[1320px]  flex flex-wrap gap-[20px] items-center px-[40px]">
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