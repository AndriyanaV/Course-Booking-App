<template>
	<section class="w-full flex items-center flex-col">
		<section class="w-full py-12 pr-0 flex justify-center">
			<Heading heading="All Current Courses" color="#4E32BA" />
		</section>

		<section class="w-[1320px] py-12 pr-0 flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-start items-center m-0 pt-[10px] px-0"
			>
				<div class="select-wrapper w-[360px]">
					<!-- <div>Selected: {{ selectedLevel }}</div> -->
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
							v-model="selectedLevel"
							class="bg-black-70 border border-r-4 border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-gray block w-full p-3 dark:bg-gray-100 dark:placeholder-gray-400 dark:text-[#4E32BA] dark:focus:ring-blue-500 dark:focus:border-[#15074d]"
						>
							<option disabled value="">Please select level you want</option>
							<option value="">All Levels</option>
							<option value="beginner">Beginner</option>
							<option value="intermediate">Intermediate</option>
							<option value="advanced">Advanced</option>
						</select>
					</form>
				</div>
			</div>
			<div class="h-[60px] w-[200px]">
				<button
					class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full w-[200px]"
					@click="
						$router.push({ name: 'AddCurrentCourse', query: { courseId: id } })
					"
				>
					Add Active Course
				</button>
			</div>
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
						@currentCourseRemoved="filterCurrentCourse"
					/>
				</div>
			</div>
		</section>
	</section>
</template>
  


<script setup>
	import { useRoute } from "vue-router";
	import { ref, watch } from "vue";
	import { toast } from "vue3-toastify";
	import axios from "axios";
	import CurrentCourseCard from "@/components/CurrentCourseCard.vue";
	import Heading from "@/components/Heading.vue";

	const route = useRoute();
	const id = route.params.id;

	let currentCourses = ref("");
	let selectedLevel = ref("");

	watch(selectedLevel, () => {
		getAllCurrentCourses();
	});

	const token = localStorage.getItem("access_token");

	const getAllCurrentCourses = async () => {
		try {
			const response = await axios.get(
				`/api/admin/get-all-current-courses/${id}`,
				{
					params: {
						level: selectedLevel.value,
					},

					headers: {
						Authorization: `Bearer ${token}`, // Dodajemo token u header
					},
				}
			);
			currentCourses.value = response.data;
			console.log(currentCourses);
		} catch (error) {
			toast.error(error.message);
		}
	};

	const filterCurrentCourse = (deletedCourse) => {
		currentCourses.value = currentCourses.value.filter(
			(course) => course.id !== deletedCourse.id
		);
	};

	getAllCurrentCourses();
</script>

<style>
</style>