<template>
	<section class="main w-full flex flex-column items-center">
		<section class="w-full">
			<div class="container min-w-[100%] p-0">
				<img src="/images/Hero-img.svg" class="min-w-[100%]" />
			</div>
		</section>

		<section class="w-full flex justify-center">
			<div
				class="container max-w-[1320px] mx-auto flex flex-row justify-between gap-[60px] -mt-[190px] h-[240px]"
			>
				<FeatureCard title="Realiable" imgSrc="/images/reliable.svg" />
				<FeatureCard title="Fast Search" imgSrc="/images/search.svg" />
				<FeatureCard title="Easy Booking" imgSrc="/images/easy-book.svg" />
			</div>
		</section>

		<section class="w-full py-32">
			<div class="container max-w-[1320px] flex justify-center">
				<Heading heading="Our Courses" color="#4E32BA" />
			</div>
		</section>

		<section class="w-full flex justify-center">
			<div
				class="container max-w-[1320px] mx-auto flex flex-row justify-between items-start"
			>
				<LanguageFilterCard language="All" />
				<LanguageFilterCard language="English" />
				<LanguageFilterCard language="French" />
			</div>
		</section>

		<section class="w-full py-12 pr-0 flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-start items-center m-0 pt-[10px]"
			>
				<form
					class="max-w-[358px] w-full h-full flex items-center gap-[15px] min-w-fit"
				>
					<label
						for="countries_disabled"
						class="block mb-0 text-[#4E32BA] text-xl font-medium text-gray-900 dark:text-[ #4E32BA] min-w-fit"
					>
						Select a level
					</label>
					<select
						id="countries_disabled"
						class="bg-black-70 border border-[#4E32BA] text-[#4E32BA] text-sm rounded-lg focus:ring-blue-200 focus:border-[ #15074d] block w-full p-3 dark:bg-gray-100 dark:border-[ #15074d] dark:placeholder-gray-400 dark:text-[#4E32BA] dark:focus:ring-blue-500 dark:focus:border-[#15074d]"
					>
						<option selected>Choose the level</option>
						<option value="begginer">Beginner</option>
						<option value="intermediate">Intermediate</option>
						<option value="advanced">Advanced</option>
					</select>
				</form>
			</div>
		</section>

		<section class="w-full py-12 py-[40px] flex justify-center">
			<div
				class="container max-w-[1320px] flex justify-start items-start m-0 flex-wrap gap-[40px] p-0"
			>
				<LanguageCard />
				<LanguageCard />
				<LanguageCard />
				<LanguageCard />
			</div>
		</section>
	</section>
</template>

<script setup>
	import FeatureCard from "@/components/FeatureCard.vue";
	import Heading from "@/components/Heading.vue";
	import LanguageFilterCard from "@/components/LanguageFilterCard.vue";
	import LanguageCard from "@/components/LanguageCard.vue";

	function select(el) {
		console.log(el);
	}
</script>

<style scoped>
</style>
