<template>
	<section
		class="w-full bg-[#F8F7F7] flex justify-start py-[20px] pt-[200px] flex-col items-center m-0 gap-[70px]"
	>
		<Heading heading="User Info" color="#14003B" fontWeight="medium" />

		<UserInfo :user="user" />
	</section>
</template>

<script setup>
	import UserInfo from "@/components/UserInfo.vue";
	import Heading from "@/components/Heading.vue";
	import { ref } from "vue";
	import axios from "axios";
	import { useRoute } from "vue-router";

	const route = useRoute();
	const userId = route.query.userId;

	const user = ref({});

	console.log(userId);

	const getUserInfo = async () => {
		await axios
			.get(`api/admin/get-user//${userId}`)

			.then((response) => {
				user.value = response.data;
			})
			.catch(function (error) {
				console.log(error);
			});
	};

	getUserInfo();
</script>

<style>
</style>