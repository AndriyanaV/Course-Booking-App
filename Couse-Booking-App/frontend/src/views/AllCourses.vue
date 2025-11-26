<template>
	<section class="w-full flex items-center flex-col">
		<section class="container max-w-[1320px] mx-auto w-full py-12 pr-0 flex justify-center pt-[150px] px-[40px] bg-second-blue">
			<div class="w-1/2 flex items-center text-center">
				<Heading heading="Manage All Courses" color="white"  />
			</div>
			<div class="w-1/2 h-auto flex items-center justify-center">
				<img src="/images/manage-courses.png" class="w-[400px] h-[400px]" />
			</div>
		</section>
		<section class="container max-w-[1320px] mx-auto px-[40px] py-12 flex justify-between items-center">
			<SelectLanguage
				@languageSelected="setLanguage"
				:languageOptions="languageOptions"
			/>
			<Button
				text="Add Course"
				@buttonClicked="$router.push({ name: 'AddCourse' })"
			/>
		</section>
		<section class="container max-w-[1320px] mx-auto px-[40px] flex justify-center h-auto pb-[40px]" >
			<div
				class="w-[1320px] flex flex-row flex-wrap justify-start items-start m-0 gap-[40px] p-0"
			>
				<div v-for="course in courses" :key="course.id" class="mt-[30px]">
					<CourseCard :course="course" @courseRemoved="deleteCourse" />
				</div>
			</div>
		</section>
	</section>
</template>

<script setup>
	import axios from "axios";
	import { ref, watch, onMounted } from "vue";
	import { toast } from "vue3-toastify";
	import Heading from "@/components/Heading.vue";
	import CourseCard from "@/components/CourseCard.vue";
	import SelectLanguage from "@/components/SelectLanguage.vue";
	import Button from "@/components/Button.vue";

	const languageOptions = ref([]);

	const setLanguage = (language) => {
		selectedLanguage.value = language;
	};

	let courses = ref("");
	let selectedLanguage = ref(null);
	console.log(selectedLanguage.value);

	watch(selectedLanguage, () => {
		getAllCourses();
	});

	const getAllCourses = async () => {
		try {
			const response = await axios.get("/api/admin/get-all-courses", {
				params: {
					language: selectedLanguage.value,
				},
			});
			courses.value = response.data;
		} catch (error) {
			toast.error(error.message);
		}
	};

	const deleteCourse = async (deletedCourse) => {
		if (confirm("Are you sure?")) {
			try {
				const response = await axios.delete(
					`api/admin/delete-course/${deletedCourse.id}`
				);
				courses.value = courses.value.filter(
					(course) => course.id !== deletedCourse.id
				);
				toast.success(response.data.message);
			} catch (error) {
				toast.error(error.response?.data?.message || error.message);
			}
		}
	};

	const getLanguageOptions = async () => {
		try {
			const response = await axios.get(
				"api/current-courses/get-language-options"
			);
			languageOptions.value = response.data;
		} catch (error) {
			console.log(error);
		}
	};

	onMounted(() => {
		getAllCourses();
		getLanguageOptions();
	});
</script>

<style>
</style>