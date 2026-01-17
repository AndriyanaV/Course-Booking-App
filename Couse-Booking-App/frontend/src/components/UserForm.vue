<template>
	<div class="lg:w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<Form :validation-schema="schema"  @submit="handleUserChange" class="form-layout">

				<!-- First and Last Name -->
				<div class="form-row">
					<div class="column">
						<label for="firstName" class="label-form">
							First Name <span class="span-required">*</span>
						</label>
						<!-- We need name to connect it with schema and v-model for edit mode initial value -->
						<Field name="firstName" v-model="formValues.firstName" type="text" class="input-el"
							id="firstName" />
						<ErrorMessage name="firstName" class="error-form-message " />
					</div>
					<div class="column">
						<label for="lastName" class="label-form">
							Last Name <span class="span-required">*</span>
						</label>
						<!-- We need name to connect it with schema and v-model for edit mode initial value -->
						<Field name="lastName" v-model="formValues.lastName" type="text" class="input-el"
							id="lastName" />
						<ErrorMessage name="lastName" class="error-form-message " />
					</div>
				</div>

				<!-- Password and Retype - only for add mode -->
				<div class="form-row">
					<div class="column" v-if="isAddMode">
						<label for="password" class="label-form">
							Password <span class="span-required">*</span>
						</label>
						<Field name="password" v-model="formValues.password" type="password" class="input-el"
							id="password" />
						<ErrorMessage name="password" class="error-form-message " />
					</div>
					<div class="column" v-if="isAddMode">
						<label for="retypePassword" class="label-form">
							Confirm password <span class="span-required">*</span>
						</label>
						<Field name="retypePassword" v-model="formValues.retypePassword" type="password"
							class="input-el" id="retypePassword" />
						<ErrorMessage name="retypePassword" class="error-form-message " />
					</div>

				</div>

				<!-- Email and phone number -->
				<div class="form-row">
					<div class="column">
						<label for="email" class="label-form">
							Email <span class="span-required">*</span>
						</label>
						<Field name="email" v-model="formValues.email" type="email" class="input-el"
							id="email" />
						<ErrorMessage name="email" class="error-form-message " />
					</div>
					<div class="column">
						<label for="phoneNumber" class="label-form">
							Phone Number <span class="span-required">*</span>
						</label>
						<Field name="phoneNumber" v-model="formValues.phoneNumber" type="phoneNumber" class="input-el"
							id="phoneNumber" />
						<ErrorMessage name="phoneNumber" class="error-form-message " />
					</div>
				</div>

				<!-- Role -->
				<div class="form-row">
					<div class="column">
						<label for="role" class="label-form">
							Role <span class="text-red-500">*</span>
						</label>
						<Field name="role" as="select" v-model="formValues.role" class="h-[64px] bg-white border border-gray-300 text-black text-sm rounded-xl
                        focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5">
							<option value="" disabled>
								Choose a Role
							</option>

							<option v-for="role in roles" :key="role.value" :value="role.value">
								{{ role.label }}
							</option>
						</Field>
						<ErrorMessage name="role" class="error-form-message" />
					</div>
				</div>

				<div v-if="formValues.role == 'professor'" class="column">
					<label for="biography" class="label-form">Biography</label>
					<Field as="textarea" name="biography" rows="4" class="block p-2.5 w-full text-sm text-black bg-white rounded-lg border border-gray-300
         					focus:shadow-[0_0_0_3px_rgba(59,87,255,0.15)] focus:outline-none"
						placeholder="Write biography here..." />
					<ErrorMessage name="biography" class="error-form-message" />
				</div>

				<div class="w-full flex flex-col gap-[20px] justify-start align-start">
					<label class="label-form text-start">
						Image 
					</label>

					<!-- Use v-slot to control validation using vee-validate -->
					<Field name="image" v-slot="{ setValue, errorMessage }">
						<label
							class="flex flex-col items-center justify-center lg:w-[40%] w-full h-64 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 relative">
							<img v-if="imagePreview" :src="imagePreview" class="absolute max-h-[180px]" />

							<svg v-else class="w-8 h-8 mb-4 text-gray-500" xmlns="http://www.w3.org/2000/svg"
								fill="none" viewBox="0 0 20 16">
								<path stroke="currentColor" stroke-width="2" stroke-linecap="round"
									stroke-linejoin="round" d="M13 13h3a3 3 0 0 0 0-6h-.025
                  A5.56 5.56 0 0 0 16 6.5
                  5.5 5.5 0 0 0 5.207 5.021
                  C5.137 5.017 5.071 5 5 5
                  a4 4 0 0 0 0 8h2.167
                  M10 15V6m0 0L8 8m2-2 2 2" />
							</svg>

							<p class="text-sm text-gray-500">
								Click to upload or drag and drop
							</p>

							<input type="file" accept="image/png, image/jpeg" class="hidden"
								@change="(e) => onImageChange(e, setValue)" />
						</label>

						<p class="error-form-message text-start">{{ errorMessage }}</p>
					</Field>
				</div>

				<div class="w-full flex items-center justify-start mt-[20px]">
					<Button :text="buttonText" />
				</div>
			</Form>
		</div>
	</div>
