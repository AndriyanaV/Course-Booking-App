<template>
	<div class="lg:w-[450px] flex flex-col items-start justify-start text-center gap-[40px]">
		<!-- <Heading heading="My Profile" color="#2E42BE" class="w-full font-bold" fontSize="32" /> -->
		<div
			class="user-form-container">
			<div @click="
				$router.push({ name: 'UserProfileUpdate', query: { userId: user.id } })
				" class="lg:w-[25px] lg:h-[25px] w-[24px] h-[24px] cursor-pointer absolute right-[10px] top-[10px]">
				<img src="/images/pencil.svg" class="w-full h-full" />
			</div>
			<div class="w-full flex justify-start py-[5px]">
				<div class="w-[100px] h-[100px] rounded-full">
					<img :src="userImage" class="w-full h-full rounded-full" />
				</div>
			</div>
			<div class="user-input-container">
				<label for="first_name" class="label-form"> First Name </label>
				<input v-model="firstName" class="user-input" type="text" readonly />
			</div>
			<div class="user-input-container">
				<label for="last_name" class="label-form"> Last Name </label>
				<input v-model="lastName" class="user-input" type="text" readonly />
			</div>
			<div class="user-input-container">
				<label for="email" class="label-form"> Email address </label>
				<input v-model="email" class="user-input" type="text" readonly />
			</div>
			<div class="user-input-container">
				<label for="pnumber" class="label-form"> Phone Number </label>
				<input v-model="pnumber" class="user-input" type="text" readonly />
			</div>
		</div>
	</div>

</template>

<script setup>
import { ref, watch } from "vue";
import Heading from "./Heading.vue";


const props = defineProps({
	user: Object,
});

const firstName = ref("");
const lastName = ref("");
const email = ref("");
const pnumber = ref("");
const userImage = ref("");

watch(
	() => props.user, 
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

<style></style>