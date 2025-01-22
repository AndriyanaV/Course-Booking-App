<template>
	<div
		class="w-[413px] h-[460px] flex flex-col items-center justify-start gap-[20px] bg-[rgba(239,239,239,0.45)] rounded-md shadow-custom"
	>
		<div class="w-full h-[265px]">
			<img :src="course.course_image_url" class="w-full h-full" />
		</div>
		<div class="w-full h-[64px] flex justify-center items-center">
			<h2 class="text-[#10012C] text-[25px] font-gilroy font-bold capitalize">
				{{ course.name }}
			</h2>
		</div>
		<div class="h-[64px] flex w-full justify-center h-16 items-center">
			<button
				class="bg-[#293580] hover:bg-[#2237BA] text-white font-medium py-2 px-4 border border-blue-800 rounded h-[42px] h-[50px] w-[80%]"
				@click="
					$router.push({ name: 'AllCurrentCourses', params: { id: course.id } })
				"
			>
				View Cureent Courses
			</button>
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		course: Object,
	});
</script>

<style>
</style>