</template>

<script setup>
import { ref, watch, computed } from "vue";
import { toast } from "vue3-toastify";
import Button from "./Button.vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";

const emit = defineEmits(["userChange"]);

const imagePreview = ref(null);

const props = defineProps({
	user: Object,
	buttonText: String,
	isAddMode: Boolean,
});

// Validation schema
 const schema = computed(() =>
  yup.object({
    firstName: yup.string().required("First name is required"),
    lastName: yup.string().required("Last name is required"),

    email: yup
      .string()
      .email("Invalid email format")
      .required("Email is required"),

    phoneNumber: yup
      .string()
      .required("Phone number is required"),

    role: yup
      .string()
      .oneOf(["user", "professor", "admin"], "Invalid role")
      .required("Role is required"),

    //ADD vs EDIT
    password: props.isAddMode
      ? yup
          .string()
          .required("Password is required")
          .min(6, "Password must be at least 6 characters")
      : yup.string().notRequired(),

    retypePassword: props.isAddMode
      ? yup
          .string()
          .required("Please confirm password")
          .oneOf([yup.ref("password")], "Passwords do not match")
      : yup.string().notRequired(),

    biography: yup.string().when("role", {
      is: "professor",
      then: (schema) =>
        schema
          .required("Biography is required for professors")
          .max(500, "Biography can be max 500 characters"),
      otherwise: (schema) => schema.notRequired(),
    }),

    // IMAGE
    image: yup
      .mixed()
      .nullable()
      .test(
        "fileType",
        "Only PNG and JPEG images are allowed",
        (file) => {
          if (!file) return true;
          return ["image/png", "image/jpeg"].includes(file.type);
        }
      )
      .test(
        "fileSize",
        "Image size should not exceed 2MB",
        (file) => {
          if (!file) return true;
          return file.size <= 2 * 1024 * 1024;
        }
      ),
  })
);

//Roles
const roles = [
	{ label: "User", value: "user" },
	{ label: "Professor", value: "professor" },
	{ label: "Admin", value: "admin" },
]

const formValues = ref({
	firstName: "",
	lastName: "",
	email: "",
	password: "",
	role: "",
	phoneNumber: "",
	biography: "",
	image: "",
	
});

watch(
	() => props.user, //  `user` prosleđuje kao prop
	(newUser) => {
		if (newUser) {
			formValues.value.firstName = newUser.first_name || "";
			formValues.value.lastName = newUser.last_name || "";
			formValues.value.email = newUser.email || "";
			formValues.value.role = newUser.rola || "";
			formValues.value.phoneNumber = newUser.phone_number || "";
			formValues.value.biography = newUser.biography || "";
			imagePreview.value = newUser.user_image_url || "";
			
		}
	},
	{ immediate: true } // Odmah prilikom inicijalizacije
);

const onImageChange = (event, setValue) => {
  const file = event.target.files[0];
  if (!file) return;

  //Importnat for schema 
  setValue(file);

  //Revoke previous object URL to avoid memory leaks
  if (imagePreview.value) {
    URL.revokeObjectURL(imagePreview.value);
  }

  // Set a new preview URL so the image can be displayed in the UI
  imagePreview.value = URL.createObjectURL(file);
};

const handleUserChange = (values) => {
	emit("userChange", values);
};
</script>

<style></style>