<template>
	<section
		class="w-full py-[100px] px-[60px] flex justify-center bg-white h-screen"
	>
		<div
			class="w-[1320px] flex flex-row flex-wrap bg-white justify-start items-start m-0 flex-wrap gap-[40px] p-0"
		>
			<div v-for="course in currentCourses" :key="course['current_courses.id']">
				<CurrentCourseCard :currentCourse="course" />
			</div>
		</div>
	</section>
</template>
  


<script setup>
	import { useRoute } from "vue-router";
	import { ref } from "vue";
	import { toast } from "vue3-toastify";
	import axios from "axios";
	import CurrentCourseCard from "@/components/CurrentCourseCard.vue";
	const route = useRoute();
	const id = route.params.id;

	let currentCourses = ref("");

	const token = localStorage.getItem("access_token");

	const getAllCurrentCourses = async () => {
		try {
			const response = await axios.get(
				`/api/admin/get-all-current-courses/${id}`,
				{
					headers: {
						Authorization: `Bearer ${token}`, // Dodajemo token u header
					},
				}
			);
			currentCourses.value = response.data;
			console.log("current");
		} catch (error) {
			toast.error(error.message);
		}
	};

	getAllCurrentCourses();
</script>

<style>
</style>