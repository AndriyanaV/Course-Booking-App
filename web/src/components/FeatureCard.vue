<template>
	<div class="border border-[#EEEEEE] shadow-[0_1px_2px_rgba(0,0,0,0.06)] rounded-lg p-4 lg:w-[33%] w-full min-h-[200px] relative overflow-hidden flex justify-strt items-end pb-[40px] bg-[#FEFEFE] cursor-pointer transition-all duration-1000 ease-in-out"
		:class="isActive ? 'scale-[1.01] ' : 'scale-[0.99] '">
		<div class="img-feature-container lg:w-[220px] w-[200px] lg:h-[220px] h-[200px] absolute right-0 top-[0px]">
			<img :src="imgSrc" class="w-full h-full object-cover" />
		</div>
		<div class="flex flex-col gap-[10px] relative z-10 w-[70%]">
			<h5 class="text-[#64ADC1] font-bold lg:text-[28px] text-[24px] m-0 w-full">{{ title }}</h5>
			<p class="text-[#888181]">{{ desc }}</p>

		</div>
	</div>

</template>

<script setup>
defineProps({
	title: String,
	imgSrc: String,
	desc: String,
	isActive: Boolean
});
</script>

<style></style>