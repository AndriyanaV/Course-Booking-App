<template>
	<section class="w-full flex items-center flex-col ">
		<section
			class="container max-w-[1320px] mx-auto w-full py-12 pr-0 flex justify-center pt-[150px] px-[40px] bg-second-blue">
			<div class="w-1/2 flex items-center text-center">
				<Heading heading="All Courses of laguage" color="white" />
			</div>
			<div class="w-1/2 h-auto flex items-center justify-center">
				<img src="/images/manage-current-courses.png" class="w-[430px] h-[400px]" />
			</div>
		</section>

		<section class="w-full py-12 flex items-center justify-center px-[40px]">
			<div class="container max-w-[1320px] mx-auto flex justify-between items-center m-0">
				<div>
					<SelectLevel @levelSelected="setLevel" />
				</div>
				<Button text="Add Active Course" @buttonClicked="
					$router.push({ name: 'AddCurrentCourse', query: { courseId: id } })
					" />
			</div>
		</section>
		<section class="w-full py-[100px] px-[60px] flex justify-center pb-[40px]">
			<div
				class="container max-w-[1320px] mx-auto flex flex-row  justify-start items-start m-0 flex-wrap gap-[40px]">
				<div v-if="currentCourses.length == 0"
					class="w-full h-[100px] text-black flex items-center justify-center">
					<p class="text-[18px] text-[#4E32BA]">
						There are no current courses added for the given language course!
					</p>
				</div>
				<div v-else v-for="course in currentCourses" :key="course.id">
					<CurrentCourseCard :currentCourse="course" @currentCourseRemoved="deleteCurrentCourse" />
				</div>
			</div>
		</section>
	</section>
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
	if (confirm("Are you sure?")) {
		try {
			const response = await axios.delete(
				`/api/admin/delete-current-course/${deletedCourse.id}`
			);
			currentCourses.value = currentCourses.value.filter(
				(course) => course.id !== deletedCourse.id
			);
			toast.success(response.data.message);
		} catch (error) {
			toast.error(error.message);
		}
	}
};

onMounted(() => {
	getAllCurrentCourses();
});
</script>

<style></style>