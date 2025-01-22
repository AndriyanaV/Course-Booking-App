<template>
	<div class="card w-[413px]">
		<div class="w-full h-[265px]">
			<img :src="currentCourse.course_image_url" class="w-full h-full" />
		</div>
		<div
			class="w-full px-[19px] flex justify-between flex-row h-[65px] items-center"
		>
			<div class="w-[50%] h-full flex items-center">
				<h3 class="text-[#10012C] text-[18px] font-gilroy font-bold capitalize">
					{{ currentCourse.name }}
				</h3>
			</div>
			<div class="flex gap-[15px] w-[50%] h-full flex items-center">
				<div class="level">
					<p class="capitalize">{{ currentCourse.level }}</p>
				</div>
				<div class="level bg-red-500 text-[#ffff]"><p>level</p></div>
			</div>
		</div>
		<div class="w-full h-[50px] flex items-start gap-[10px] px-[19px]">
			<div class="w-[30px] h-[30px]">
				<img src="/images/calendar.svg" class="w-full h-full" />
			</div>
			<div class="h-[30px] flex items-center">
				<p>{{ startDate }}god. - {{ endDate }}god.</p>
			</div>
		</div>
		<div
			class="w-full h-[65px] flex items-cnter gap-[10px] px-[19px] justify-between"
		>
			<div class="edit">
				<i class="fas fa-edit" style="color: #ffffff"></i>
				<p class="text-white font-gilroy">Edit</p>
			</div>
			<div class="preview">
				<i class="fa-solid fa-eye" style="color: #020342"></i>
				<p class="font-gilroy text-[#020342]">Preview</p>
			</div>
			<div class="delete">
				<i class="fa-solid fa-trash-can" style="color: #db0021"></i>
				<p class="font-gilroy text-red-500">Delete</p>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { formatDate } from "@/composables/formatDate.js";
	import { ref } from "vue";
	const props = defineProps({
		currentCourse: Object,
	});

	let startDate = ref("");
	let endDate = ref("");

	startDate.value = formatDate(props.currentCourse.start_at, false);
	endDate.value = formatDate(props.currentCourse.end_at, false);
</script>

<style>
</style>