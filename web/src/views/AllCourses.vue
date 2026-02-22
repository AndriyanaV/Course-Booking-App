<template>
	<main class="w-full flex items-center flex-col">
		<section class="w-full lg:flex flex-col items-center lg:px-[40px] px-[20px]">
			<div
				class="container max-w-[1320px] mx-auto flex lg:flex-row flex-col bg-soft-blue h-auto mt-[100px]  rounded-[10px] gap-[20px]">
				<div
					class="sm:w-[55%] w-full flex justify-start flex-col items-start lg:gap-[30px] gap-[20px] sm:pl-[50px] pl-[20px] sm:pr-[0px] pr-[20px] pt-[50px] pb-[50px]">
					
					<div class="flex flex-col lg:gap-[20px] gap-[14px]">
						<Heading heading="Manage Courses" color="#363232" class="w-full font-bold"
							fontSize="64" />
						<p class="text-[#4F4A4A] lg:w-[75%] w-[95%]">Manage all courses: create, update, delete, and adjust course information.</p>
					</div>
					
				</div>
				<div class="lg:w-[45%] flex justify-center flex-col items-center">
					<img src="/images/manage-courses.png" class="max-w-[100%] h-max-[90%] object-contain " />
				</div>

			</div>
		</section>
		<section class="container max-w-[1320px] mx-auto lg:px-[40px] px-[20px] lg:py-[80px] py-[40px] flex lg:flex-row flex-col lg:justify-between gap-[20px] lg:items-center">
			<SelectLanguage @languageSelected="setLanguage" :languageOptions="languageOptions" />
			<Button text="Add Course" @buttonClicked="$router.push({ name: 'AddCourse' })"/>
		</section>
		<section class="w-full flex  justify-center lg:py-[0px] lg:pb-[40px] py-[20px] lg:px-[40px] px-[20px]">
			<div class="container max-w-[1320px] mx-auto lg:flex-wrap flex lg:flex-row flex-col lg:gap-[20px] lg:justify-start h-auto gap-[40px] ">
				<CourseCard v-for="course in courses" :key="course.id" :course="course" @courseRemoved="deleteCourse" />
			</div>
		</section>
	</main>
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
		toast.error(error.response?.data?.message || error.message);
	}
};

const deleteCourse = async (deletedCourse) => {
	
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
	
};

const getLanguageOptions = async () => {
	try {
		const response = await axios.get(
			"api/current-courses/get-language-options"
		);
		languageOptions.value = response.data;
	} catch (error) {
		toast.error(error.response?.data?.message || error.message);
	}
};

onMounted(() => {
	getAllCourses();
	getLanguageOptions();
});
</script>

<style></style>