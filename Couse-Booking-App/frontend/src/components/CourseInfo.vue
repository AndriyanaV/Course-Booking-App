<template>
	<div class="flex w-[1100px] flex-col justify-start items-center gap-[10px]">
		<div class="title-desc">
			<div class="title">
				<p>Level</p>
			</div>
			<div class="description">
				<p>{{ course.level }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Duration</p>
			</div>
			<div class="description">
				<p>{{ course.weeks_duration }} Weeks</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Price</p>
			</div>
			<div class="description">
				<p>{{ course.price }}$</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Start Date</p>
			</div>
			<div class="description">
				<p>{{ startDate }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>End Date</p>
			</div>
			<div class="description">
				<p>{{ endDate }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Max Members</p>
			</div>
			<div class="description">
				<p>{{ course.max_members }}</p>
			</div>
		</div>
		<div class="w-full h-[350px] flex rounded-sm">
			<div
				class="w-[40%] flex items-center justify-start h-full flex-col rounded-sm"
			>
				<div
					class="w-full h-[90px] bg-[#9989B4] text-[#FFFF] flex flex-col items-center justify-center font-medium text-[32px] font-gilroy rounded-sm"
				>
					<p>Teacher</p>
				</div>
				<div class="w-full h-[250px] rounded-sm">
					<img
						:src="course.user_image_url"
						class="w-full h-full rounded-b-sm"
					/>
				</div>
			</div>
			<div
				class="w-[60%] h-[350px] flex flex-col rounded-bl-md rounded-br-md rounded-sm"
			>
				<div
					class="w-full h-[90px] flex bg-white justify-center items-center text-[24px] font-gilroy font-normal text-[#A49D9D] rounded-l-lg-md rounded-sm"
				>
					<p>{{ course.first_name }} {{ course.last_name }}</p>
				</div>
				<div
					class="w-full h-[250px] bg-white text-[18px] font-gilroy font-normal text-[#A49D9D] px-[40px] rounded-sm"
				>
					<p>
						{{ course.biography }}
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { formatDate } from "@/composables/formatDate.js";
	import { ref, onMounted, watch } from "vue";

	const props = defineProps({
		course: Object,
	});

	let startDate = ref(null);
	let endDate = ref(null);

	const updateDates = () => {
		startDate.value = formatDate(props.course.start_at, true);

		endDate.value = formatDate(props.course.end_at, false);
	};

	onMounted(() => {
		updateDates();
	});

	watch(
		() => props.course,
		() => {
			updateDates();
		}
	);
</script>

<style>
</style>
