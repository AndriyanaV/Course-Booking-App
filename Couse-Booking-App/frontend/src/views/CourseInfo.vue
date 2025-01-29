<template>
	<section
		class="w-full bg-[#F8F7F7] flex justify-start py-[20px] pt-[150px] flex-col items-center m-0 gap-[70px]"
	>
		<Heading heading="Course Info" color="#14003B" fontWeight="medium" />

		<CourseInfo :course="course" />
	</section>
</template>

<script setup>
	import { useRoute } from "vue-router";
	import { ref, onMounted } from "vue";
	import axios from "axios";
	import Heading from "@/components/Heading.vue";
	import CourseInfo from "@/components/CourseInfo.vue";
	import { toast } from "vue3-toastify";

	let course = ref("");

	const route = useRoute();
	const id = route.query.courseId;

	const getCourseInfo = async () => {
		try {
			const response = await axios.get(`api/current-courses/course-info/${id}`);
			console.log(response.data);
			course.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	onMounted(() => {
		getCourseInfo();
	});
</script>


<style scoped>
</style>