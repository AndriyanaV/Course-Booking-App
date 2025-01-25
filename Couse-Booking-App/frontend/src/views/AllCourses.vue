<template>
	<section class="w-full flex items-center flex-col">
		<section class="w-full py-12 pr-0 flex justify-center">
			<Heading heading="All  Courses" color="#4E32BA" />
		</section>
		<section class="w-[1320px] py-12 flex justify-center items-center">
			<div
				class="container max-w-[1320px] flex justify-start items-center m-0 pt-[10px] px-0"
			>
				<div class="select-wrapper w-[360px]">
					<!-- <div>Selected: {{ selectedLanguage }}</div> -->
					<form
						class="max-w-[358px] w-full h-full flex items-center gap-[15px] min-w-fit"
					>
						<label
							for="countries_disabled"
							class="block mb-0 text-[#4E32BA] text-[18px] font-medium min-w-fit"
						>
							Select a level
						</label>

						<select
							v-model="selectedLanguage"
							class="bg-black-70 border border-r-4 border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-gray block w-full p-3 dark:bg-gray-100 dark:placeholder-gray-400 dark:text-[#4E32BA] dark:focus:ring-blue-500 dark:focus:border-[#15074d]"
						>
							<option disabled value="">Please select level you want</option>
							<option value="%">All Languages</option>
							<option value="english">English</option>
							<option value="french">French</option>
						</select>
					</form>
				</div>
			</div>
			<div class="h-[60px] w-[150px]">
				<button
					class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full w-[150px]"
					@click="$router.push({ name: 'AddCourse' })"
				>
					Add Course
				</button>
			</div>
		</section>
		<section class="w-full py-[20px] flex justify-center bg-white h-screen">
			<div
				class="w-[1320px] flex flex-row flex-wrap bg-white justify-start items-start m-0 flex-wrap gap-[40px] p-0"
			>
				<div v-for="course in courses" :key="course.id">
					<CourseCard :course="course" @courseRemoved="filterCourses" />
				</div>
			</div>
		</section>
	</section>
</template>

<script setup>
	import axios from "axios";
	import { ref, watch } from "vue";
	import { toast } from "vue3-toastify";
	import Heading from "@/components/Heading.vue";
	import CourseCard from "@/components/CourseCard.vue";

	const token = localStorage.getItem("access_token");

	let courses = ref("");
	let selectedLanguage = ref(null);
	console.log(selectedLanguage.value);

	watch(selectedLanguage, () => {
		getAllCourses();
	});

	const getAllCourses = async () => {
		try {
			const response = await axios.get("/api/admin/get-all-courses", {
				headers: {
					Authorization: `Bearer ${token}`, // Dodajemo token u header
				},
				params: {
					language: selectedLanguage.value,
				},
			});
			courses.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	const filterCourses = (deletedCourse) => {
		courses.value = courses.value.filter(
			(course) => course.id !== deletedCourse.id
		);
		console.log("filtriram");
	};

	getAllCourses();
</script>

<style>
</style>