<template>
	<div
		class="card-container flex flex-column justify-center items-start rounded-lg bg-[rgba(239,239,239,0.45)] border-0 rounded-md gap-[10px] pb-[10px] shadow-custom w-[413px]"
		style="background-color: rgba(239, 239, 239, 0.45)"
	>
		<div class="w-full h-[265px]">
			<img :src="course.course_image_url" class="w-full h-full" />
		</div>
		<div
			class="w-full px-[19px] flex justify-between flex-row h-[60px] items-center"
		>
			<div class="w-[50%] h-full flex items-center">
				<h3 class="text-[#10012C] text-[18px]  font-bold capitalize">
					{{ course.name }}
				</h3>
			</div>
			<div
				class="flex gap-[15px] w-[50%] h-full justify-center flex items-center"
			>
				<div class="level">
					<p class="capitalize">{{ course.level }}</p>
				</div>
			</div>
		</div>
		<div class="w-full h-[50px] flex items-start gap-[10px] px-[19px]">
			<div class="w-[30px] h-[30px]">
				<img src="/images/calendar.svg" class="w-full h-full" />
			</div>
			<div class="h-[30px] flex items-center">
				<p>{{ startDate }}- {{ endDate }}god.</p>
			</div>
		</div>

		<div class="px-[19px] flex w-full gap-[50px] h-16 items-center">
			<button
				class="bg-blue-800 hover:bg-[#06088C] text-white font-medium py-2 px-4 border border-gray-400 rounded h-[42px] w-[200px]"
				@click="
					$router.push({ name: 'CourseInfo', query: { courseId: course.id } })
				"
			>
				More Details
			</button>
			<div
				class="text-[16px]  font-bold w-[75px] text-[#00000e] text-[16px] flex items-center justify-center border border-[#c5c5c5] h-[42px]"
			>
				<span class="font-bold"> {{ course.price }}$</span>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref, watch } from "vue";
	import { formatDate } from "@/composables/formatDate.js";

	const props = defineProps({
		course: Object,
	});

	let startDate = ref("");
	let endDate = ref("");

	startDate.value = formatDate(props.course.start_at, true);
	endDate.value = formatDate(props.course.end_at, false);
</script>

<style>
</style>