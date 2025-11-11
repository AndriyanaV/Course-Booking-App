<template>
	<div
		class="backdrop-blur-md flex flex-col items-center justify-center gap-[20px] w-1/4 bg-main-blue h-fill text-white text-[26px]   rounded-md"
	>
		<div class="img-feature-container w-[50px] i h-[50px]">
			<img :src="imgSrc" class="w-full h-full object-cover"/>
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