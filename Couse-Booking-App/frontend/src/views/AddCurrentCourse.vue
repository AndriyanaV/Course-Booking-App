<template>
	<section class="w-full flex justify-center pt-[200px]">
		<AddCurrentCourseForm @activeCourseAdded="addActiveCourse" />
	</section>
</template>

<script setup>
	import AddCurrentCourseForm from "@/components/AddCurrentCourseForm.vue";
	import { useRoute, useRouter } from "vue-router";
	import axios from "axios";
	import { toast } from "vue3-toastify";

	const route = useRoute();
	const router = useRouter();
	const id = Number(route.query.courseId);
	// console.log("id");
	// console.log(id);

	const addActiveCourse = async (form) => {
		try {
			const response = await axios.post("api/admin/add-current-course", {
				course_id: id,
				user_id: form.professor,
				price: form.price,
				start_at: form.startAt,
				end_at: form.endAt,
				max_members: form.members,
				level: form.level,
				location: form.location,
				lessons: form.lessons,
			});
			router
				.push(`/all-current-courses/${id}`)
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.message);
		}
	};
</script>

<style>
</style>