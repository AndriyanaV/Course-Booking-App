<script setup>
	import { RouterLink, RouterView, useRoute } from "vue-router";
	import Navbar from "@/components/Navbar.vue";
	import router from "./router";

	const route = useRoute();
</script>

<template>
	<Navbar v-if="route.name !== 'Login'" />
	<RouterView />
</template>


<style scoped>
</style>
