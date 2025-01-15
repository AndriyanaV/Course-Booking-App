<template>
	<!-- <div class="col-12 col-md-4 mb-4"> -->
	<div
		class="card d-flex flex-column justify-content-center align-items-start"
		style="width: 413px"
	>
		<div class="course-img-container">
			<img src="/images/english-language-course.png" />
		</div>
		<div
			class="level-language-container d-flex justify-content-center align-items-center"
		>
			<div class="level-container">
				<p>Begginer</p>
			</div>
			<div class="language-container">
				<h4>English Language</h4>
			</div>
		</div>

		<div class="language-description">
			<div class="duration">
				<div class="week-img-container"><img src="/images/clock.svg" /></div>
				<p>Weeks</p>
			</div>
			<div class="duration">
				<div class="week-img-container"><img src="/images/clock.svg" /></div>
				<p>Lessons</p>
			</div>
			<div class="duration">
				<div class="week-img-container"><img src="/images/clock.svg" /></div>
				<p>Start</p>
			</div>
		</div>

		<div class="buttons-container">
			<button type="button" class="btn btn-primary">Primary</button>
			<button type="button" class="btn btn-info">Info</button>
			<div class="price-container"><span> $430 </span></div>
		</div>
	</div>
</template>

<script setup>
</script>

<style scoped>
	.card {
		border-radius: 10px;
		background: #efefef;
		border: none;
		gap: 20px;
	}

	.course-img-container {
		width: 100%;
		height: 270px;
	}

	.course-img-container img {
		width: 100%;
		height: 100%;
	}

	.level-language-container {
		gap: 40px;
		height: 64px;
		width: 100%;
		align-items: center;
	}

	.level-container {
		width: 27%;
		height: 70%;
		box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.25);
		text-align: center;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #252525;
		font-size: 16px;
	}

	.language-container {
		width: 57%;
		display: flex;
		justify-content: center;
		align-items: center;
	}

	h4 {
		color: black;
		font-size: 20px;
		font-family: "Gilroy";
		font-weight: 600;
	}

	.language-description {
		width: 100%;
		color: #a2a2a2;
		font-size: 16px;
		display: flex;
		justify-content: center;
		gap: 56px;
	}

	.duration {
		display: flex;
		gap: 4px;
		width: 85px;
		height: 55px;
	}

	.week-img-container {
		width: 28px;
		height: 28px;
	}

	.week-img-container img {
		width: 100%;
		height: 100%;
	}

	.buttons-container {
		padding: 0px 19px;
		display: flex;
		width: 100%;
		justify-content: space-between;
		height: 64px;
	}

	.buttons-container button {
		width: 120px;
		height: 42px;
	}

	.price-container {
		width: 75px;
		height: 42px;
		color: #00000e;
		font-size: 16px;
		display: flex;
		align-items: center;
		font-size: 16px;
		border: 1px solid #c5c5c5;
		justify-content: center;
	}

	.price-container p {
		font-size: 16px;
		font-weight: 600px;
	}
</style>