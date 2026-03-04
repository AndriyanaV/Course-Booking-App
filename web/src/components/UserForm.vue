<template>
	<!-- Loader -->
	<div v-show="loading" class="w-full flex justify-center items-center h-full">
    <Loader />
  </div>

  <!-- Form -->
	<div v-show="!loading" class="lg:w-[1200px] h-auto bg-white py-[20px] lg:px-[40px] px-[20px] rounded-[14px]">
		<div class="form wraper w-full flex flex-col gap-[40px]">

			<Form ref="userForm" :validation-schema="schema" :initial-values="initialValues" @submit="handleUserChange"
				class="form-layout">

				<!-- First and Last Name -->
				<div class="form-row">
					<div class="column">
						<label for="firstName" class="label-form">First Name <span
								class="span-required">*</span></label>
						<Field name="firstName" type="text" class="input-el" id="firstName" />
						<ErrorMessage name="firstName" class="error-form-message" />
					</div>
					<div class="column">
						<label for="lastName" class="label-form">Last Name <span class="span-required">*</span></label>
						<Field name="lastName" type="text" class="input-el" id="lastName" />
						<ErrorMessage name="lastName" class="error-form-message" />
					</div>
				</div>

				<!-- Passwords only in add mode -->
				<div class="form-row" v-if="isAddMode">
					<div class="column">
						<label for="password" class="label-form">Password <span class="span-required">*</span></label>
						<Field name="password" type="password" class="input-el" id="password" />
						<ErrorMessage name="password" class="error-form-message" />
					</div>
					<div class="column">
						<label for="retypePassword" class="label-form">Confirm Password <span
								class="span-required">*</span></label>
						<Field name="retypePassword" type="password" class="input-el" id="retypePassword" />
						<ErrorMessage name="retypePassword" class="error-form-message" />
					</div>
				</div>

				<!-- Email, Phone, Role -->
				<div class="form-row">
					<div class="column">
						<label for="email" class="label-form">Email <span class="span-required">*</span></label>
						<Field name="email" type="email" class="input-el" id="email" />
						<ErrorMessage name="email" class="error-form-message" />
					</div>
					<div class="column">
						<label for="phoneNumber" class="label-form">Phone Number </label>
						<Field name="phoneNumber" type="text" class="input-el" id="phoneNumber" />
						<ErrorMessage name="phoneNumber" class="error-form-message" />
					</div>
				</div>

				<!-- Role -->
				<div class="form-row">
					<div class="column">
						<label for="role" class="label-form">Role <span class="span-required">*</span></label>
						<Field name="role" as="select"
							class="input-el h-[64px] bg-white border border-gray-300 text-black text-sm rounded-xl p-2.5">
							<option value="" disabled>Choose a Role</option>
							<option v-for="role in roles" :key="role.value" :value="role.value">{{ role.label }}
							</option>
						</Field>
						<ErrorMessage name="role" class="error-form-message" />
					</div>
				</div>

				<!-- Biography -->
				<Field name="role" v-slot="{ value }">
					<div v-if="value === 'professor'" class="column">
						<label class="label-form">Biography</label>
						<Field as="textarea" name="biography" rows="4" class="input-el" />
						<ErrorMessage name="biography" class="error-form-message" />
					</div>
				</Field>

				<!-- Image -->
				<div class="w-full flex flex-col gap-[20px] justify-start align-start">
					<label class="label-form text-start">Image</label>
					<Field name="image" v-slot="{ setValue, errorMessage }">
						<label
							class="flex flex-col items-center justify-center lg:w-[40%] w-full h-64 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 relative">
							<img v-if="imagePreview" :src="imagePreview" class="absolute max-h-[180px]" />

							<svg v-else class="w-8 h-8 mb-4 text-gray-500" xmlns="http://www.w3.org/2000/svg"
								fill="none" viewBox="0 0 20 16">
								<path stroke="currentColor" stroke-width="2" stroke-linecap="round"
									stroke-linejoin="round" d="M13 13h3a3 3 0 0 0 0-6h-.025 A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021
                  C5.137 5.017 5.071 5 5 5 a4 4 0 0 0 0 8h2.167 M10 15V6m0 0L8 8m2-2 2 2" />
							</svg>

							<p class="text-sm text-gray-500">Click to upload or drag and drop</p>

							<input type="file" accept="image/png, image/jpeg" class="hidden" @change="(e) => {
								setValue(e.target.files[0]);
								setFile(e.target.files[0]);
							}" />
							<button v-if="imagePreview" type="button"
								class=" absolute top-2 right-2 bg-white/90 hover:bg-white text-gray-700 rounded-full p-1 shadow"
								@click.stop="removeImage(setValue)">
								<svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24"
									stroke="currentColor" stroke-width="2">
									<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
								</svg>
							</button>
						</label>
						<p class="error-form-message text-start">{{ errorMessage }}</p>
					</Field>

				</div>

				<!-- Submit button -->
				<!-- Submit button -->
				<div class="custom-button-container">
					<button type="submit" class="custom-button">
						{{ buttonText }}
					</button>
				</div>

			</Form>
		</div>
	</div>
</template>


<script setup>
import { ref, watch } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import Loader from "@/components/Loader.vue";
import { userSchema } from "@/validation/userSchema.js";
import { useImagePreview } from "@/composables/useImagePreview";
import { ROLES } from "@/constants/roles";

const props = defineProps({
	user: Object,
	buttonText: String,
	isAddMode: Boolean,
	loading: {
		type: Boolean,
		required: false,
		default: false
	}
});

const emit = defineEmits(["userChange"]);

const userForm = ref(null);
const { preview: imagePreview, setFile } = useImagePreview();

const schema = userSchema(props.isAddMode, imagePreview);


const removeImage = (setValue
) => {
	imagePreview.value = null
	setValue(null)

	// Reset file input to solve problem when we remove image and try to add it again 
	const inputEl = document.querySelector('input[type="file"]');
	if (inputEl) inputEl.value = "";
}

// roles
const roles = ROLES

watch(
	() => props.user,
	(newUser) => {
		if (!newUser || !userForm.value) return;

		userForm.value.setValues({
			firstName: newUser.first_name || "",
			lastName: newUser.last_name || "",
			email: newUser.email || "",
			role: newUser.rola || "",
			phoneNumber: newUser.phone_number || "",
			biography: newUser.biography || "",
			image: null,
		});

		imagePreview.value = newUser.user_image_url || null;
	},
	{ immediate: true }
);

const handleUserChange = (values) => {
	console.log(values)
	emit("userChange", values);
};
</script>

<style></style>