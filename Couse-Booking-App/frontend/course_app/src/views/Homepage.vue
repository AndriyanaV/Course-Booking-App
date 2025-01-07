<template>
	<div class="container-fluid">
		<div class="hero-img-container">
			<img src="/images/Hero-img.svg" />
		</div>
	</div>
	<div class="container-xl d-flex justify-content-around align-items-center">
		<FeatureCard title="Realiable" imgSrc="/images/reliable.svg" />
		<FeatureCard title="Fast Search" imgSrc="/images/search.svg" />
		<FeatureCard title="Easy Booking" imgSrc="/images/easy-book.svg" />
	</div>
</template>

<script setup>
	// console.log(document.getElementsByClassName("container-fluid"));
	import FeatureCard from "@/components/FeatureCard.vue";
</script>

<style scoped>
	.container-fluid {
		display: flex;
		justify-content: center;
		padding: 0;
		height: 900px;
	}

	.hero-img-container {
		width: 100vh;
		height: 100%;
		padding: 0px;
		/* background: url("/images/Hero-img.svg");
																														background-position: center;
																														background-size: cover;
																														background-repeat: no-repeat; */
		width: 100%;
		height: 100%;
	}

	.hero-img-container img {
		width: 100%;
	}

	.container-xl {
		height: 230px;
		/* background: green; */
	}
</style>
