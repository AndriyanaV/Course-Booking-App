<template>
	<section class="w-full pt-[200px] flex justify-center bg-white pb-[40px]">
		<CourseForm text="Add" @courseChange="addCourse" />
	</section>
</template>

<script setup>
	import CourseForm from "@/components/CourseForm.vue";
	import { toast } from "vue3-toastify";
	import { useRouter } from "vue-router";
	import axios from "axios";

	const router = useRouter();

	const addCourse = async (form) => {
		const formData = new FormData();
		formData.append("name", form.name);
		formData.append("language", form.language.toLowerCase());
		formData.append("file", form.image);

		try {
			const response = await axios.post("api/admin/add-course", formData);
			router
				.push("/all-courses")
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.response.data.message || error.message);
		}
	};
</script>

<style>
</style>