<template>
	<section
		class="w-full py-[150px] flex flex-col justify-center items-center bg-[#f5f5f4] lg:px-[40px] px-[20px]  h-full">
		<div class="container max-w-[1320px] mx-auto flex flex-col justify-center items-center text-center lg:gap-[60px] gap-[40px]">
			<Heading heading="Add New Course" color="#46A5BA" class="w-full font-bold  text-center" fontSize="46"
				fontWeight="600" />
			<CourseForm buttonText="Add Course" @courseChange="addCourse" />
		</div>
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
		toast.error(error.response?.data?.message || error.message);
	}
};
</script>

<style></style>