<template>
	<section class="w-full flex flex-column items-center">
		<section
			class="main w-full flex flex-column items-center h-[1000px] m-0 p-0"
		>
			<section class="w-full mx-0">
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
			<div class="w-[1320px] flex justify-between px-[200px]">
				<SelectLevel @levelSelected="setLevel" />
				<SelectLanguage
					@languageSelected="setLanguage"
					:languageOptions="languageOptions"
				/>
			</div>
		</section>

		<section class="w-full py-12 py-[40px] flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-start items-start m-0 flex-wrap gap-[40px] p-0"
			>
				<div v-if="courses.length === 0" class="w-full h-[100px] text-center">
					<p class="font-gilroy text-[18px] text-[#4E32BA]">
						We still dont't have a course to offfer.
					</p>
				</div>
				<div v-for="course in courses" :key="course.id">
					<LanguageCard :course="course" @courseBooking="bookCourse" />
				</div>
			</div>
		</section>
	</section>
</template>

<script setup>
	import { ref, onMounted, watch } from "vue";
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import FeatureCard from "@/components/FeatureCard.vue";
	import Heading from "@/components/Heading.vue";
	import LanguageFilterCard from "@/components/LanguageFilterCard.vue";
	import LanguageCard from "@/components/LanguageCard.vue";
	import SelectLanguage from "@/components/SelectLanguage.vue";
	import SelectLevel from "@/components/SelectLevel.vue";
	import Navbar from "@/components/Navbar.vue";

	let courses = ref([]);
	const languageOptions = ref([]);
	let selectedLanguage = ref("");
	const selectedLevel = ref("");

	watch([selectedLanguage, selectedLevel], () => {
		getCourses();
	});

	const setLanguage = (language) => {
		selectedLanguage.value = language;
	};

	const setLevel = (level) => {
		selectedLevel.value = level;
	};

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

	const getLanguageOptions = async () => {
		try {
			const response = await axios.get(
				"api/current-courses/get-language-options"
			);
			languageOptions.value = response.data;
		} catch (error) {
			toast.error(error.message || error.response.data.message);
		}
	};

	const bookCourse = async (id) => {
		try {
			if (confirm("Are you sure?")) {
				const response = await axios.post(`api/users/book-course/${id}`);
				toast.success(response.data.message);
			}
		} catch (error) {
			toast.error(error.response.data.message || error.message);
		}
	};

	onMounted(() => {
		getCourses();
		getLanguageOptions();
	});
</script>

<style scoped>
</style>
