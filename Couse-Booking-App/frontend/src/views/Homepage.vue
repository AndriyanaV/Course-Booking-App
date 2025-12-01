<template>
	<!-- Hero Section -->

	<section class="w-full lg:flex flex-col items-center lg:px-[40px] px-[20px]">
		<div
			class="container max-w-[1320px] mx-auto flex lg:flex-row flex-col bg-[#EFEFFF] h-auto mt-[100px]  rounded-[10px] gap-[20px]">
			<div
				class="sm:w-[55%] w-full flex justify-start flex-col items-start lg:gap-[30px] gap-[20px] sm:pl-[50px] pl-[20px] sm:pr-[0px] pr-[20px] pt-[50px] pb-[50px]">
				<div
					class="min-w-[200px] h-[40px] flex justify-start  items-center gap-[8px] p-4 ring-1 ring-inset ring-[#9B91E2] rounded-lg cursor-pointer">
					<div class="lg:max-w-[28px] lg:h-max-[28px] max-w-[24px] max-h-[24px]"><img
							src="/images/sparkle.png" class="max-w-[100%] h-max-[100%] object-contain" /></div>
					<p class="text-[#4F4A4A] font-poppins"> A sign of bravery</p>
				</div>
				<div class="flex flex-col lg:gap-[20px] gap-[14px]">
					<Heading heading="Connection Starts with One Word" color="#363232" class="w-full font-bold"
						fontSize="64" />
					<p class="text-[#4F4A4A] lg:w-[75%] w-[95%]">Advance with confidence in every language lesson. Every
						step
						you take brings you closer to fluency.</p>
				</div>
				<Button text="Start your journey" class="mt-[10px]" @buttonClicked="goToCourses"></Button>
			</div>
			<div class="lg:w-[45%] flex justify-center flex-col items-center">
				<img src="/images/hero-img.png" class="max-w-[80%] h-max-[80%] object-contain lg:mt-[60px]" />
			</div>

		</div>

	</section>

	<!-- Benefit Cards -->

	<section class="w-full flex flex-col items-center lg:px-[40px] px-[20px]">
		<div
			class="container max-w-[1320px] mx-auto flex lg:flex-row flex-col justify-between  h-auto lg:py-[80px] py-[40px] lg:gap-[40px] gap-[20px]">
			<FeatureCard v-for="(card, index) in featureCards" :key="index" :title="card.title" :desc="card.desc"
				:imgSrc="card.imgSrc" :isActive="activeIndex === index" />
		</div>
	</section>


	<main>

		<!-- Course Cards -->

		<section ref="courseSection" class="w-full flex flex-col items-center justify-center lg:py-[80px] py-[40px] lg:px-[40px] px-[20px]">
			<div class="container max-w-[1320px] mx-auto flex flex-col lg:gap-[80px] gap-[80px] ">
				<!-- Heading and Filters -->
				<div class=" w-full h-auto flex flex-col gap-[40px]">
					<div class="w-full flex flex-col justify-center text-center gap-[10px]">
						<Heading heading="Our Courses" color="#7786EB" class="w-full font-bold" fontSize="56" />
						<p class="text-gray-500 lg:text-lg">Discover your next course – it’s waiting</p>
					</div>
					<div class="w-full pr-0 flex justify-center ">
						<div class="w-full flex justify-center lg:gap-[100px] gap-[40px] flex-wrap h-fit">
							<SelectLevel @levelSelected="setLevel" />
							<SelectLanguage @languageSelected="setLanguage" :languageOptions="languageOptions" />
						</div>
					</div>
				</div>

				<!-- Course Cards Container-->

				<div class="w-full flex justify-start items-start m-0 flex-wrap gap-[40px] ">
					<div v-if="courses.length === 0" class="w-full h-[100px] text-center">
						<p class=" text-[18px] text-[#688BFF]">
							We still don't have a course to offer.
						</p>
					</div>

					<div class="w-full flex flex-wrap lg:gap-[30px]  gap-[20px] lg:justify-start justify-center h-fit">
						<div v-for="course in courses" :key="course.id">
							<LanguageCard :course="course" @courseBooking="bookCourse" />
						</div>
					</div>
				</div>

			</div>
		</section>


		<section class="w-full flex justify-center lg:px-[40px] px-[20px] lg:py-[80px] py-[40px] bg-[#F1F1FD] relative">
			<div class="container max-w[1320px] mx-auto flex flex-col items-center lg:gap-[60px] gap-[40px]  relative overflow-hidden ">
				<div class="absolute w-full lg:w-[55%] left-1/2 bottom-0 -translate-x-1/2"><img src="/images/teacher.png"
						class=" object-contain opacity-40 lg:h-[65%] " /></div>
				<div class="w-full flex flex-col gap-[16px] text-center">
					<h2 class="lg:text-[56px] text-[#363232] font-bold text-[32px]"><span
							class="text-[#86CBBB] font-bold">Language School</span>– Where Words Become Bridges Between
						People</h2>
					<p class="text-gray-500 text-lg">
						Learn with heart today, and speak with confidence tomorrow
					</p>
				</div>

				<div class="w-full flex lg:gap-[20px] gap-[40px] sm:flex-wrap lg:justify-center lg:items-center overflow-x-scroll lg:overflow-hidden lg:pl-[0px] pl-[20px]">
					<div v-for="p in pros" class="lg:w-[30%] lg:min-w-[30%] w-[350px] min-w-[300px] min-h-[240px]">
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
import Button from "@/components/Button.vue";


const courses = ref([]);
const languageOptions = ref([]);
const selectedLanguage = ref("");
const selectedLevel = ref("");

const courseSection = ref(null)

//Smooth Scroll 
function goToCourses() {
  courseSection.value?.scrollIntoView({ behavior: "smooth" });
}

//Feature cards 
const activeIndex = ref(0)
let intervalId = null

const setLanguage = (language) => {
	selectedLanguage.value = language;
};

const setLevel = (level) => {
	selectedLevel.value = level;
};

// Get courser at filter change
watch([selectedLanguage, selectedLevel], () => {
	getCourses();
});

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
		toast.error(error.response?.data?.message || error.message);
	}
};

//Api call for languages select
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
		toast.error(error.response?.data?.message || error.message);
	}
};

//Features cards data

const featureCards = [
	{ title: 'Realiable', desc: 'Your trusted online language school.', imgSrc: '/images/pen.png' },
	{ title: 'Fast Search', desc: 'The fastest way to find your perfect language course.', imgSrc: '/images/pen.png' },
	{ title: 'Easy Booking', desc: 'Simple and fast booking. Your spot, secured instantly.', imgSrc: '/images/pen.png' },
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
