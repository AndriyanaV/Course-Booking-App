<template>
	<div class="lg:w-fit w-full flex lg:justify-center justify-between items-center m-0 px-0 h-full">
		<div class="select-wrapper">
			<form
				class="lg:max-w-[358px] w-full h-full lg:justify-center justify-between flex items-center gap-[15px] min-w-fit"
			>
				<label
					for="countries_disabled"
					class="block mb-0 text-[#688BFF] lg:text-[18px] font-medium min-w-fit "
				>
					Choose a level
				</label>

				<select
					v-model="selectedLevel"
					@change="selectLevel"
					class="bg-black-70 border border-r-4 border-[#688BFF] text-gray-600 text-sm rounded-lg focus:ring-blue-200 focus:border-gray block lg:w-fit w-1/2 p-3"
				>
					<option disabled value="">Please select level you want</option>
					<option value="">All Levels</option>
					<option value="beginner">Beginner</option>
					<option value="intermediate">Intermediate</option>
					<option value="advanced">Advanced</option>
				</select>
			</form>
		</div>
	</div>
</template>

<script setup>
	import { ref } from "vue";

	const selectedLevel = ref("");

	const emit = defineEmits(["levelSelected"]);

	const selectLevel = () => {
		emit("levelSelected", selectedLevel.value);
	};
</script>

<style>
</style>