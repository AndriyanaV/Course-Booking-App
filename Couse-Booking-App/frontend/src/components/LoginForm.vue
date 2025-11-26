<template>
	<div
		class="w-[100%] flex items-center h-[688px] rounded-xl bg-white justify-center"
	>
		<div class="w-[50%] h-full flex items-center justify-center">
			<div class="flex felx-col h-[100%] w-[95%] bg-black">
				<section class="bg-white w-full">
					<div
						class="flex flex-col items-center justify-center h-[100%] px-6 py-8 mx-auto lg:py-0"
					>
						<div
							class="w-full bg-white rounded-lg shadow md:mt-0 sm:max-w-md xl:p-0"
						>
							<div class="p-6 space-y-4 md:space-y-6 sm:p-8">
								<h1
									class="text-xl font-bold leading-tight tracking-tight text-[#4E32BA] md:text-2xl  font-bold"
								>
									Sign in to your account
								</h1>
								<form
									class="space-y-4 md:space-y-6"
									action="#"
									@submit.prevent="handleSubmit()"
								>
									<div>
										<label
											for="email"
											class="block mb-2 text-base font-medium text-[#4E32BA] "
											>Your Email</label
										>
										<input
											v-model="email"
											type="email"
											name="email"
											id="email"
											class="bg-[#EFEFEF] text-[#A5A4A4] rounded-lg block w-full p-2.5"
											placeholder="myemail@gmail.com"
											required=""
										/>
									</div>
									<div>
										<label
											for="password"
											class="block mb-2 text-base font-medium text-[#4E32BA] "
											>Password</label
										>
										<input
											v-model="password"
											type="password"
											name="password"
											id="password"
											placeholder="••••••••"
											class="bg-[#EFEFEF] text-[#A5A4A4] rounded-lg block w-full p-2.5"
											required=""
										/>
									</div>

									<button
										type="submit"
										class="w-full mb-4 text-white bg-[#4E32BA] hover:[#2E158E] focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center  capitalize"
									>
										Sign in
									</button>
									<p class="text-sm font-light text-gray-500 ml-0.5">
										Don’t have an account yet?
										<a
											href="#"
											class="font-medium text-primary-600 hover:underline dark:text-primary-500"
											>Sign up</a
										>
									</p>
								</form>
							</div>
						</div>
					</div>
				</section>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref } from "vue";
	import { toast } from "vue3-toastify";

	const email = ref("");
	const password = ref("");
	const message = ref("");

	const emit = defineEmits(["login"]);

	function handleSubmit() {
		if (email.value == "") {
			message.value = "Please enter your email.";
			toast.error(message.value);
			return;
		}

		if (password.value == "") {
			message.value = "Please enter your password";
			toast.error(message.value);
			return;
		}

		// console.log(e);

		emit("login", { email: email.value, password: password.value });
	}
</script>

<style>
</style>