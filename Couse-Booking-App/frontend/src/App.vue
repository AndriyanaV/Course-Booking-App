<script setup>
import { RouterLink, RouterView, useRoute } from "vue-router";
import Navbar from "@/components/Navbar.vue";
import LogOutPopUp from "./components/LogOutPopUp.vue";
import router from "./router";
import { onMounted, ref, watchEffect } from "vue";
import { useUserStore } from "./stores/user";

const route = useRoute();

const userStore = useUserStore();

onMounted(() => {
	userStore.initFromStorage();
});

</script>

<template>
	<Navbar v-if="route.name !== 'Login'"/>
	<LogOutPopUp v-if="route.name !== 'Login'" 
		/>
	<RouterView />
</template>


<style scoped></style>
