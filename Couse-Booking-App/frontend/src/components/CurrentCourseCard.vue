<template>
	<div class="card lg:w-[30%] w-[100%] pb-[20px] relative">
		<div class=" relative w-full h-[240px] flex justify-center px-[20px] pt-[20px] overflow-hidden">
			<img :src="currentCourse.course_image_url" class="w-[100%] h-[90%] rounded-md" />
			<div class="absolute lg:bottom-[30px] left-[-5px] bottom-[60px] bg-[#28C7D4]
         w-fit h-[40px] flex items-center justify-center 
         text-[#252525] text-[16px] cursor-pointer text-center p-[10px] rounded-[6px]">
				<p class="capitalize text-[16px] text-white font-medium">{{ currentCourse.level }}</p>
			</div>
		</div>
		<div class="w-full px-[20px] flex justify-between flex-row h-auto items-center">
			<div class="w-[50%] h-full flex items-center">
				<h3 class="text-language-heading text-[18px]  font-bold capitalize">
					{{ currentCourse.name }}
				</h3>
			</div>
			<div class="flex gap-[15px] w-fit h-full rounded-[16px] items-center">

				<div :class="[
					isActive ? 'active' : 'inactive',
					'rounded-[5px]'
				]">
					<p>{{ status }}</p>
				</div>
			</div>
		</div>
		<div class="w-full h-[50px] flex items-start gap-[10px] px-[19px]">
			<div class="w-[30px] h-[30px]">
				<img src="/images/weeks.svg" class="w-full h-full" />
			</div>
			<div class="h-[30px] flex items-center text-gray-600">
				<p>{{ startDate }}god. - {{ endDate }}god.</p>
			</div>
		</div>

		<div class="flex gap-[10px] h-[30px] items-start justify-start pr-[15px] pt-[3px] w-full pl-[20px]">
			<div class="w-[18px] h-[19px] cursor-pointer hover:scale-105" @click="
				$router.push({
					name: 'UpdateCurrentCourse',
					query: { courseId: currentCourse.id },
				})
				">
				<img src="/images/pencil.svg" class="w-full h-full" />
			</div>

			<div class="w-[20px] h-[20px] cursor-pointer hover:scale-105" @click="
				$router.push({
					name: 'CourseInfo',
					query: { courseId: currentCourse.id },
				})
				">
				<img src="/images/eye2.svg" class="w-full h-full" />
			</div>

			<div class="w-[20px] h-[20px] cursor-pointer hover:scale-105" @click="toggleConfirmCard">
				<img src="/images/delete-x.svg" class="w-full h-full" />
			</div>
		</div>
		<!-- Confirm Card Component -->
		<ConfirmCard :confirmCard="confirmCard" @onDelete="deleteCurrentCourse" @onCancelDelete="toggleConfirmCard" />
	</div>
</template>

<script setup>
import { formatDate } from "@/composables/formatDate.js";
import { onMounted, ref } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import ConfirmCard from "./ConfirmCard.vue";
import { useConfirmCard } from '@/composables/useConfirmCard.js'; 

const props = defineProps({
	currentCourse: Object,
});

const emit = defineEmits(["currentCourseRemoved"]);

// Confirm Card Options
const { confirmCard, toggleConfirmCard } = useConfirmCard();

const status = ref("");
let startDate = ref("");
let endDate = ref("");

const isActive = ref(null);

startDate.value = formatDate(props.currentCourse.start_at, false);
endDate.value = formatDate(props.currentCourse.end_at, false);

const dateNow = new Date(Date.now()).getTime();
const start = new Date(props.currentCourse.start_at).getTime();
const end = new Date(props.currentCourse.end_at).getTime();

const chehckStatus = () => {
	if (end < dateNow) {
		status.value = "Finished";
		isActive.value = false;
		return;
	} else if (start < dateNow) {
		status.value = "Closed";
		isActive.value = false;
		return;
	}
	status.value = "Active";
	isActive.value = true;
};

const deleteCurrentCourse = async () => {
	emit("currentCourseRemoved", props.currentCourse);
	confirmCard.value = false
};

const cancelDelete = () => {
	confirmCard.value = false
}

const showConfirmCard = () => {
	confirmCard.value = true
	
}

onMounted(() => {
	chehckStatus();
});
</script>

<style></style>