<template>
	<div class="font-gilroy">
		<h1
			:style="{
				color: color,
				fontWeight: fontWeight,
				fontSize: (fontSize || 70) + 'px',
			}"
			class="font-medium"
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
		fontSize: Number, 
	});
</script>

<style scoped>
</style>