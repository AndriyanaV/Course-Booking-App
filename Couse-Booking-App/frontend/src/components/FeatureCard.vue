<template>
	<div
		class="feature-card-container d-flex flex-column justify-content-center align-items-center gap-3"
	>
		<div class="img-feature-container">
			<img :src="imgSrc" />
		</div>
		<p font-weight-normal>{{ title }}</p>
	</div>
</template>

<script setup>
	defineProps({
		title: String,
		imgSrc: String,
	});
</script>

<style>
	.feature-card-container {
		width: 30%;
		height: 100%;
		background-color: #00015b;
		color: white;
		font-size: 30px;
		z-index: 1;
		padding-top: 20px;
	}
</style>