<template>
	<div class="flex w-[1100px] flex-col justify-start items-center gap-[10px]">
		<div class="title-desc">
			<div class="title">
				<p>Ime</p>
			</div>
			<div class="description">
				<p>{{ user.first_name }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Last Name</p>
			</div>
			<div class="description">
				<p>{{ user.last_name }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>email</p>
			</div>
			<div class="description">
				<p class="lowercase">{{ user.email }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Phone Number</p>
			</div>
			<div class="description">
				<p>{{ user.phone_number }}</p>
			</div>
		</div>

		<div class="title-desc">
			<div class="title">
				<p>Rola</p>
			</div>
			<div class="description">
				<p>{{ user.rola }}</p>
			</div>
		</div>
		<div class="w-full h-[350px] flex rounded-sm">
			<div
				class="w-[40%] flex items-center justify-start h-full flex-col rounded-sm"
			>
				<div
					class="w-full h-[90px] bg-[#9989B4] text-[#FFFF] flex flex-col items-center justify-center font-medium text-[32px] font-gilroy rounded-sm"
				>
					<p>Photo</p>
				</div>
				<div class="w-full h-[250px] rounded-sm">
					<img :src="user.user_image_url" class="w-full h-full rounded-b-sm" />
				</div>
			</div>
			<div
				class="w-[60%] h-[350px] flex flex-col rounded-bl-md rounded-br-md rounded-sm"
			>
				<div
					class="w-full h-[90px] flex bg-white justify-center items-center text-[24px] font-gilroy font-normal text-[#A49D9D] rounded-l-lg-md rounded-sm"
				>
					<p v-if="user.rola == 'professor'">Biography</p>
				</div>
				<div
					class="w-full h-[250px] bg-white text-[18px] font-gilroy font-normal text-[#A49D9D] px-[40px] rounded-sm"
				>
					<p>{{ user.biography }}</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	const props = defineProps({
		user: Object,
	});
</script>

<style>
</style>