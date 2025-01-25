<template>
	<section class="w-full flex justify-center pt-[200px]">
		<AddCurrentCourseForm :courseId="id" />
	</section>
</template>

<script setup>
	import AddCurrentCourseForm from "@/components/AddCurrentCourseForm.vue";
	import { useRoute } from "vue-router";

	const route = useRoute();
	const id = route.query.courseId;
</script>

<style>
</style>