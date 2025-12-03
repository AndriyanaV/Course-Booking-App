<template>
	<div class="w-[100%] flex items-center h-full rounded-xl  justify-center">
		<div class=" w-[100%] h-full flex items-center justify-center">
			<div class="flex felx-col h-[100%] w-[95%] ">
				<div class=" w-full">
					<div class="flex flex-col items-center justify-center h-[100%] px-6 py-8 mx-auto lg:py-0">
						<div class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0">

							<div class="p-6 space-y-4 md:space-y-6 sm:p-8 flex flex-col lg:gap-[20px] gap-[16px]">
								<div v-if="serverMessage" class="w-full h-fit flex items-center gap-[16px] text-gray-600">
									<div class="w-1/2 flex flex-col gap-2">
										<h4 class="m-0 font-bold">HMM!</h4>
										<p>{{serverMessage}}</p>
									</div>
									<div class="w-1/2 h-[140px] flex flex-col gap-2"><img src="/images/emoji.png" class="w-full h-full object-contain" /></div>
								</div>
								<h1
									class="text-xl  leading-tight tracking-tight text-medium-purple md:text-2xl  font-bold">
									Sign in to your account
								</h1>
								<form class="space-y-6 md:space-y-6 flex flex-col lg:gap-[20px] gap-[16px] !mt-0"
									action="#" @submit.prevent="handleSubmit">
									<div class="flex flex-col gap-[12px]">
										<label for="email" class="block mb-2 text-base font-medium text-dark-purple ">
											Email</label>
										<div class="w-full flex flex-col gap-[8px]">
											<input v-model="email" type="text" name="email" id="email"
												class="bg-[#EFEFEF] text-[#A5A4A4] rounded-lg block placeholder:text-sm  p-2.5 focus:shadow-[0_0_0_3px_rgba(59,87,255,0.15)] focus:outline-none w-full"
												placeholder="myemail@gmail.com" @input="emailMessage = false" />
											<p v-if="emailMessage" class="error-message">{{ emailNotice }}</p>
										</div>
									</div>
									<div class="flex flex-col gap-[12px] m-0 !mt-0">
										<label for="password"
											class="block  text-base font-medium text-dark-purple  mt-0 ">Password</label>
										<div class="w-full flex flex-col gap-[8px]">
											<input v-model="password" type="password" name="password" id="password"
												placeholder="••••••••"
												class="bg-[#EFEFEF] text-[#A5A4A4] rounded-lg block  p-2.5 focus:shadow-[0_0_0_3px_rgba(59,87,255,0.15)] focus:outline-none w-full"
												@input="passwordMessage = false" />
											<p v-if="passwordMessage" class="error-message">Please enter your password.
											</p>
										</div>
									</div>

									<div class="w-full flex flex-col gap-[10px] !mt-0">
										<button type="submit" class="w-full !mt-[10px] text-white 
               													bg-gradient-to-br from-[#7786EB] to-[#7786EB] 
               													hover:to-[#7F8BF0]
               													transition-all duration-500 ease-in-out
               													focus:outline-none focus:ring-primary-300 
               													font-bold rounded-[10px] text-[16px] px-5 py-2.5 text-center capitalize">
											Sign in
										</button>
										<p class="text-sm font-light text-gray-500 ">
											Don’t have an account yet?
											<a href="#"
												class="font-medium text-primary-600 hover:underline !hover:bg-none ">Sign
												up</a>
										</p>
									</div>
								</form>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, defineProps } from "vue";

defineProps({
  serverMessage: {
    type: String,
    default: null
  }
});

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const email = ref("");
const emailNotice = ref("")
const password = ref("");
const emailMessage = ref(false);
const passwordMessage = ref(false);

const emit = defineEmits(["login"]);

function handleSubmit() {
	if (!email.value || !emailRegex.test(email.value)) {
		emailMessage.value = true;

		emailNotice.value = !email.value
			? 'Please enter your email.'
			: 'Invalid email format';

		return;
	}

	if (!password.value) {
		passwordMessage.value = "Please enter your password";
		return;
	}

	emit("login", { email: email.value, password: password.value });
}
</script>

<style></style>