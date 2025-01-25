<template>
	<section class="w-full flex justify-center pt-[200px]">
		<UpdateCurrentCourseForm :courseId="courseId" />
	</section>
</template>

<script setup>
	import { useRoute } from "vue-router";
	import UpdateCurrentCourseForm from "@/components/UpdateCurrentCourseForm.vue";

	const route = useRoute();
	const courseId = route.query.courseId;
</script>

<style>
</style>