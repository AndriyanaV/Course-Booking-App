<template>
	<div
		class="w-[413px] h-fit flex flex-col items-center justify-start gap-[15px] bg-[rgba(239,239,239,0.45)] rounded-md shadow-custom pb-[15px]"
	>
		<div class="w-full h-[265px]">
			<img :src="course.course_image_url" class="w-full h-full rounded-md" />
		</div>

		<div class="w-full h-[64px] flex justify-center items-center">
			<div class="w-[100%] h-full flex items-center justify-between">
				<div class="w-[70%] h-full flex justify-center items-center">
					<h2
						class="text-[#10012C] text-[25px] font-gilroy font-bold capitalize"
					>
						{{ course.name }}
					</h2>
				</div>
				<div
					class="flex gap-[6px] h-full w-[30%] items-start justify-end pr-[15px] pt-[3px]"
				>
					<div
						class="w-[20px] h-[20px] cursor-pointer"
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
						class="w-[20px] h-[20px] cursor-pointer"
						@click="
							$router.push({
								name: 'CourseCardInfo',
								params: { id: course.id },
							})
						"
					>
						<img src="/images/eye.png" class="w-full h-full" />
					</div>

					<div class="w-[20px] h-[20px] cursor-pointer" @click="deleteCourse()">
						<img src="/images/delete.png" class="w-full h-full" />
					</div>
				</div>
			</div>
		</div>
		<div class="h-[64px] flex w-full justify-center h-16 items-center">
			<button
				class="bg-[#293580] hover:bg-[#2237BA] text-white font-medium py-2 px-4 border border-blue-800 rounded h-[42px] h-[50px] w-[80%]"
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
		try {
			const token = localStorage.getItem("access_token");
			const response = await axios.delete(
				`api/admin/delete-course/${props.course.id}`,
				{
					headers: {
						Authorization: `Bearer ${token}`,
					},
				}
			);
			toast.success(response.data.message);
			emit("courseRemoved", props.course);
		} catch (error) {
			toast.error(
				error.response?.data?.message ||
					"An error occurred while deleting the course."
			);
		}
	};
</script>

<style>
</style>