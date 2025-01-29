<template>
	<div
		class="flex flex-column items-center justify-center gap-[20px] w-[400px] bg-[#06088C] h-fill text-white text-[30px] font-gilroy rounded rounded-md"
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
</style>