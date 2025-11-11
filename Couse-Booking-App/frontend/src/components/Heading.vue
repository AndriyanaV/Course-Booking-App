<template>
	<div>
		<h1
			:style="{
				color: color,
				fontSize: (fontSize || 70) + 'px',
			}"
			:class="fontWeight ? '' : 'font-semibold'"
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