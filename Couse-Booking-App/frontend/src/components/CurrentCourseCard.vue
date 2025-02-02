<template>
	<div class="card w-[413px] pb-[20px]">
		<div class="w-full h-[265px]">
			<img
				:src="currentCourse.course_image_url"
				class="w-full h-full rounded-md"
			/>
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
				<div :class="isActive ? 'active' : 'inactive'">
					<p>{{ status }}</p>
				</div>
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
			class="flex gap-[10px] h-[30px] w-[30%] items-start justify-start pr-[15px] pt-[3px] w-full pl-[20px]"
		>
			<div
				class="w-[23px] h-[23px] cursor-pointer"
				@click="
					$router.push({
						name: 'UpdateCurrentCourse',
						query: { courseId: currentCourse.id },
					})
				"
			>
				<img src="/images/edit.png" class="w-full h-full" />
			</div>

			<div
				class="w-[23px] h-[23px] cursor-pointer"
				@click="
					$router.push({
						name: 'CourseInfo',
						query: { courseId: currentCourse.id },
					})
				"
			>
				<img src="/images/eye.png" class="w-full h-full" />
			</div>

			<div
				class="w-[23px] h-[23px] cursor-pointer"
				@click="deleteCurrentCourse"
			>
				<img src="/images/delete.png" class="w-full h-full" />
			</div>
		</div>
	</div>
</template>

<script setup>
	import { formatDate } from "@/composables/formatDate.js";
	import { onMounted, ref } from "vue";
	import axios from "axios";
	import { toast } from "vue3-toastify";

	const emit = defineEmits(["currentCourseRemoved"]);

	const status = ref("");

	const props = defineProps({
		currentCourse: Object,
	});

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
	};

	onMounted(() => {
		chehckStatus();
	});
</script>

<style>
</style>