<template>
	<main class="w-full flex flex-col items-center">
		<section class="w-full lg:flex flex-col items-center lg:px-[40px] px-[20px]">
			<div
				class="container max-w-[1320px] mx-auto flex lg:flex-row flex-col bg-soft-blue h-auto mt-[100px]  rounded-[10px] gap-[20px]">
				<div
					class="sm:w-[50%] w-full flex justify-center flex-col items-start lg:gap-[30px] gap-[20px] sm:pl-[50px] pl-[20px] sm:pr-[0px] pr-[20px] pt-[50px] pb-[50px]">

					<div class="flex flex-col lg:gap-[20px] gap-[14px]">
						<Heading heading="Manage Users" color="#363232" class="w-full font-bold" fontSize="64" />
						<p class="text-[#4F4A4A] lg:w-[75%] w-[80%]">Manage all users: create, update, delete, and
							adjust user information.</p>
					</div>

				</div>
				<div class="lg:w-[50%] flex justify-center flex-col h-full items-center">
					<img src="/images/user-hero-img.png" class="max-w-[100%] h-max-[80%] object-contain " />
				</div>

			</div>
		</section>
		<section class="w-full  flex justify-center lg:px-[40px] px-[20px] lg:py-[80px] py-[40px]">
			<div class="container max-w-[1320px] mx-auto h-fit flex lg:flex-row flex-col lg:justify-between gap-[20px] lg:items-center">
				<Button text="Add User" @buttonClicked="$router.push({ name: 'AddUser' })"/>
			</div>
		</section>
		<section class="w-full flex justify-center lg:px-[40px] px-[20px] ">
			<div class="container max-w-[1320px] mx-auto h-fit flex lg:flex-row flex-col lg:justify-between gap-[20px] flex-wrap lg:items-center">
				<UserCard v-for="user in allUsers" :key="user.id" :user="user" @userDeleted="deleteUser" />	
			</div>
		</section>
	</main>
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

<style></style>