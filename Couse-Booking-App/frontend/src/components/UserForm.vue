<template>
	<div class="w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<form class="w-full" @submit.prevent="handleUserChange()">
				<div class="form-row w-full flex gap-[20px] h-[140px]">
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="name"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							First Name <span class="text-red-500"> * </span>
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="form.firstName"
								type="text"
								placeholder="Enter your first name"
								class="w-full rounded-xl h-full border pl-[10px]"
								required
							/>
						</div>
					</div>
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="last_name"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							Last Name <span class="text-red-500"> * </span>
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="form.lastName"
								type="text"
								placeholder="Enter your last name"
								class="w-full rounded-xl h-full border pr-[5px] pl-[10px]"
								required
							/>
						</div>
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label v-if="isAddMode" for="password" class="label-form">
							Password <span class="text-red-500"> * </span></label
						>
						<label v-else for="password" class="label-form"> Password </label>
						<div class="input-container">
							<input
								v-model="form.password"
								type="password"
								placeholder="******"
								class="input-el"
								:required="isAddMode"
							/>
						</div>
					</div>
					<div class="column">
						<label for="email" class="label-form">
							Email <span class="text-red-500"> * </span></label
						>
						<div class="input-container">
							<input
								v-model="form.email"
								type="email"
								placeholder="Enter your email address"
								class="input-el"
								required
							/>
						</div>
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="phumber" class="label-form"> Phone Number </label>
						<div class="input-container">
							<input
								v-model="form.phoneNumber"
								type="tel"
								placeholder="Enter your phone number"
								class="input-el"
							/>
						</div>
					</div>
					<div class="column">
						<label for="email" class="label-form">
							Rola <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<select
								v-model="form.rola"
								class="h-[64px] bg-white border border-gray-300 text-black text-sm  rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
								required
							>
								<option selected disabled>Choose a Role</option>
								<option value="user">User</option>
								<option value="professor">Professor</option>
								<option value="admin">Admin</option>
							</select>
						</div>
					</div>
				</div>
				<div
					v-if="form.rola == 'professor'"
					class="form-row flex-col mb-[20px]"
				>
					<label for="message" class="label-form">Biography</label>
					<textarea
						id="message"
						v-model="form.biography"
						rows="4"
						class="block p-2.5 w-full text-sm text-black bg-white rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
						placeholder="Write your biography here..."
					></textarea>
				</div>

				<div
					class="image-cotainer w-full flex flex-col gap-[20px] h-[290px] pr-[20px]"
				>
					<label
						for="image"
						class="text-[#14003B] text-[18px] font-filroy font-medium"
						>Image</label
					>
					<div class="w-full h-[200px]">
						<div class="flex items-center justify-start w-full">
							<label
								for="dropzone-file"
								class="flex flex-col items-center justify-center w-[40%] h-64 border border-gray-200 border-solid rounded-lg cursor-pointer bg-white dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
							>
								<div
									class="flex flex-col items-center justify-center pt-5 pb-6 realtive"
								>
									<div v-if="form.imagePreview">
										<img
											:src="form.imagePreview"
											alt="Image preview"
											style="max-width: 200px"
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
									<p
										class="mb-2 text-sm text-gray-500 dark:text-gray-400 pt-[20px]"
									>
										<span class="font-semibold">Click to upload</span> or drag
										and drop
									</p>
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

				<div class="w-full h-[100px] flex items-center justify-start mt-[20px]">
					<div class="h-[50px] w-[150px]">
						<button
							type="submit"
							class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full w-[150px]"
						>
							{{ text }}
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
	import { ref, watch } from "vue";
	import { toast } from "vue3-toastify";

	const emit = defineEmits(["userChange"]);

	const props = defineProps({
		user: Object,
		text: String,
		isAddMode: Boolean,
	});

	const form = ref({
		firstName: "",
		lastName: "",
		email: "",
		password: "",
		rola: "",
		phoneNumber: "",
		biography: "",
		image: "",
		imagePreview: "",
	});

	watch(
		() => props.user, //  `user` prosleđuje kao prop
		(newUser) => {
			if (newUser) {
				form.value.firstName = newUser.first_name || "";
				form.value.lastName = newUser.last_name || "";
				form.value.email = newUser.email || "";
				form.value.rola = newUser.rola || "";
				form.value.phoneNumber = newUser.phone_number || "";
				form.value.biography = newUser.biography || "";
				form.value.imagePreview = newUser.user_image_url || ""; // Ako je slika prisutna u user objektu
			}
		},
		{ immediate: true } // Odmah prilikom inicijalizacije
	);

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

	const handleUserChange = () => {
		if (
			!form.value.firstName ||
			!form.value.lastName ||
			!form.value.email ||
			!form.value.rola ||
			(props.isAddMode && !form.value.password)
		) {
			toast.error("Enter all require fields.");
			return;
		}

		emit("userChange", form.value);
	};
</script>

<style>
</style>