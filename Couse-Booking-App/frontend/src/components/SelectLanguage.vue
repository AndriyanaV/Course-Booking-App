<template>
	<div class="w-fit flex justify-center items-center m-0 px-0">
		<div class="select-wrapper w-fit">
			<form
				class="max-w-[358px] w-full h-full flex items-center gap-[15px] min-w-fit"
			>
				<label
					for="countries_disabled"
					class="block mb-0 text-[#4E32BA] text-[18px] font-medium min-w-fit"
				>
					Choose a language
				</label>

				<select
					v-model="selectedLanguage"
					@change="selectLanguage()"
					class="bg-black-70 border border-r-4 border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-gray block w-full p-3 dark:bg-gray-100 dark:placeholder-gray-400 dark:text-[#4E32BA] dark:focus:ring-blue-500 dark:focus:border-[#15074d] capitalize"
				>
					<option disabled value="">Please select language you want</option>
					<option value="">All Languages</option>
					<option
						v-for="languageOption in languageOptions"
						:key="languageOption.id"
						:value="languageOption.language"
						class="capitalize"
					>
						{{ languageOption.language }}
					</option>
				</select>
			</form>
		</div>
	</div>
</template>

<script setup>
	import { ref } from "vue";

	const props = defineProps({
		languageOptions: Object,
	});

	const selectedLanguage = ref("");

	const emit = defineEmits(["languageSelected"]);

	const selectLanguage = () => {
		emit("languageSelected", selectedLanguage.value);
	};
</script>

<style>
</style>