<template>
	<div
		class="flex flex-column justify-center items-start rounded-lg bg-[rgba(239,239,239,0.80)] border-0 gap-[20px] w-[413px] pb-[20px]"
	>
		<div class="w-full h-[270px] m-0">
			<img src="/images/english-language-course.png" class="h-full w-full" />
		</div>
		<div
			class="flex items-center justify-center gap-[40px] h-[64px] w-full py-[10px] pl-[19px]"
		>
			<div
				class="w-[115px] h-[45px] shadow-[2px_2px_5px_rgba(0,_0,_0,_0.25)] text-center flex items-center justify-center text-[#252525] text-[16px]"
			>
				<p>Begginer</p>
			</div>
			<div class="w-[57%] flex justify-center h-full items-center">
				<h4 class="text-black text-[20px] font-gilroy font-semibold">
					English Language
				</h4>
			</div>
		</div>

		<div
			class="w-full text-[#a2a2a2] text-[16px] flex justify-between px-[20px] h-[55px]"
		>
			<div
				class="flex w-[85px] mh-[55px] gap-[8px] flex items-center justify-center"
			>
				<div class="w-[28px] h-[28px]">
					<img src="/images/clock.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">Weeks</p>
			</div>
			<div
				class="flex w-[85px] mh-[55px] gap-[8px] flex items-center justify-center"
			>
				<div class="week-img-container">
					<img src="/images/clock.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">Lessons</p>
			</div>
			<div
				class="flex w-[85px] mh-[55px] gap-[8px] flex items-center justify-center"
			>
				<div class="week-img-container">
					<img src="/images/clock.svg" class="w-full h-full" />
				</div>
				<p class="text-[16px]">Start</p>
			</div>
		</div>

		<div class="px-[19px] flex w-full justify-between h-16">
			<button
				class="bg-[#06088C] hover:bg-blue-700 text-white font-medium py-2 px-4 border border-blue-700 rounded h-[42px]"
			>
				Book Now
			</button>
			<button
				class="bg-[#EFEFEF] hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded h-[42px]"
			>
				More Info
			</button>
			<div
				class="text-[16px] font-bold w-[75px] text-[#00000e] text-[16px] flex items-center justify-center border border-[#c5c5c5] h-[42px]"
			>
				<span class="font-bold"> $430 </span>
			</div>
		</div>
	</div>
</template>

<script setup>
</script>

<style scoped>
	/* .card {
																																																											border-radius: 10px;
																																																											background: #efefef;
																																																											border: none;
																																																											gap: 20px;
																																																										}

																																																										.course-img-container {
																																																											width: 100%;
																																																											height: 270px;
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
																																																										} */
</style>