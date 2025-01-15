<template>
	<div
		class="flex flex-column items-center justify-center gap-[20px] w-[350px] bg-[#00015B] h-fill text-white text-[30px] font-gilroy rounded"
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