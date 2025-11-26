<template>
	<section class="w-full py-[150px] flex flex-col justify-center items-center bg-[#f5f5f4] px-[40px] gap-[60px] h-full">
		<Heading heading="Add new course" color="#2430D6" class="w-full font-bold  text-center" fontSize="46" fontWeight="600"/>
		<CourseForm text="Add" @courseChange="addCourse" />
	</section>
</template>

<script setup>
	import CourseForm from "@/components/CourseForm.vue";
	import Heading from "@/components/Heading.vue";
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