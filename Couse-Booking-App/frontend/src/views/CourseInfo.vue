<template>
	<section class="w-full  flex justify-start py-[20px] pt-[150px] flex-col items-center m-0 px-[40px]">
		<div class="max-w-[1320px] mx-0 container flex justify-center flex-col">
			<div class="w-full py-[20px] flex justify-center">
				<Heading heading="Course Info" color="#5a32d1" />
			</div>
			<div class="w-full py-[20px] flex justify-center">
				<CourseInfo :course="course" />
			</div>
			<div class="container max-w-[1320px] mx-0 px-[40px] mt-[20px]">
			<div v-if="userRole === 'admin' || userRole === 'professor'"
				class="w-[1100px] flex flex-col justify-between items-center gap-[20px]">
				<div class="w-full justify-between flex items-center">
					<Heading heading="Members" color="#14003B" fontWeight="medium" fontSize="40" />
					<Button text="See Members" @buttonClicked="getMembers()" />
				</div>

				<div v-if="isMembers" class=" w-full flex justify-center py-[50px]">
					<p class="">No Registered Users yet!</p>
				</div>

				<div v-else v-for="member in members" :key="member.id" class="flex items-center w-full">
					<CourseMember :member="member" @memberDeleted="cancelReservation" />
				</div>
			</div>
		</div>
		</div>
	</section>
</template>

<script setup>
import { useUserRole } from "@/composables/useUserRole.js";
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";
import Heading from "@/components/Heading.vue";
import CourseInfo from "@/components/CourseInfo.vue";
import Button from "@/components/Button.vue";
import CourseMember from "@/components/CourseMember.vue";
import { toast } from "vue3-toastify";

let course = ref("");
const members = ref("");

const route = useRoute();
const id = route.query.courseId;

const isMembers = ref(false);

const { userRole, checkUserRole } = useUserRole();

const getCourseInfo = async () => {
	try {
		const response = await axios.get(`api/current-courses/course-info/${id}`);
		console.log(response.data);
		course.value = response.data;
	} catch (error) {
		toast.error(error.message);
	}
};

const getMembers = async () => {
	try {
		const response = await axios.get(`api/current-courses/get-memebers/${id}`);
		members.value = response.data;

		if (members.value == "") {
			isMembers.value = true;
		}
	} catch (error) {
		toast.error(error.response.data.message || error.message);
	}
};

const cancelReservation = async (deletedMember) => {
	if (confirm("Are you sure?")) {
		try {
			const response = await axios.delete(
				`api/current-courses/cancel-reservation/${deletedMember.id}`
			);
			members.value = members.value.filter(
				(member) => member.id != deletedMember.id
			);
			toast.success(response.data.message);
		} catch (error) {
			toast.error(error.message);
		}
	}
};

onMounted(() => {
	checkUserRole();
	getCourseInfo();
});
</script>


<style scoped></style>