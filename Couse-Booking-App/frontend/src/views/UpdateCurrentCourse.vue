<template>
	<section class="w-full flex flex-col justify-center items-center py-[150px] gap-[60px] h-full">
		<Heading heading="Update Course Info" color="#2D3CFF" class="w-full font-bold  text-center" fontSize="46" fontWeight="700"/>
		<CurrentCourseForm
			:course="course"
			text="Update"
			@currentCourseChange="updateActiveCourse"
		/>
	</section>
</template>

<script setup>
	import { useRoute, useRouter } from "vue-router";
	import { ref, onMounted } from "vue";
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import CurrentCourseForm from "@/components/CurrentCourseForm.vue";
	import Heading from "@/components/Heading.vue";

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
					level: form.level.toLowerCase(),
					location: form.location,
					max_members: form.members,
					lessons: form.lessons,
				}
			);
			router
				.push(`/all-current-courses/${course.value.course_id}`)
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error);
		}
	};

	onMounted(() => {
		getCourseInfo();
	});
</script>

<style>
</style>