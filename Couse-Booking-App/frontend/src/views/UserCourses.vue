<template>
	<section class="w-full py-[40px] flex justify-center lg:px-[40px] px-[20px] ">
		<div
			class="container max-w-[1320px] mx-auto flex  flex-col text-center  h-auto mt-[100px] justify-center  rounded-[10px] gap-[20px]">
			<Heading heading="My Courses" color="#46A5BA" class="w-full font-bold" fontSize="64" />
				<div class="w-full flex lg:flex-row flex-col gap-[40px]">
					<UserCourseCard v-for="course in courses" :key="course.id" :course="course" />
				</div>
		</div>
	</section>
</template>

<script setup>
import UserCourseCard from "@/components/UserCourseCard.vue";
import Heading from "@/components/Heading.vue";
import { ref, onMounted } from "vue";
import { toast } from "vue3-toastify";
import axios from "axios";

const courses = ref([]);

const getUserCourses = async () => {
	try {
		const response = await axios.get("api/users/user-courses");
		courses.value = response.data;
	} catch (error) {
		toast.error(error.response.data.message || error.message);
	}
};

onMounted(() => {
	getUserCourses();
});
</script>

<style></style>