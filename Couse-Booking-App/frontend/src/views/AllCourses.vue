<template>
	<section
		class="w-full py-[100px] px-[60px] flex justify-center bg-white h-screen"
	>
		<div
			class="w-[1320px] flex flex-row flex-wrap bg-white justify-start items-start m-0 flex-wrap gap-[40px] p-0"
		>
			<div v-for="course in courses" :key="course.id">
				<CourseCard :course="course" />
			</div>
		</div>
	</section>
</template>

<script setup>
	import axios from "axios";
	import { ref } from "vue";
	import { toast } from "vue3-toastify";

	import CourseCard from "@/components/CourseCard.vue";

	const token = localStorage.getItem("access_token");
	console.log(token);
	let courses = ref("");

	const getAllCourses = async () => {
		try {
			const response = await axios.get(`/api/admin/get-all-courses`, {
				headers: {
					Authorization: `Bearer ${token}`, // Dodajemo token u header
				},
			});
			courses.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	getAllCourses();
</script>

<style>
</style>