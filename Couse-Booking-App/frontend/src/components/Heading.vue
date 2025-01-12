<template>
	<div>
		<h2 :style="{ color: color, fontSize: fontSize }">{{ heading }}</h2>
	</div>
</template>

<script setup>
	defineProps({
		heading: String,
		color: String,
		fontSize: String,
	});
</script>

<style scoped>
	h2 {
		font-family: "Gilroy";
		font-weight: 500;
	}
</style>