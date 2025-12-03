<template>
	<div class="relative overflow-hidden card-container  py-[20px] cursor-pointer flex flex-col justify-center items-start   border-0 rounded-md shadow-custom lg:min-w-[350px] mt-[20px] h-auto"
		style="background-color: rgba(239, 239, 239, 0.45)">
		<div class="w-full h-[220px] m-0 mt-[10px] flex justify-center relative">
			<img :src="course.course_image_url" class="h-[95%] w-[90%] cover" />
					<div class="absolute bottom-[20px] left-[-5px] bg-[#28C7D4]
         w-fit h-[40px] flex items-center justify-center 
         text-[#252525] text-[16px] cursor-pointer text-center p-[10px] rounded-[6px]">
						<p class="capitalize text-[16px] text-white font-medium">{{ course.level }}</p>
					</div>
		</div>
		<div class="flex flex-col gap-[16px] w-full h-auto px-[20px]">
			<div class="w-full  flex justify-between flex-row h-[60px] items-center">
				<div class="w-full h-fit flex items-center">
					<h3 class="text-language-heading text-[18px]  font-bold capitalize">
						{{ course.name }}
					</h3>
				</div>
				<div class="flex gap-[15px] w-[50%] h-full justify-center  items-center">
			
				</div>
			</div>
			<div class="w-full h-[50px] flex items-start gap-[10px] ">
				<div class="w-[24px] h-[24px]">
					<img src="/images/timeout.png" class="w-[100%] h-[100%] object-cover" />
				</div>
				<div class="h-[30px] flex items-center">
					<p class="text-gray-500">{{ startDate }}- {{ endDate }}god.</p>
				</div>
			</div>
			<div class="flex h-fit w-full justify-between">
				<Button  :mt="false"  text="More Info" @buttonClicked="$router.push({ name: 'CourseInfo', query: { courseId: course.id } })" />
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
import Button from "./Button.vue";

const props = defineProps({
	course: Object,
});

let startDate = ref("");
let endDate = ref("");

startDate.value = formatDate(props.course.start_at, true);
endDate.value = formatDate(props.course.end_at, false);
</script>

<style></style>