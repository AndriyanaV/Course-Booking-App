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
		const token = localStorage.getItem("access_token");

		try {
			const response = await axios.post("api/admin/add-course", formData, {
				headers: {
					Authorization: `Bearer ${token}`,
				},
			});
			toast.success(response.data.message);
			router.push({ name: "AllCourses" });
		} catch (error) {
			toast.error(error.message);
		}
	};
</script>

<style>
</style>