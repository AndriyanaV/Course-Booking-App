<template>
	<div class="container-fluid">
		<div class="hero-img-container w-100 p-0">
			<img src="/images/Hero-img.svg" />
		</div>
	</div>
	<div
		class="fetature-cards-container container-xl d-flex justify-content-between align-items-center"
	>
		<FeatureCard title="Realiable" imgSrc="/images/reliable.svg" />
		<FeatureCard title="Fast Search" imgSrc="/images/search.svg" />
		<FeatureCard title="Easy Booking" imgSrc="/images/easy-book.svg" />
	</div>

	<div
		class="heading-container container-xl d-flex justify-content-center align-items-start"
	>
		<Heading heading="Our Courses" color="#4E32BA" fontSize="60px" />
	</div>

	<div class="container-xl d-flex justify-content-between align-items-start">
		<LanguageFilterCard language="All" @click="select(this)" />
		<LanguageFilterCard language="English" />
		<LanguageFilterCard language="French" />
	</div>

	<div class="container-xl d-flex justify-content-start align-items-start">
		<select
			class="select-level form-select w-30"
			aria-label="Default select example"
		>
			<option value="">Select Your Level</option>
			<option value="Beginner">Beginner</option>
			<option value="Intermediate">Intermediate</option>
			<option value="Advanced">Advanced</option>
		</select>
	</div>
</template>

<script setup>
	import FeatureCard from "@/components/FeatureCard.vue";
	import Heading from "@/components/Heading.vue";
	import LanguageFilterCard from "@/components/LanguageFilterCard.vue";

	function select(el) {
		console.log(el);
	}
</script>

<style scoped>
	.container-fluid {
		display: flex;
		justify-content: center;
		padding: 0;
		height: fit-content;
	}

	.w-30 {
		width: 360px;
	}

	.hero-img-container {
		height: fit-content;
	}

	.hero-img-container img {
		width: 100%;
		height: 100%;
	}

	.fetature-cards-container {
		height: 230px;
		/* background: green; */
		margin-top: -120px;
		font-family: "Gilroy";
	}

	.heading-container {
		margin-top: 20px;
		width: 100%;
	}

	.select-level {
		color: #15074d;
	}
</style>
