<template>
	<div
		class="w-[500px] bg-[rgba(239,239,239,0.45)] border-0 rounded-md gap-[20px] py-[10px] flex flex-col shadow-custom position-relative"
	>
		<div
			@click="
				$router.push({ name: 'UserProfileUpdate', query: { userId: user.id } })
			"
			class="w-[30px] h-[30px] cursor-pointer position-absolute right-[10px] top-[10px]"
		>
			<img src="/images/edit.png" class="w-full h-full" />
		</div>
		<div class="w-full flex justify-center py-[5px]">
			<div class="w-[100px] h-[100px] rounded-full">
				<img :src="userImage" class="w-full h-full rounded-full" />
			</div>
		</div>
		<div class="f-full flex flex-col items-center gap-[10px]">
			<label for="first_name" class="label-form"> First Name </label>
			<div class="w-[80%] bg-white rounded">
				<input
					v-model="firstName"
					class="w-full rounded h-[45px] text-center"
					type="text"
					readonly
				/>
			</div>
		</div>
		<div class="f-full flex flex-col items-center gap-[10px]">
			<label for="last_name" class="label-form"> Last Name </label>
			<div class="w-[80%] bg-white rounded">
				<input
					v-model="lastName"
					class="w-full rounded h-[45px] text-center"
					type="text"
					readonly
				/>
			</div>
		</div>
		<div class="f-full flex flex-col items-center gap-[10px]">
			<label for="email" class="label-form"> Email address </label>
			<div class="w-[80%] bg-white rounded">
				<input
					v-model="email"
					class="w-full rounded h-[45px] text-center"
					type="text"
					readonly
				/>
			</div>
		</div>
		<div class="f-full flex flex-col items-center gap-[10px]">
			<label for="pnumber" class="label-form"> Phone Number </label>
			<div class="w-[80%] bg-white rounded">
				<input
					v-model="pnumber"
					class="w-full rounded h-[45px] text-center"
					type="text"
					readonly
				/>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref, watch } from "vue";

	const props = defineProps({
		user: Object,
	});

	const firstName = ref("");
	const lastName = ref("");
	const email = ref("");
	const pnumber = ref("");
	const userImage = ref("");

	watch(
		() => props.user, // Pretpostavljam da se `user` prosleđuje kao prop
		(newUser) => {
			if (newUser) {
				firstName.value = newUser.first_name || "";
				lastName.value = newUser.last_name || "";
				email.value = newUser.email || "";
				pnumber.value = newUser.phone_number || "";
				userImage.value = newUser.user_image_url || "";
			}
		},
		{ immediate: true } // Odmah prilikom inicijalizacije
	);
</script>

<style>
</style>