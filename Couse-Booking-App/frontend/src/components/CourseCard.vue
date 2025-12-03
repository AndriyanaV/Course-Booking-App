<template>
	<div
		class="lg:min-w-[30%] lg:max-w-[30%] max-w-[100%] lg:mt-[5px] h-fit min-h-max flex flex-col items-center justify-start gap-[20px] bg-[rgba(239,239,239,0.45)] rounded-md shadow-custom relative">
		<div class="w-full lg:h-[240px] h-[200px] rounded-md flex justify-center px-[20px] pt-[20px]">
			<img :src="course.course_image_url" class="w-[100%]  h-[100%] rounded-md" />
		</div>

		<div class="w-full h-fit flex flex-col  gap-[40px] justify-center items-center px-[20px] pb-[20px]">
			<div class="w-[100%] h-full flex items-start justify-between">
				<div class="w-[70%] h-full flex justify-start items-start">
					<h2 class="text-[#7c9fef] text-[22px] font-bold capitalize ">
						{{ course.name }}
					</h2>
				</div>
				<div class="flex gap-[6px] h-full w-[30%] items-start justify-end">
					<div class="w-[19px] h-[18px] cursor-pointer hover:scale-105" @click="
						$router.push({
							name: 'UpdateCourse',
							query: { courseId: course.id },
						})
						">
						<img src="/images/pencil.svg" class="w-full h-full" />
					</div>

					<!-- <div class="w-[20px] h-[20px] cursor-pointer hover:scale-105" @click="
						$router.push({
							name: 'CourseCardInfo',
							params: { id: course.id },
						})
						">
						<img src="/images/eye2.svg" class="w-full h-full" />
					</div> -->

					<div class="w-[20px] h-[20px] cursor-pointer hover:scale-105" @click="toggleConfirmCard">
						<img src="/images/delete-x.svg" class="w-full h-full" />
					</div>
				</div>
			</div>
			<div class="lg:h-[50px] lg:min-w-[150px] h-[48px] min-w-[100px]">
				<button
					class="bg-[#46A5BA] hover:bg-[#4096a9] text-white font-bold py-2 px-4 rounded h-full min-w-[100px]"
					@click="
						$router.push({ name: 'AllCurrentCourses', params: { id: course.id } })
						">
					View Cureent Courses
				</button>
			</div>
		</div>

		<!-- Confirm Card Component -->
		<ConfirmCard :confirmCard="confirmCard" @onDelete="deleteCourse" @onCancelDelete="toggleConfirmCard" />
	</div>
</template>

<script setup>
import axios from "axios";
import { toast } from "vue3-toastify";
import { ref } from "vue";
import ConfirmCard from "./ConfirmCard.vue";
import { useConfirmCard } from '@/composables/useConfirmCard.js'; 

const emit = defineEmits(["courseRemoved"]);

const props = defineProps({
	course: Object,
});

const { confirmCard, toggleConfirmCard } = useConfirmCard();

const deleteCourse = async () => {
	emit("courseRemoved", props.course);
	confirmCard.value = false;
};

</script>

<style></style>