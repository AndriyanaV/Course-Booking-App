<template>
	<section class="w-full flex justify-center pt-[150px]">
		<UserProfileForm :user="user" />
	</section>
</template>

<script setup>
	import UserProfileForm from "@/components/UserProfileForm.vue";
	import axios from "axios";
	import { ref, onMounted } from "vue";
	import { toast } from "vue3-toastify";

	const user = ref({});

	const getUserProfileInfo = async () => {
		try {
			const response = await axios.get("api/users/user-profile");
			user.value = response.data;
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