<template>
  <div class="lg:w-[1200px] h-auto bg-white py-[20px] lg:px-[40px] px-[20px] rounded-[14px]">
    <div class="form wraper w-full flex flex-col gap-[40px]">

      <Form :validation-schema="schema" @submit="handleCourseChange" class="w-full flex flex-col gap-[40px] py-[40px]">
        <!-- Course name and language -->
        <div class="form-row">
          <div class="column">
            <label for="name" class="label-form">
              Name Of Course <span class="span-required">*</span>
            </label>
            <!-- We need name to connect it with schema and v-model for edit mode initial value -->
            <Field name="name" v-model="formValues.name" type="text" class="input-el" id="name" />
            <ErrorMessage name="name" class="error-form-message " />
          </div>

          <div class="column">
            <label for="language" class="label-form">
              Language <span class="span-required">*</span>
            </label>
            <Field name="language" v-model="formValues.language" type="text" class="input-el" id="language" />
            <ErrorMessage name="language" class="error-form-message " />
          </div>
        </div>

        <!-- Course Image -->
        <div class="w-full flex flex-col gap-[20px] justify-start align-start">
          <label class="label-form text-start">
            Image <span class="span-required">*</span>
          </label>

          <!-- Use v-slot to control validation using vee-validate -->
          <Field name="image" v-slot="{ setValue, errorMessage }">
            <label
              class="flex flex-col items-center justify-center lg:w-[40%] w-full h-64 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-100 relative">
              <img v-if="imagePreview" :src="imagePreview" class="absolute max-h-[180px]" />

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
                Click to upload or drag and drop
              </p>

              <input type="file" accept="image/png, image/jpeg" class="hidden"
                @change="(e) => onImageChange(e, setValue)" />
            </label>

            <p class="error-form-message text-start">{{ errorMessage }}</p>
          </Field>
        </div>

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
import * as yup from "yup";

const props = defineProps({
  course: Object,
  buttonText: String,
});

// Emit for edit/add course
const emit = defineEmits(["courseChange"]);

const imagePreview = ref(null);

// Important for edit mode, to get initial values
const formValues = ref({
  name: "",
  language: "",
  image: null,
});

/* Yup schema */
const schema = yup.object({
  name: yup.string().required("Course name is required"),
  language: yup.string().required("Language is required"),
  image: yup
    .mixed()
    .nullable()
    .test(
      "required-if-no-preview",
      "Image is required",
      function (value) {
        // value = new image (File)
        // imagePreview.value = old image (URL)
        if (value) return true;             // new image
        if (imagePreview.value) return true; // if we have old image as preview for edit mode then true
        return false;                        // no image - error
      }
    )
    .test(
      "fileType",
      "Only PNG and JPEG images are allowed",
      (file) => {
        // If the user hasn't selected a new file yet (file === null),
        // the validation passes – the type is not checked.
        // If a new file exists, it checks that the file is PNG or JPEG.
        if (!file) return true;
        return ["image/png", "image/jpeg"].includes(file.type);
      }
    )
    .test(
      "fileSize",
      "Image size should not exceed 2MB",
      (file) => {
        // If the user hasn't selected a new file yet (file === null),
        // the validation passes – the size is not checked.
        // If a new file exists, it checks size
        if (!file) return true;
        return file.size <= 2 * 1024 * 1024;
      }
    ),
});

//Handle upload/change of image
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

const handleCourseChange = (values) => {
  emit("courseChange", values);
};

// Edit mode
watch(
  () => props.course,
  (course) => {
    if (!course) return;
    imagePreview.value = course.course_image_url;
    formValues.value.name = course.name || "";
    formValues.value.language = course.language || "";
    formValues.value.image = null;
  },
  { immediate: true }
);

</script>