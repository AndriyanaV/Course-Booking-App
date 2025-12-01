<template>
	<section class="w-full py-[150px] flex flex-col justify-center items-center bg-[#f5f5f4] lg:px-[40px] px-[20px]  h-full">
		<div
			class="container max-w-[1320px] mx-auto flex flex-col justify-center items-center text-center lg:gap-[60px] gap-[40px]">
			<Heading heading="Update Course Info" color="#46A5BA" class="w-full font-bold  text-center" fontSize="46"
				fontWeight="700" />
			<CurrentCourseForm :course="course" buttonText="Update Course Info"
				@currentCourseChange="updateActiveCourse" />
		</div>
	</section>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import CurrentCourseForm from "@/components/CurrentCourseForm.vue";
import Heading from "@/components/Heading.vue";

const route = useRoute();
const router = useRouter();
const courseId = Number(route.query.courseId);
const course = ref({});

const getCourseInfo = async () => {
	await axios
		.get(`api/current-courses/course-info/${courseId}`)

		.then((response) => {
			course.value = response.data;
			console.log(response.data);
		})
		.catch(function (error) {
			console.log(error);
		});
};

const updateActiveCourse = async (form) => {
	try {
		const response = await axios.put(
			`api/admin/update-current-course/${courseId}`,
			{
				professor: form.professor,
				price: form.price,
				start_at: form.startAt,
				end_at: form.endAt,
				level: form.level.toLowerCase(),
				location: form.location,
				max_members: form.members,
				lessons: form.lessons,
			}
		);
		router
			.push(`/all-current-courses/${course.value.course_id}`)
			.then(() => toast.success(response.data.message));
	} catch (error) {
		toast.error(error);
	}
};

onMounted(() => {
	getCourseInfo();
});
</script>

<style></style>