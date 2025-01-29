<template>
	<div class="w-fit flex justify-center items-center m-0 px-0 h-full">
		<div class="select-wrapper">
			<form
				class="max-w-[358px] w-full h-full flex items-center gap-[15px] min-w-fit"
			>
				<label
					for="countries_disabled"
					class="block mb-0 text-[#4E32BA] text-[18px] font-medium min-w-fit"
				>
					Choose a level
				</label>

				<select
					v-model="selectedLevel"
					@change="selectLevel"
					class="bg-black-70 border border-r-4 border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-gray block w-full p-3"
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