<template>
	<!-- Hero Section -->
	<section class="w-full flex flex-col items-center">
		<section class="w-full flex flex-col items-center m-0 p-0">
			<section class="w-full mx-0">
				<div class="container min-w-[100%] p-0">
					<img src="/images/Hero-img.svg" class="min-w-[100%]" />
				</div>
			</section>

			<!-- Feature Cards Section -->
			<section class="container flex  z-10 w-full">
				<div
					class="w-full justify-center cursor-pointer mx-auto px-[30px] flex flex-row  gap-[40px] -mt-[140px] min-h-[200px]">
					<FeatureCard v-for="(card, index) in featureCards" :key="index" :title="card.title"
						:imgSrc="card.imgSrc" class="transition-transform duration-500"
						:class="activeIndex === index ? 'scale-105' : 'scale-100'" />
				</div>
			</section>

		</section>
	</section>

	<main>
		<!-- Course Cards -->
		<section class="w-full flex flex-col items-center justify-center py-[50px] mt-[40px] animate-fadeIn">
			<div class="container max-w-[1320px] mx-auto flex flex-col gap-[60px] ">

				<!-- Heading and Filters -->
				<div class=" w-full h-auto flex flex-col gap-[40px] py-[20px]">
					<div class="w-full flex flex-col justify-center text-center">
						<Heading heading="Our Courses" color="var(--main-blue)" class="w-full font-bold" />
						<p class="text-gray-500 text-lg">Discover your next course – it’s waiting</p>
					</div>
					<div class="w-full pr-0 flex justify-center ">
						<div class="w-full flex justify-center gap-[100px] flex-wrap h-fit">
							<SelectLevel @levelSelected="setLevel" />
							<SelectLanguage @languageSelected="setLanguage" :languageOptions="languageOptions" />
						</div>
					</div>
				</div>

				<!-- Course Cards -->
				<div class="w-full flex justify-start items-start m-0 flex-wrap gap-[40px] px-[40px] py-[20px]">
					<div v-if="courses.length === 0" class="w-full h-[100px] text-center">
						<p class=" text-[18px] text-[#4E32BA]">
							We still don't have a course to offer.
						</p>
					</div>

					<div class="w-full flex flex-wrap gap-[30px] justify-start h-fit">
						<div v-for="course in courses" :key="course.id">
							<LanguageCard :course="course" @courseBooking="bookCourse" />
						</div>
					</div>
				</div>

			</div>
		</section>

		<section class="w-full flex justify-center px-[40px] py-[40px]">
			<div class="container max-w[1320px] mx-auto flex flex-col items-center gap-[60px]">
				<div class="w-full flex flex-col gap-[16px] text-center">
					<Heading heading="Language School – Where Words Become Bridges Between People"
						color="#6f4eed" :fontSize="48"/>
					<p class="text-gray-500 text-lg">
						Learn with heart today, and speak with confidence tomorrow
					</p>
				</div>
				
				<div class="w-full flex gap-[20px] flex-wrap justify-center items-center">
					<div v-for="p in pros" class="w-[30%] min-h-[240px]">
						<ProsCard :title="p.title" :desc="p.desc" :imgSrc="p.imgSrc" />
					</div>
					
				</div>




			</div>
		</section>

	</main>

</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import FeatureCard from "@/components/FeatureCard.vue";
import Heading from "@/components/Heading.vue";
import LanguageFilterCard from "@/components/LanguageFilterCard.vue";
import LanguageCard from "@/components/LanguageCard.vue";
import SelectLanguage from "@/components/SelectLanguage.vue";
import SelectLevel from "@/components/SelectLevel.vue";
import Navbar from "@/components/Navbar.vue";
import ProsCard from "@/components/ProsCard.vue";

let courses = ref([]);
const languageOptions = ref([]);
let selectedLanguage = ref("");
const selectedLevel = ref("");

// Get courser at filter change
watch([selectedLanguage, selectedLevel], () => {
	getCourses();
});

const setLanguage = (language) => {
	selectedLanguage.value = language;
};

const setLevel = (level) => {
	selectedLevel.value = level;
};

//Api call for courses
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

//Api call for languages
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

const token = localStorage.getItem("access_token");

//Api call to book course
const bookCourse = async (id) => {
	try {
		if (!token) {
			toast.error("You need to sign in");
			return;
		}
		if (confirm("Are you sure?")) {
			const response = await axios.post(`api/users/book-course/${id}`);
			toast.success(response.data.message);
		}
	} catch (error) {
		toast.error(error.response.data.message || error.message);
	}
};

const featureCards = [
	{ title: 'Realiable', imgSrc: '/images/reliable.svg' },
	{ title: 'Fast Search', imgSrc: '/images/search.svg' },
	{ title: 'Easy Booking', imgSrc: '/images/easy-book.svg' },
]

//Pros cards data
const pros = [
	{
		title: 'Qualified Teachers',
		desc: 'Learn from professionals with real teaching experience.',
		imgSrc: '/images/graduation.png'
	},
	{
		title: 'Structured Program',
		desc: 'Courses are designed to guide you from basics',
		imgSrc: '/images/graduation.png'
	},
	{
		title: 'Motivating Environment',
		desc: 'Learning in a group helps you stay consistent and motivated.',
		imgSrc: '/images/graduation.png'
	},
	{
		title: 'Language Certificate',
		desc: 'Receive an official certificate after completing your course.',
		imgSrc: '/images/graduation.png'
	},
	{
		title: 'Interactive Lessons',
		desc: 'Engaging activities make learning fun and effective.',
		imgSrc: '/images/graduation.png'
	},
	{
		title: 'Cultural Experience',
		desc: 'Explore new cultures while improving your communication skills.',
		imgSrc: '/images/graduation.png'
	}
]

const activeIndex = ref(0)
let intervalId = null

onMounted(() => {
	getCourses();
	getLanguageOptions();

	intervalId = setInterval(() => {
		activeIndex.value = (activeIndex.value + 1) % featureCards.length
	}, 2000)
});

onUnmounted(() => {
	clearInterval(intervalId)
})

</script>

<style scoped></style>
