<template>
	<section class="w-full pt-[200px] flex justify-center bg-[#EFEFEF] pb-[40px]">
		<AddCourseForm @courseAdded="addCourse" />
	</section>
</template>

<script setup>
	import AddCourseForm from "@/components/AddCourseForm.vue";
	import { toast } from "vue3-toastify";
	import { useRouter } from "vue-router";
	import axios from "axios";

	const router = useRouter();

	const addCourse = async (form) => {
		const formData = new FormData();
		formData.append("name", form.courseName);
		formData.append("language", form.language);
		formData.append("file", form.image);

		try {
			const response = await axios.post("api/admin/add-course", formData);
			router
				.push("/all-courses")
				.then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.message);
		}
	};
</script>

<style>
</style>