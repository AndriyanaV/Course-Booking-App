<template>
	<Navbar bgColor="bg-gray" />
	<section
		class="w-full bg-[#F8F7F7] flex justify-start py-[20px] pt-[200px] flex-col items-center m-0 gap-[70px]"
	>
		<Heading heading="Course Info" color="#14003B" fontWeight="medium" />

		<CourseInfo :course="course" />
	</section>
</template>

<script setup>
	import { useRoute } from "vue-router";
	import { ref } from "vue";
	import axios from "axios";
	import Heading from "@/components/Heading.vue";
	import CourseInfo from "@/components/CourseInfo.vue";
	import Navbar from "@/components/Navbar.vue";

	let course = ref({});

	const route = useRoute();
	const id = route.query.courseId;

	async function getCourseInfo() {
		await axios
			.get(`api/current-courses/course-info/${id}`)

			.then((response) => {
				course.value = response.data;
				console.log(response.data);
			})
			.catch(function (error) {
				console.log(error);
			});
	}

	getCourseInfo();
</script>


<style scoped>
</style>