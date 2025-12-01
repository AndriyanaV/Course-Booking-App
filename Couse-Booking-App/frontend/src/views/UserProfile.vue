<template>
	<section class="w-full flex justify-center items-start bg-gradient-to-b from-[#2d3cff]/20 to-white min-h-screen lg:px-[40px] px-[20px]">
		<div class="container max-w-[1320px] mx-auto flex flex-col justify-center items-center  py-[150px] text-center">
			<UserProfileForm :user="user" />
		</div>
	</section>
</template>

<script setup>
import UserProfileForm from "@/components/UserProfileForm.vue";
import axios from "axios";
import { ref, onMounted } from "vue";
import { toast } from "vue3-toastify";
import Heading from "@/components/Heading.vue";

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

<style></style>