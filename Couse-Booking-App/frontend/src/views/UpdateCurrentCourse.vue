<template>
	<section class="w-full flex justify-center pt-[200px]">
		<UpdateCurrentCourseForm
			:course="course"
			@activeCourseUpdated="updateActiveCourse"
		/>
	</section>
</template>

<script setup>
	import { useRoute, useRouter } from "vue-router";
	import { ref } from "vue";
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import UpdateCurrentCourseForm from "@/components/UpdateCurrentCourseForm.vue";

	const route = useRoute();
	const router = useRouter();
	const courseId = Number(route.query.courseId);
	const course = ref({});

	const getCourseInfo = async () => {
		await axios
			.get(`api/current-courses/course-info/${courseId}`)

			.then((response) => {
				course.value = response.data;
				console.log(response.data);
			})
			.catch(function (error) {
				console.log(error);
			});
	};

	const updateActiveCourse = async (form) => {
		try {
			const response = await axios.put(
				`api/admin/update-current-course/${courseId}`,
				{
					professor: form.professor,
					price: form.price,
					start_at: form.startAt,
					end_at: form.endAt,
					level: form.level,
					location: form.location,
					max_members: form.members,
					lessons: form.lessons,
				}
			);
			router
				.push(`/all-courses`)
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error);
		}
	};

	// const updateActiveCourse = async () => {
	// 	if (
	// 		!price.value ||
	// 		!members.value ||
	// 		!startAt.value ||
	// 		!endAt.value ||
	// 		!lessons.value ||
	// 		!professor.value ||
	// 		!location.value ||
	// 		!level.value
	// 	) {
	// 		toast.error("Please enter all filds.");
	// 		return;
	// 	}
	// 	try {
	// 		const response = await axios.put(
	// 			`api/admin/update-current-course/${courseId}`,
	// 			{
	// 				professor: professor.value,
	// 				price: price.value,
	// 				start_at: startAt.value,
	// 				end_at: endAt.value,
	// 				level: level.value,
	// 				location: location.value,
	// 				max_members: members.value,
	// 				lessons: lessons.value,
	// 			}
	// 		);
	// 		router
	// 			.push(`/all-current-courses/${courseId}`)
	// 			.then(() => toast.success(response.data.message));
	// 	} catch (error) {
	// 		toast.error(error);
	// 	}
	// };

	getCourseInfo();
</script>

<style>
</style>