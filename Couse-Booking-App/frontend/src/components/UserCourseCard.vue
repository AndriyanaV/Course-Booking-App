<template>
	<div class="relative overflow-hidden card-container cursor-pointer flex flex-col justify-center items-start   border-0 rounded-md shadow-custom min-w-[350px] mt-[20px] h-auto"
		style="background-color: rgba(239, 239, 239, 0.45)">
		<div class="w-full h-[220px] m-0 mt-[10px] flex justify-center relative">
			<img :src="course.course_image_url" class="h-[95%] w-[90%] cover" />
					<div class="absolute bottom-[20px] left-[-5px] bg-blue-500
         w-fit h-[40px] flex items-center justify-center 
         text-[#252525] text-[16px] cursor-pointer text-center p-[10px] rounded-[6px]">
						<p class="capitalize text-[16px] text-white font-medium">{{ course.level }}</p>
					</div>
		</div>
		<div class="flex flex-col gap-[16px] w-full">
			<div class="w-full px-[19px] flex justify-between flex-row h-[60px] items-center">
				<div class="w-full h-fit flex items-center">
					<h3 class="text-[#3252E4] text-[18px]  font-bold capitalize">
						{{ course.name }}
					</h3>
				</div>
				<div class="flex gap-[15px] w-[50%] h-full justify-center flex items-center">
			
				</div>
			</div>
			<div class="w-full h-[50px] flex items-start gap-[10px] px-[19px]">
				<div class="w-[30px] h-[30px]">
					<img src="/images/calendar.png" class="max-w-[28px] h-max-[28px] object-contain" />
				</div>
				<div class="h-[30px] flex items-center">
					<p class="text-gray-500">{{ startDate }}- {{ endDate }}god.</p>
				</div>
			</div>

			<div class="px-[19px] flex w-full gap-[50px] h-16 items-center">
				<button
					class="bg-[#4A6CF7] hover:bg-[#2367d4] text-white font-normal py-2 px-4 border w-[160px] rounded h-[42px]"
					@click="
						$router.push({ name: 'CourseInfo', query: { courseId: course.id } })
						">
					More Details
				</button>
				<div
					class="text-[16px]  font-bold  text-[#3E9C52]  flex items-center justify-center h-auto ">
					<span class="font-bold"> {{ course.price }}$</span>
				</div>
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

<style></style>