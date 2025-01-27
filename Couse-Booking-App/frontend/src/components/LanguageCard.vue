<template>
	<div
		class="card-container flex flex-column justify-center items-start rounded-lg bg-[rgba(239,239,239,0.45)] border-0 rounded-md gap-[20px] pb-[20px] shadow-custom w-[413px]"
		style="background-color: rgba(239, 239, 239, 0.45)"
	>
		<div class="w-full h-[270px] m-0">
			<img :src="course.course_image_url" class="h-full w-full rounded-md" />
		</div>
		<div
			class="flex items-center justify-between gap-[40px] h-[64px] w-full py-[10px] pl-[20px]"
		>
			<div
				class="w-[115px] h-[45px] text-center flex items-center justify-center text-[#252525] text-[16px] cursor-pointer bg-gray-200 gap-[20px]"
			>
				<p class="first-letter-uppercase">{{ course.level }}</p>
			</div>
			<div class="w-[55%] flex justify-start h-full items-center">
				<h4 class="text-black text-[20px] font-gilroy font-semibold capitalize">
					{{ course.name }}
				</h4>
			</div>
		</div>

		<div
			class="w-full text-[#a2a2a2] text-[14px] flex justify-between px-[20px] h-[55px]"
		>
			<div
				class="flex w-fit mh-[55px] gap-[6px] flex items-center justify-between mb-[5px]"
			>
				<div class="w-[32px] h-[32px]">
					<img src="/images/clock.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">{{ course.weeks_duration }} Weeks</p>
			</div>
			<div
				class="flex w-fit mh-[55px] gap-[8px] flex items-center justify-center"
			>
				<div class="w-[32px] h-[32px]">
					<img src="/images/lessons.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">{{ course.lessons }} Lessons</p>
			</div>
			<div
				class="flex w-fit mh-[55px] gap-[8px] flex items-center justify-center"
			>
				<div class="w-[32px] h-[32px]">
					<img src="/images/start.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">{{ formattedDate }}</p>
			</div>
		</div>

		<div class="px-[19px] flex w-full justify-between h-16 items-center">
			<button
				class="bg-blue-800 hover:bg-[#06088C] text-white font-medium py-2 px-4 border border-blue-800 rounded h-[42px]"
			>
				Book Now
			</button>
			<button
				class="bg-[#FFFF] hover:bg-gray-200 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded h-[42px]"
				@click="
					$router.push({ name: 'CourseInfo', query: { courseId: course.id } })
				"
			>
				Learn More
			</button>
			<div
				class="text-[16px] font-gilroy font-bold w-[75px] text-[#00000e] text-[16px] flex items-center justify-center border border-[#c5c5c5] h-[42px]"
			>
				<span class="font-bold"> {{ course.price + "$" }} </span>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref, computed } from "vue";
	const props = defineProps({
		course: Object,
	});

	let date = new Date(props.course.start_at);
	let day = date.getDate(); // Dan u mesecu (1-31)
	let month = date.getMonth() + 1; // Mesec (1-12), zato što je `getMonth()` 0-indeksiran
	let year = date.getUTCFullYear(); // Godina (četvorka)
	let formattedDate = `${day}.${month}.${year}`;
</script>

<style scoped>
</style>