<template>
	<div class="lg:w-fit w-full flex lg:justify-center justify-between items-center m-0 px-0">
		<div class="select-wrapper w-fit">
			<form
				class="lg:max-w-[358px] w-full  h-full flex items-center gap-[15px] min-w-fit"
			>
				<label
					for="countries_disabled"
					class="block mb-0 text-[#688BFF] lg:text-[18px] font-medium min-w-fit"
				>
					Choose a language
				</label>

				<select
					v-model="selectedLanguage"
					@change="selectLanguage()"
					class="bg-black-70 border border-r-4 border-[#688BFF] text-gray-500 text-sm rounded-lg focus:ring-blue-200 focus:border-gray block lg:min-w-[160px] w-full p-3  capitalize"
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