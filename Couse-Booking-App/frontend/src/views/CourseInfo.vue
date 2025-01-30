<template>
	<section
		class="w-full bg-[#F8F7F7] flex justify-start py-[20px] pt-[150px] flex-col items-center m-0 gap-[70px]"
	>
		<Heading heading="Course Info" color="#14003B" fontWeight="medium" />

		<CourseInfo :course="course" />

		<div
			v-if="userRole === 'admin' || userRole === 'professor'"
			class="w-[1100px] flex flex-col justify-between items-center gap-[20px]"
		>
			<div class="w-full justify-between flex items-center">
				<Heading
					heading="Members"
					color="#14003B"
					fontWeight="medium"
					fontSize="40"
				/>
				<Button text="See Members" @buttonClicked="getMembers()" />
			</div>
			<!-- <div
				v-if="members.length === 0"
				class="isMembers? w-full flex justify-center :w-full flex justify-center display-none"
			>
				<p class="font-gilroy font-normal">There is no registered users yet.</p>
			</div> -->

			<div
				v-for="member in members"
				:key="member.id"
				class="flex items-center w-full"
			>
				<CourseMember :member="member" @memberDeleted="filterMemebers" />
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
		} catch (error) {
			toast.error(error.response.data.message || error.message);
		}
	};

	const filterMemebers = (deletedMember) => {
		members.value = members.value.filter(
			(member) => member.id != deletedMember.id
		);
	};

	onMounted(() => {
		checkUserRole();
		getCourseInfo();
	});
</script>


<style scoped>
</style>