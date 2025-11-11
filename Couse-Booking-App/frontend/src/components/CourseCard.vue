<template>
	<div
		class="w-[380px] h-fit flex flex-col items-center justify-start gap-[15px] bg-[rgba(239,239,239,0.45)] rounded-md shadow-custom pb-[15px]"
	>
		<div class="w-full h-[265px] rounded-md flex justify-center pt-[20px]">
			<img :src="course.course_image_url" class="w-[90%] h-[90%] rounded-md" />
		</div>

		<div class="w-full h-[64px] flex justify-center items-center">
			<div class="w-[100%] h-full flex items-center justify-between">
				<div class="w-[70%] h-full flex justify-center items-center">
					<h2
						class="text-[#3252E4] text-[25px] font-bold capitalize"
					>
						{{ course.name }}
					</h2>
				</div>
				<div
					class="flex gap-[6px] h-full w-[30%] items-start justify-end pr-[15px] pt-[3px]"
				>
					<div
						class="w-[20px] h-[20px] cursor-pointer hover:scale-105"
						@click="
							$router.push({
								name: 'UpdateCourse',
								query: { courseId: course.id },
							})
						"
					>
						<img src="/images/edit.png" class="w-full h-full" />
					</div>

					<div
						class="w-[20px] h-[20px] cursor-pointer hover:scale-105"
						@click="
							$router.push({
								name: 'CourseCardInfo',
								params: { id: course.id },
							})
						"
					>
						<img src="/images/eye.png" class="w-full h-full" />
					</div>

					<div class="w-[20px] h-[20px] cursor-pointer hover:scale-105" @click="deleteCourse()">
						<img src="/images/delete.png" class="w-full h-full" />
					</div>
				</div>
			</div>
		</div>
		<div class="h-[64px] flex w-full justify-center h-16 items-center">
			<button
				class="bg-second-blue hover:bg-[#2237BA] text-white font-medium py-2 px-4 border border-none rounded h-[42px]  w-[80%]"
				@click="
					$router.push({ name: 'AllCurrentCourses', params: { id: course.id } })
				"
			>
				View Cureent Courses
			</button>
		</div>
	</div>
</template>

<script setup>
	import axios from "axios";
	import { toast } from "vue3-toastify";

	const emit = defineEmits(["courseRemoved"]);

	const props = defineProps({
		course: Object,
	});

	const deleteCourse = async () => {
		emit("courseRemoved", props.course);
	};
</script>

<style>
</style>