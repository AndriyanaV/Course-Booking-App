<template>
	<div class="flex lg:w-[1100px] flex-col justify-start items-center lg:gap-[10px] cursor-pointer">
		<div class="title-desc">
			<div class="title relative">
				<div class="card-icon">
					<img src="/images/level.png" class="w-[45px]  h-[45px]  object-cover" />
				</div>
				<p>Level</p>
			</div>
			<div class="description">
				
				<p>{{ course.level }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/timeout.png" class="lg:max-w-[30px] w-[44px]  h-[44px] lg:max-h-[30px] object-cover" />
				</div>
				<p>Duration</p>
			</div>
			<div class="description">
				<p>{{ course.weeks_duration }} Weeks</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/money.png" class="w-[43px] h-[43px] object-cover" />
				</div>
				<p>Price</p>
			</div>
			<div class="description">
				<p>{{ course.price }}$</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/lessons-2.png" class="w-[40px] h-[40px] object-cover" />
				</div>
				<p>Number Of Lessons</p>
			</div>
			<div class="description">
				<p>{{ course.lessons }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/level.png" class="w-[40px] h-[40px] object-cover" />
				</div>
				<p>Start Date</p>
			</div>
			<div class="description">
				<p>{{ startDate }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/finish.png" class="w-[40px] h-[40px] object-cover" />
				</div>
				<p>End Date</p>
			</div>
			<div class="description">
				<p>{{ endDate }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<div class="card-icon">
					<img src="/images/level.png" class="w-[40px] h-[40px] object-cover" />
				</div>
				<p>Max Members</p>
			</div>
			<div class="description">
				<p>{{ course.max_members }}</p>
			</div>
		</div>
		<div class="w-full lg:h-[350px] flex lg:flex-row flex-col rounded-sm">
			<div
				class="lg:w-[40%] flex items-center justify-start h-full flex-col rounded-sm"
			>
				<div
					class="min-w-[100%] title"
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
				class="lg:w-[60%] h-[350px] flex flex-col rounded-bl-md rounded-br-md rounded-sm"
			>
				<div
					class="w-full h-[90px] flex lg:bg-white lg:justify-center items-center text-[22px]  font-normal text-[#A49D9D] rounded-l-lg-md rounded-sm"
				>
					<p>{{ course.first_name }} {{ course.last_name }}</p>
				</div>
				<div
					class="w-full h-[250px] lg:bg-white text-[18px] text-start lg:text-center   font-normal text-[#A49D9D] lg:px-[40px] rounded-sm"
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
