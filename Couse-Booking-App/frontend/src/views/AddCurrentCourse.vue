<template>
	<section class="w-full py-[150px] flex flex-col justify-center items-center bg-[#f5f5f4] lg:px-[40px] px-[20px]  h-full">
		<div
			class="container max-w-[1320px] mx-auto flex flex-col justify-center items-center text-center lg:gap-[60px] gap-[40px]">
			<Heading heading="Add New Course for Selected Language" color="#46A5BA" class="w-full font-bold  text-center" fontSize="46"
				fontWeight="600" />
			<CurrentCourseForm buttonText="Add Course" @currentCourseChange="addActiveCourse" />
		</div>
	</section>
</template>

<script setup>
import CurrentCourseForm from "@/components/CurrentCourseForm.vue";
import Heading from "@/components/Heading.vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { toast } from "vue3-toastify";

const route = useRoute();
const router = useRouter();
const id = Number(route.query.courseId);

const addActiveCourse = async (form) => {
	try {
		const response = await axios.post("api/admin/add-current-course", {
			course_id: id,
			user_id: form.professor,
			price: form.price,
			start_at: form.startAt,
			end_at: form.endAt,
			max_members: form.members,
			level: form.level.toLowerCase(),
			location: form.location,
			lessons: form.lessons,
		});
		router
			.push(`/all-current-courses/${id}`)
			.then(() => toast.success(response.data.message));
	} catch (error) {
		toast.error(error.message);
	}
};
</script>

<style></style>