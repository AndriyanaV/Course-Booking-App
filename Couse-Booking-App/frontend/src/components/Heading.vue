<template>
	<div class="container flex justify-center w-full font-gilroy">
		<h1
			:style="{ color: color, fontWeight: fontWeight }"
			class="text-h1 font-medium"
		>
			{{ heading }}
		</h1>
	</div>
</template>

<script setup>
	defineProps({
		heading: String,
		color: String,
		fontWeight: String,
	});
</script>

<style scoped>
</style>