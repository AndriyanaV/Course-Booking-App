<template>
	<section class="w-full py-[150px] flex flex-col items-center justify-center bg-[#EFEFEF] h-full gap-[60px]">
		<Heading heading="Update Course Info" color="#2D3CFF" class="w-full font-bold  text-center" fontSize="46" fontWeight="700"/>
		<CourseForm :course="course" text="Update" @courseChange="updateCourse" />
	</section>
</template>

<script setup>
	import CourseForm from "@/components/CourseForm.vue";
	import Heading from "@/components/Heading.vue";
	import { useRoute, useRouter } from "vue-router";
	import { toast } from "vue3-toastify";
	import axios from "axios";
	import { ref, onMounted } from "vue";

	const route = useRoute();
	const router = useRouter();
	const id = route.query.courseId;
	const course = ref({});

	const getCourseInfo = async () => {
		try {
			const response = await axios.get(`api/admin/get-course/${id}`);
			course.value = response.data;
		} catch (error) {
			toast.error(error);
		}
	};

	const updateCourse = async (form) => {
		const formData = new FormData();
		formData.append("name", form.name);
		formData.append("language", form.language.toLowerCase());
		formData.append("file", form.image);

		try {
			const response = await axios.put(`api/admin/update-course/${id}`, formData);
			router
				.push("/all-courses")
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.message);
		}
	};

	onMounted(() => {
		getCourseInfo();
	});
</script>

<style>
</style>