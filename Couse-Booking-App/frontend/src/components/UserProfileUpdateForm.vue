<template>
  <div class="lg:w-[500px] flex flex-col gap-[40px]">
    <div class="user-form-container w-full">

      <Form
        :validation-schema="schema"
        @submit="updateUserProfile"
        class="w-full flex flex-col gap-[20px]"
      >

        <!-- IMAGE -->
        <div class="w-full flex flex-col gap-[10px]">
          <label class="label-form text-start">
            Image <span class="span-required">*</span>
          </label>

          <Field name="image" v-slot="{ setValue, errorMessage }">
            <label
              class="flex flex-col items-center justify-center lg:w-[40%] h-[200px]
                     border-2 border-gray-100 rounded-lg cursor-pointer hover:bg-gray-100 relative"
            >
              <img
                v-if="imagePreview"
                :src="imagePreview"
                class="absolute max-h-[120px]"
              />

              <svg
                v-else
                class="w-8 h-8 mb-4 text-gray-500"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 20 16"
              >
                <path
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M13 13h3a3 3 0 0 0 0-6h-.025
                  A5.56 5.56 0 0 0 16 6.5
                  5.5 5.5 0 0 0 5.207 5.021
                  C5.137 5.017 5.071 5 5 5
                  a4 4 0 0 0 0 8h2.167
                  M10 15V6m0 0L8 8m2-2 2 2"
                />
              </svg>

              <p class="text-sm text-gray-500">
                Click to upload
              </p>

              <input
                type="file"
                class="hidden"
                accept="image/png, image/jpeg"
                @change="(e) => onImageChange(e, setValue)"
              />
            </label>

            <p class="error-form-message">{{ errorMessage }}</p>
          </Field>
        </div>

        <!-- FIRST NAME -->
        <div class="user-input-container">
          <label class="label-form">
            First Name <span class="span-required">*</span>
          </label>
          <Field
            name="firstName"
            v-model="formValues.firstName"
            class="user-input-update"
          />
          <ErrorMessage name="firstName" class="error-form-message" />
        </div>

        <!-- LAST NAME -->
        <div class="user-input-container">
          <label class="label-form">
            Last Name <span class="span-required">*</span>
          </label>
          <Field
            name="lastName"
            v-model="formValues.lastName"
            class="user-input-update"
          />
          <ErrorMessage name="lastName" class="error-form-message" />
        </div>

        <!-- EMAIL -->
        <div class="user-input-container">
          <label class="label-form">
            Email <span class="span-required">*</span>
          </label>
          <Field
            name="email"
            v-model="formValues.email"
            class="user-input-update"
            type="email"
          />
          <ErrorMessage name="email" class="error-form-message" />
        </div>

        <!-- PHONE -->
        <div class="user-input-container">
          <label class="label-form">Phone Number</label>
          <Field
            name="phoneNumber"
            v-model="formValues.phoneNumber"
            class="user-input-update"
          />
        </div>

        <Button text="Update" type="submit" />
      </Form>
    </div>
  </div>
</template>
<script setup>
import { ref, watch } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import Button from "./Button.vue";

const props = defineProps({
  user: Object,
});

const emit = defineEmits(["userProfileUpdated"]);

const imagePreview = ref(null);

const formValues = ref({
  firstName: "",
  lastName: "",
  email: "",
  phoneNumber: "",
  image: null,
});

/* Yup schema */
const schema = yup.object({
  firstName: yup.string().required("First name is required"),
  lastName: yup.string().required("Last name is required"),
  email: yup.string().email().required("Email is required"),
  phoneNumber: yup.string().nullable(),
  image: yup
    .mixed()
    .nullable()
    .test("required-if-no-preview", "Image is required", function (value) {
      if (value) return true;
      if (imagePreview.value) return true;
      return false;
    })
    .test("fileType", "Only PNG and JPEG images are allowed", (file) => {
      if (!file) return true;
      return ["image/png", "image/jpeg"].includes(file.type);
    })
    .test("fileSize", "Image must be under 2MB", (file) => {
      if (!file) return true;
      return file.size <= 2 * 1024 * 1024;
    }),
});

/* Image upload */
const onImageChange = (event, setValue) => {
  const file = event.target.files[0];
  if (!file) return;

  setValue(file);

  if (imagePreview.value) {
    URL.revokeObjectURL(imagePreview.value);
  }

  imagePreview.value = URL.createObjectURL(file);
};

/* Submit */
const updateUserProfile = (values) => {
  emit("userProfileUpdated", values);
};

/* Edit mode */
watch(
  () => props.user,
  (user) => {
    if (!user) return;

    formValues.value.firstName = user.first_name || "";
    formValues.value.lastName = user.last_name || "";
    formValues.value.email = user.email || "";
    formValues.value.phoneNumber = user.phone_number || "";
    formValues.value.image = null;

    imagePreview.value = user.user_image_url || null;
  },
  { immediate: true }
);
</script>
