<template>
	<div class="relative overflow-hidden card-container cursor-pointer flex flex-col justify-center items-start  bg-[rgba(239,239,239,0.45)] border-0 rounded-md shadow-custom min-w-[350px] mt-[20px] h-auto"
		style="background-color: rgba(239, 239, 239, 0.45)">
		<div class="w-full h-[220px] m-0 mt-[10px] flex justify-center relative">
			<img :src="course.course_image_url" class="h-[95%] w-[90%]  cover" />
			<div class="absolute bottom-[20px] left-[-5px] bg-blue-500
         w-fit h-[40px] flex items-center justify-center 
         text-[#252525] text-[16px] cursor-pointer text-center p-[10px] rounded-[6px]">
				<p class="capitalize text-[16px] text-white font-medium">{{ course.level }}</p>
			</div>
		</div>
		<div class="flex flex-col items-start  justify-start w-full pb-[10px] h-fit gap-[16px]">
			<div class="flex items-center justify-start gap-[40px] h-auto w-full px-[20px]">

				<div class=" flex justify-start h-auto items-center">
					<h4 class="text-[#3252E4] text-[20px] font-bold capitalize h-auto">
						{{ course.name }}
					</h4>
				</div>
			</div>

			<div
				class="w-[80%] text-[#878686] text-[14px] flex flex-col justify-start items-start px-[20px] h-auto gap-[8px] ">
				<div class="flex w-fit h-auto gap-[8px]  items-center justify-between ">
					<div class="min-w-[28px] min-h-[28px]">
						<img src="/images/lessons.svg" class="max-w-[28px] h-max-[28px] object-contain" />
					</div>
					<p class="text-[16px]"><b>{{ course.lessons }}</b> Lessons</p>
				</div>
				<div class="flex w-fit h-auto gap-[8px] items-center">
					<div class="min-w-[28px] min-h-[28px]">
						<img src="/images/weeks.svg" class="max-w-[28px] h-max-[28px] object-contain" />
					</div>
					<p class="text-[16px]"><b>{{ course.weeks_duration }}</b> Weeks</p>
				</div>

				<div class="flex w-fit h-auto gap-[8px]  items-center justify-between">
					<div class="min-w-[28px] min-h-[28px]">
						<img src="/images/start.svg" class="max-w-[28px] h-max-[28px] object-contain" />
					</div>
					<span class="text-[16px] font-normal">Start at: {{ startDate }}</span>
				</div>
			</div>

			<div class="w-full flex flex-col gap-[10px] h-fit">
				<div class=" flex justify-end h-auto items-center w-full px-[20px]">
					<div
						class="text-[16px]  font-bold  text-[#3E9C52]  flex items-center justify-center h-auto w-[160px]">
						<span class="font-bold"> {{ course.price + "$" }} </span>
					</div>
				</div>
				<div class="flex gap-[20px]  h-fit w-full justify-center items-center">
					<button
						class="flex flex-row-reverse gap-[4px] hover:scale-105 hover:text-gray-600 border-none text-gray-600 font-semibold items-center border  rounded h-fit text-[16px]"
						@click="
							$router.push({ name: 'CourseInfo', query: { courseId: course.id } })
							">
						Learn More
						<img src="/images/arrow-more.png"
							class="max-w-[28px] h-max-[28px] object-contain rotate-[30deg]" />
					</button>
					<button @click="bookCourse()"
						class="bg-[#4A6CF7] hover:bg-[#2367d4] text-white font-normal py-2 px-4 border w-[160px] rounded h-[42px]">
						Reverse a spot
					</button>
				</div>


			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, computed } from "vue";
import { formatDate } from "@/composables/formatDate.js";

const props = defineProps({
	course: Object,
});

const emit = defineEmits(["courseBooking"]);

const startDate = ref("");

startDate.value = formatDate(props.course.start_at, false);

const bookCourse = () => {
	emit("courseBooking", props.course.id);
};
</script>

<style scoped></style>