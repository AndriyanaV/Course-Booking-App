<template>
	<div
		class="w-[500px] bg-[rgba(239,239,239,0.45)] border-0 rounded-md shadow-custom position-relative"
	>
		<form
			@submit.prevent="updateUserProfile()"
			class="w-full h-full gap-[20px] py-[20px] flex flex-col"
		>
			<div
				class="image-cotainer w-full flex flex-col gap-[20px] h-[290px] pr-[20px]"
			>
				<label for="image" class="label-form w-full text-center">Image</label>
				<div class="w-full h-[200px]">
					<div class="flex items-center justify-center w-full">
						<label
							for="dropzone-file"
							class="flex flex-col items-center justify-center w-[40%] h-64 border-2 border-gray-300 border-solid rounded-lg cursor-pointer bg-white dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
						>
							<div
								class="flex flex-col items-center justify-center pt-5 pb-6 realtive"
							>
								<div v-if="form.imagePreview">
									<img
										:src="form.imagePreview"
										alt="Image preview"
										style="max-width: 100px"
										class="aboslute top-0"
									/>
								</div>
								<svg
									class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400 absolute"
									aria-hidden="true"
									xmlns="http://www.w3.org/2000/svg"
									fill="none"
									viewBox="0 0 20 16"
								>
									<path
										stroke="currentColor"
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
									/>
								</svg>
								<p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
									<span class="font-semibold">Click to upload</span> or drag and
									drop
								</p>
								<!-- <p class="text-xs text-gray-500 dark:text-gray-400">
										SVG, PNG, JPG or GIF (MAX. 800x400px)
									</p> -->
							</div>
							<input
								id="dropzone-file"
								type="file"
								class="hidden"
								@change="handleFileChange"
							/>
						</label>
					</div>
				</div>
			</div>
			<div class="w-full flex justify-center py-[5px]"></div>
			<div class="f-full flex flex-col items-center gap-[10px]">
				<label for="first_name" class="label-form">
					First Name <span class="text-red-500"> * </span></label
				>
				<div class="w-[80%] bg-white rounded">
					<input
						v-model="form.firstName"
						class="w-full rounded h-[45px] text-center"
						type="text"
					/>
				</div>
			</div>
			<div class="f-full flex flex-col items-center gap-[10px]">
				<label for="last_name" class="label-form">
					Last Name <span class="text-red-500"> * </span>
				</label>
				<div class="w-[80%] bg-white rounded">
					<input
						v-model="form.lastName"
						class="w-full rounded h-[45px] text-center"
						type="text"
					/>
				</div>
			</div>
			<div class="f-full flex flex-col items-center gap-[10px]">
				<label for="email" class="label-form">
					Email address <span class="text-red-500"> * </span>
				</label>
				<div class="w-[80%] bg-white rounded">
					<input
						v-model="form.email"
						class="w-full rounded h-[45px] text-center"
						type="text"
					/>
				</div>
			</div>
			<div class="f-full flex flex-col items-center gap-[10px]">
				<label for="pnumber" class="label-form"> Phone Number </label>
				<div class="w-[80%] bg-white rounded">
					<input
						v-model="form.pnumber"
						class="w-full rounded h-[45px] text-center"
						type="text"
					/>
				</div>
			</div>
			<div class="w-full h-[100px] flex items-center justify-center">
				<div class="h-[50px] w-[150px]">
					<button
						type="submit"
						class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full w-[150px]"
					>
						Update
					</button>
				</div>
			</div>
		</form>
	</div>
</template>

<script setup>
	import { ref, watch } from "vue";
	import { toast } from "vue3-toastify";

	const props = defineProps({
		user: Object,
	});

	const emit = defineEmits(["userProfileUpdated"]);

	const form = ref({
		firstName: "",
		lastName: "",
		email: "",
		pnumber: "",
		image: "",
		imagePreview: "",
	});

	const handleFileChange = (event) => {
		const file = event.target.files[0];
		if (!file) {
			form.value.image = null;
			form.value.imagePreview = null;
			return;
		}
		if (!file.type.startsWith("image/")) {
			toast.error("Please upload a valid image file!");
			return;
		}
		form.value.image = file;
		form.value.imagePreview = URL.createObjectURL(file);
	};

	watch(
		() => props.user, // Pretpostavljam da se `user` prosleđuje kao prop
		(newUser) => {
			if (newUser) {
				form.value.firstName = newUser.first_name || "";
				form.value.lastName = newUser.last_name || "";
				form.value.email = newUser.email || "";
				form.value.pnumber = newUser.phone_number || "";
				form.value.userImage = newUser.user_image_url || "";
				form.value.imagePreview = newUser.user_image_url;
			}
		},
		{ immediate: true } // Odmah prilikom inicijalizacije
	);

	const updateUserProfile = () => {
		if (!form.value.firstName || !form.value.lastName || !form.value.email) {
			toast.error("Enter all required fields.");
			return;
		}
		emit("userProfileUpdated", form.value);
	};
</script>

	


<style>
</style>