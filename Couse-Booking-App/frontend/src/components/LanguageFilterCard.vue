

<template>
	<div class="inactive d-flex align-items-center" @click="handleClick">
		<p>{{ language }}</p>
	</div>
</template>

<script setup>
	import { ref } from "vue";

	defineProps({
		language: String,
	});

	let isActive = ref(true);
</script>

<style scoped>
	.inactive {
		color: #15074d;
		font-family: "Gilroy";
		font-size: 40px;
		background-color: #d2d0e8;
		border-radius: 5px;
		width: 360px;
		height: 70px;
		display: flex;
		justify-content: center;
		align-items: center;
		cursor: pointer;
		/* font-weight: 200; */
	}

	.active {
		color: white;
		background-color: #586ce3;
		font-family: "Gilroy";
		font-size: 40px;
		border-radius: 5px;
		width: 360px;
		height: 70px;
		display: flex;
		justify-content: center;
		align-items: center;
		cursor: pointer;
		font-weight: 600;
	}
</style>