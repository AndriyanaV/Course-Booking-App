<template>
	<section class="w-full py-12 pr-0 flex justify-center pt-[150px]">
		<Heading heading="My Courses" color="#4E32BA" />
	</section>
	<section class="w-full py-12 py-[40px] flex justify-center">
		<div
			class="container max-w-[1320px] flex justify-start items-start m-0 flex-wrap gap-[40px] p-0"
		>
			<div v-for="course in courses" :key="course.id">
				<UserCourseCard :course="course" />
			</div>
		</div>
	</section>
</template>

<script setup>
	import UserCourseCard from "@/components/UserCourseCard.vue";
	import Heading from "@/components/Heading.vue";
	import { ref, onMounted } from "vue";
	import { toast } from "vue3-toastify";
	import axios from "axios";

	const courses = ref([]);

	const getProfessorCourses = async () => {
		try {
			const response = await axios.get("api/users/professor-courses");
			courses.value = response.data;
		} catch (error) {
			toast.error(error.message || error.repsonse.message.data);
		}
	};

	onMounted(() => {
		getProfessorCourses();
	});
</script>

<style>
</style>