<template>
	<section
		class="w-full bg-[#F8F7F7] flex justify-start py-[20px] pt-[200px] flex-col items-center m-0 gap-[70px]"
	>
		<Heading heading="Course Info" color="#14003B" fontWeight="medium" />

		<CourseCardInfo :courseId="id" />
	</section>
</template>

<script setup>
	import CourseCardInfo from "@/components/CourseCardInfo.vue";
	import Heading from "@/components/Heading.vue";
	import { ref } from "vue";
	import { useRoute } from "vue-router";

	const route = useRoute();
	const id = route.params.id;
</script>

<style scoped>
</style>