<template>
  <div v-if="loading || !user" class="w-full flex justify-center items-center h-full">
    <Loader />
  </div>
  <div v-else class="lg:w-[500px] flex flex-col gap-[40px]">
    <div class="user-form-container w-full">

      <Form ref="userForm" :validation-schema="schema" :initial-values="initialValues" @submit="updateUserProfile"
        class="w-full flex flex-col gap-[20px]">

        <!-- Image -->
        <div class="w-full flex flex-col gap-[10px]">
          <label class="label-form text-start">
            Image <span class="span-required">*</span>
          </label>

          <Field name="image" v-slot="{ setValue, errorMessage }">
            <label class="flex flex-col items-center justify-center lg:w-[40%] h-[200px]
                     border-2 border-gray-100 rounded-lg cursor-pointer hover:bg-gray-100 relative">
              <img v-if="imagePreview" :src="imagePreview" class="absolute max-h-[120px]" />

              <svg v-else class="w-8 h-8 mb-4 text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none"
                viewBox="0 0 20 16">
                <path stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M13 13h3a3 3 0 0 0 0-6h-.025
                  A5.56 5.56 0 0 0 16 6.5
                  5.5 5.5 0 0 0 5.207 5.021
                  C5.137 5.017 5.071 5 5 5
                  a4 4 0 0 0 0 8h2.167
                  M10 15V6m0 0L8 8m2-2 2 2" />
              </svg>

              <p class="text-sm text-gray-500">
                Click to upload
              </p>

              <input type="file" class="hidden" accept="image/png, image/jpeg" @change="(e) => {
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

            <p class="error-form-message">{{ errorMessage }}</p>
          </Field>
        </div>

        <!-- First name -->
        <div class="user-input-container">
          <label class="label-form">
            First Name <span class="span-required">*</span>
          </label>
          <Field name="firstName" class="user-input-update" />
          <ErrorMessage name="firstName" class="error-form-message" />
        </div>

        <!-- Last name -->
        <div class="user-input-container">
          <label class="label-form">
            Last Name <span class="span-required">*</span>
          </label>
          <Field name="lastName" class="user-input-update" />
          <ErrorMessage name="lastName" class="error-form-message" />
        </div>

        <!-- Email -->
        <div class="user-input-container">
          <label class="label-form">
            Email <span class="span-required">*</span>
          </label>
          <Field name="email" type="email" class="user-input-update" />
          <ErrorMessage name="email" class="error-form-message" />
        </div>

        <!-- Phone number -->
        <div class="user-input-container">
          <label class="label-form">Phone Number</label>
          <Field name="phoneNumber" class="user-input-update" />
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
import { userProfileUpdateSchema } from "@/validation/userProfileUpdateSchema.js";
import { useImagePreview } from "@/composables/useImagePreview";
import Loader from "@/components/Loader.vue";
import { computed } from "vue";

const initialValues = computed(() => {
  if (!props.user) return {};

  return {
    firstName: props.user.first_name || "",
    lastName: props.user.last_name || "",
    email: props.user.email || "",
    phoneNumber: props.user.phone_number || "",
    image: null,
  };
});

const props = defineProps({
  user: Object,
  loading: {
		type: Boolean,
		default: false
	} 
});

const emit = defineEmits(["userProfileUpdated"]);

const userForm = ref(null);
const { preview: imagePreview, setFile } = useImagePreview();

const schema = userProfileUpdateSchema(imagePreview);

const removeImage = (setValue
) => {
  imagePreview.value = null
  setValue(null)

  // Reset file input to solve problem when we remove image and try to add it again 
  const inputEl = document.querySelector('input[type="file"]');
  if (inputEl) inputEl.value = "";
}

/* Submit */
const updateUserProfile = (values) => {
  emit("userProfileUpdated", values);
};

/* Edit mode */
watch(
  () => props.user,
  (user) => {
    if (!user || !userForm.value) return;

    userForm.value.setValues({
      firstName: user.first_name || "",
      lastName: user.last_name || "",
      email: user.email || "",
      phoneNumber: user.phone_number || "",
      image: null,
    });

    imagePreview.value = user.user_image_url || null;
  },
  { immediate: true }
);
</script>
