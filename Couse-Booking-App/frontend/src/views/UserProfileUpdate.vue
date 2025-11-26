<template>
	<section class="w-full flex justify-center items-start bg-gradient-to-b from-[#2d3cff]/20 to-white min-h-screen py-[150px]">
		<UserProfileUpdateForm :user="user" @userProfileUpdated="updateUserInfo" />
	</section>
</template>

<script setup>
	import UserProfileUpdateForm from "@/components/UserProfileUpdateForm.vue";
	import axios from "axios";
	import { ref, onMounted } from "vue";
	import { toast } from "vue3-toastify";
	import { useRoute, useRouter } from "vue-router";

	const route = useRoute();
	const router = useRouter();
	const userId = route.query.userId;

	console.log(userId);

	const user = ref(null);

	const getUserProfileInfo = async () => {
		try {
			const response = await axios.get("api/users/user-profile");
			console.log("API Response:", response);
			user.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	const updateUserInfo = async (form) => {
		const formData = new FormData();
		formData.append("first_name", form.firstName);
		formData.append("last_name", form.lastName);
		formData.append("email", form.email);
		formData.append("phone_number", form.pnumber);
		formData.append("file", form.image);

		try {
			const response = await axios.put(
				`api/admin/update-user/${userId}`,
				formData
			);
			router
				.push("/user-profile")
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.message);
		}
	};

	onMounted(() => {
		getUserProfileInfo();
	});
</script>

<style>
</style>