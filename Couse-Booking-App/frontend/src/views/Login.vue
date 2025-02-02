<template>
	<section
		class="w-full flex justify-center items-center m-0 h-[688px] bg-black"
	>
		<LoginForm @login="handleEvent" />
	</section>
</template>

<script setup>
	import LoginForm from "@/components/LoginForm.vue";
	import { toast } from "vue3-toastify";
	import axios from "axios";
	import { useRoute, useRouter } from "vue-router";

	const router = useRouter();

	async function handleEvent(payload) {
		try {
			const { email, password } = payload;
			const response = await axios.post("/api/login", { email, password });

			const { access_token, message, role, user_id } = response.data;
			console.log(response.data);

			// Čuvanje tokena i role u localStorage
			const expirationTime = Date.now() + 3 * 24 * 60 * 60 * 1000; // 1 minu
			localStorage.setItem("access_token", access_token);
			localStorage.setItem("token_expiration", expirationTime.toString());
			localStorage.setItem("rola", role);
			localStorage.setItem("user_id", user_id);

			router.push("/").then(() => toast.success(message));
		} catch (error) {
			toast.error(error.response.data.message || error.message);
		}
	}
</script>

<style>
</style>