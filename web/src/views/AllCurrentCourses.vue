<template>
	<main class="w-full flex items-center flex-col ">
		<section class="w-full lg:flex flex-col items-center lg:px-[40px] px-[20px]">
			<div
				class="container max-w-[1320px] mx-auto flex lg:flex-row flex-col bg-soft-blue h-auto mt-[100px]  rounded-[10px] gap-[20px]">
				<div
					class="sm:w-[60%] w-full flex justify-start flex-col items-start lg:gap-[30px] gap-[20px] sm:pl-[50px] pl-[20px] sm:pr-[0px] pr-[20px] pt-[50px] pb-[50px]">

					<div class="flex flex-col lg:gap-[20px] gap-[14px]">
						<Heading heading="Manage Courses for the Selected Language" color="#363232" class="w-full font-bold" fontSize="64" />
						<p class="text-[#4F4A4A] lg:w-[75%] w-[95%]">Manage all courses for selected language: create, update, delete, and adjust course information.</p>
					</div>

				</div>
				<div class="lg:w-[40%] flex justify-center flex-col items-center">
					<img src="/images/current-courses-hero.png" class="max-w-[100%] h-max-[90%] object-contain " />
				</div>

			</div>
		</section>

		<section class="w-full  flex items-center justify-center lg:px-[40px] px-[20px] lg:py-[80px] py-[40px]">
			<div class="container max-w-[1320px] mx-auto  flex lg:flex-row flex-col lg:justify-between gap-[20px] lg:items-center">
				<div>
					<SelectLevel @levelSelected="setLevel" />
				</div>
				<Button text="Add Active Course" @buttonClicked="
					$router.push({ name: 'AddCurrentCourse', query: { courseId: id } })
					"/>
			</div>
		</section>
		<section class="w-full lg:px-[40px] px-[20px] flex justify-center pb-[40px]">
			<div
				class="container max-w-[1320px] mx-auto flex flex-row  justify-start items-start m-0 flex-wrap gap-[40px]">
				<div v-if="currentCourses.length == 0"
					class="w-full h-[100px] text-black flex items-center justify-center">
					<p class="text-[18px] text-gray-600">
						There are no current courses added for the given language course!
					</p>
				</div>
				<CurrentCourseCard v-for="course in currentCourses" :key="course.id" :currentCourse="course" @currentCourseRemoved="deleteCurrentCourse" />
			</div>
		</section>
	</main>
</template>



<script setup>
import { useRoute } from "vue-router";
import { ref, watch, onMounted } from "vue";
import { toast } from "vue3-toastify";
import axios from "axios";
import CurrentCourseCard from "@/components/CurrentCourseCard.vue";
import SelectLevel from "@/components/SelectLevel.vue";
import Heading from "@/components/Heading.vue";
import Button from "@/components/Button.vue";

const route = useRoute();
const id = route.params.id;

let currentCourses = ref([]);
let selectedLevel = ref("");

const setLevel = (level) => {
	selectedLevel.value = level;
};

watch(selectedLevel, () => {
	getAllCurrentCourses();
});

const getAllCurrentCourses = async () => {
	try {
		const response = await axios.get(
			`/api/admin/get-all-current-courses/${id}`,
			{
				params: {
					level: selectedLevel.value,
				},
			}
		);
		currentCourses.value = response.data;
		console.log(currentCourses);
	} catch (error) {
		toast.error(error.message);
	}
};

const deleteCurrentCourse = async (deletedCourse) => {
		try {
			const response = await axios.delete(
				`/api/admin/delete-current-course/${deletedCourse.id}`
			);
			currentCourses.value = currentCourses.value.filter(
				(course) => course.id !== deletedCourse.id
			);
			toast.success(response.data.message);
		} catch (error) {
			toast.error(error.response?.data?.message || error.message);
		}
	}


onMounted(() => {
	getAllCurrentCourses();
});
</script>

<style></style>