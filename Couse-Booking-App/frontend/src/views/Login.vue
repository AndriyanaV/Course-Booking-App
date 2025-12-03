<template>
	<section class="w-full flex justify-center items-center m-0 min-h-screen py-[20px]">
		<div class="container max-w-[1320px] mx-0 flex justify-center items-center h-full">
			 <LoginForm :serverMessage="serverMessage" 
			@login="handleLogin" />
		</div>
	</section>
</template>

<script setup>
import LoginForm from "@/components/LoginForm.vue";
import { toast } from "vue3-toastify";
import axios from "axios";
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

const router = useRouter();

const serverMessage = ref(null)

const userStore = useUserStore();

async function handleLogin(payload) {
  try {
    const { email, password } = payload;
    const response = await axios.post("/api/login", { email, password });

    const { access_token, message, role, user_id } = response.data;

    //Set user data using a store 
    userStore.setUser({ role, user_id, token: access_token });

    router.push("/").then(() => toast.success(message));
  } catch (error) {
    serverMessage.value = error.response?.data?.message || error.message;
  }
}
</script>

<style></style>