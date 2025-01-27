<script setup>
	import { RouterLink, RouterView } from "vue-router";
	import Navbar from "@/components/Navbar.vue";
	import router from "./router";
</script>

<template>
	<Navbar />
	<RouterView />
</template>


<style scoped>
</style>
