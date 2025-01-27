<template>
	<section class="w-full flex flex-column items-center">
		<section
			class="main w-full flex flex-column items-center h-[1000px] m-0 p-0"
		>
			<section class="min-w-[100%]">
				<div class="container min-w-[100%] p-0">
					<img src="/images/Hero-img.svg" class="min-w-[100%]" />
				</div>
			</section>

			<section class="w-full flex justify-center z-10">
				<div
					class="container max-w-[1320px] mx-auto flex flex-row justify-between gap-[60px] -mt-[190px] h-[240px]"
				>
					<FeatureCard title="Realiable" imgSrc="/images/reliable.svg" />
					<FeatureCard title="Fast Search" imgSrc="/images/search.svg" />
					<FeatureCard title="Easy Booking" imgSrc="/images/easy-book.svg" />
				</div>
			</section>
		</section>

		<section class="w-full py-[40px]">
			<div class="container max-w-[1320px] flex justify-center">
				<Heading heading="Our Courses" color="#4E32BA" />
			</div>
		</section>

		<section class="w-full py-12 pr-0 flex justify-center">
			<div class="w-[1320px] flex justify-center">
				<div
					class="container max-w-[50%] flex justify-center items-center m-0 pt-[10px] px-0"
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
								Choose a level
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
				<div
					class="container max-w-[50%] flex justify-center items-center m-0 pt-[10px] px-0"
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
								Choose a language
							</label>

							<select
								v-model="selectedLanguage"
								class="bg-black-70 border border-r-4 border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-gray block w-full p-3 dark:bg-gray-100 dark:placeholder-gray-400 dark:text-[#4E32BA] dark:focus:ring-blue-500 dark:focus:border-[#15074d] capitalize"
							>
								<option disabled value="">
									Please select language you want
								</option>
								<option value="">All Languages</option>
								<option
									v-for="languageOption in languageOptions"
									:key="languageOption.id"
									:value="languageOption.language"
									class="capitalize"
								>
									{{ languageOption.language }}
								</option>
							</select>
						</form>
					</div>
				</div>
			</div>
		</section>

		<section class="w-full py-12 py-[40px] flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-start items-start m-0 flex-wrap gap-[40px] p-0"
			>
				<div v-if="courses.length === 0" class="w-full h-[100px] text-center">
					<p class="font-gilroy">We still dont't have a course to offfer.</p>
				</div>
				<div v-for="course in courses" :key="course.id">
					<LanguageCard :course="course" />
				</div>
			</div>
		</section>
	</section>
</template>

<script setup>
	import { ref, onMounted, watch } from "vue";
	import axios from "axios";
	import FeatureCard from "@/components/FeatureCard.vue";
	import Heading from "@/components/Heading.vue";
	import LanguageFilterCard from "@/components/LanguageFilterCard.vue";
	import LanguageCard from "@/components/LanguageCard.vue";
	import Navbar from "@/components/Navbar.vue";

	let courses = ref([]);
	const languageOptions = ref([]);
	let selectedLanguage = ref("");

	const selectedLevel = ref("");

	function changeLanguage(language) {
		selectedLanguage.value = language;
	}

	watch([selectedLanguage, selectedLevel], () => {
		getCourses();
	});

	const getCourses = async () => {
		try {
			const response = await axios.get("api/current-courses/get-courses", {
				params: {
					language: selectedLanguage.value,
					level: selectedLevel.value,
				},
			});
			courses.value = response.data;
		} catch (error) {
			console.log(error);
		}
	};

	const getLnaguageOptions = async () => {
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
		getCourses();
		getLnaguageOptions();
	});
</script>

<style scoped>
</style>
