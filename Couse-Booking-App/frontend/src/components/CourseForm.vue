<template>
  <!-- Loader -->
  <div v-show="loading" class="w-full flex justify-center items-center h-full">
    <Loader />
  </div>

  <!-- Form -->
  <div v-show="!loading" class="lg:w-[1200px] h-auto bg-white py-[20px] lg:px-[40px] px-[20px] rounded-[14px]">
    <div  class="form wraper w-full flex flex-col gap-[40px] relative">
      <Form ref="courseForm" :validation-schema="schema" :initial-values="initialValues" @submit="handleCourseChange"
        class="w-full flex flex-col gap-[40px] py-[40px]">
        <!-- Course name and language -->
        <div class="form-row">
          <div class="column">
            <label for="name" class="label-form">
              Name Of Course <span class="span-required">*</span>
            </label>
            <!-- v-model removed, vee-validate kontrolise vrednost -->
            <Field name="name" type="text" class="input-el" id="name" />
            <ErrorMessage name="name" class="error-form-message" />
          </div>

          <div class="column">
            <label for="language" class="label-form">
              Language <span class="span-required">*</span>
            </label>
            <Field name="language" type="text" class="input-el" id="language" />
            <ErrorMessage name="language" class="error-form-message" />
          </div>
        </div>

        <!-- Course Image -->
        <div class="w-full flex flex-col gap-[20px] justify-start align-start">
          <label class="label-form text-start">
            Image <span class="span-required">*</span>
          </label>

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

              <input type="file" accept="image/png, image/jpeg" class="hidden" @change="(e) => {
                setValue(e.target.files[0]);
                setFile(e.target.files[0]);
              }" />
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
import { ref, computed, watch } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import { courseSchema } from "@/validation/courseSchema.js";
import { useImagePreview } from "@/composables/useImagePreview";
import Loader from "@/components/Loader.vue";


const props = defineProps({
  course: Object,
  buttonText: String,
  loading: {
    type: Boolean,
    required: false,
    default: false
  }
});


const courseForm = ref(null);
const { preview: imagePreview, setFile } = useImagePreview();

const schema = courseSchema(imagePreview);

const emit = defineEmits(["courseChange"]);

/* Watch for edit mode course */
watch(
  () => props.course,
  (course) => {
    if (!course) return;

    // update preview image
    imagePreview.value = course.course_image_url || null;

    // Form values from api
    if (courseForm.value) {
      courseForm.value.setValues({
        name: course.name || "",
        language: course.language || "",
        image: null, // file input null
      });
    }
  },
  { immediate: true }
);

/* Submit handler */
const handleCourseChange = (values) => {
  emit("courseChange", values);
};
</script>
