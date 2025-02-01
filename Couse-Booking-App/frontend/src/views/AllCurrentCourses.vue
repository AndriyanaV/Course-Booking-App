<template>
	<section class="w-full flex items-center flex-col pt-[150px]">
		<section class="w-full py-12 pr-0 flex justify-center">
			<Heading heading="All Current Courses" color="#4E32BA" />
		</section>

		<section class="w-[1320px] py-12 pr-0 flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-between items-center m-0 px-0"
			>
				<SelectLevel @levelSelected="setLevel" />
			</div>
			<Button
				text="Add Active Course"
				@buttonClicked="
					$router.push({ name: 'AddCurrentCourse', query: { courseId: id } })
				"
			/>
		</section>
		<section
			class="w-full py-[100px] px-[60px] flex justify-center bg-white h-screen"
		>
			<div
				class="w-[1320px] flex flex-row flex-wrap bg-white justify-start items-start m-0 flex-wrap gap-[40px] p-0"
			>
				<div
					v-if="currentCourses == ''"
					class="w-full h-[100px] text-black flex items-center justify-center"
				>
					<p class="font-gilroy text-black text-[18px]">
						There are no current courses added for the given language course!
					</p>
				</div>
				<div v-else v-for="course in currentCourses" :key="course.id">
					<CurrentCourseCard
						:currentCourse="course"
						@currentCourseRemoved="deleteCurrentCourse"
					/>
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

	let currentCourses = ref("");
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

<style>
</style>