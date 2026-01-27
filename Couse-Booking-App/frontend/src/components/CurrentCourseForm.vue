<template>
  <!-- Loader -->
  <div v-if="loading" class="w-full flex justify-center items-center h-full">
		<Loader />
	</div>
  <div v-else class="lg:w-[1200px] bg-white lg:py-[40px] py-[20px] lg:px-[40px] px-[20px] rounded shadow">
    <div class="w-full">
      <Form
        ref="courseForm"
        :validation-schema="schema"
        :initial-values="initialValues"
        @submit="handleCurrentCourseChange"
        class="w-full flex flex-col gap-[40px] py-[40px]"
      >
        <!-- First row: price & max members -->
        <div class="form-row">
          <div class="column">
            <label for="price" class="label-form">Price ($)<span class="span-required">*</span></label>
            <Field name="price" type="number" class="input-el" />
            <ErrorMessage name="price" class="error-form-message" />
          </div>
          <div class="column">
            <label for="maxMembers" class="label-form">Max Members <span class="span-required">*</span></label>
            <Field name="maxMembers" type="number" class="input-el" />
            <ErrorMessage name="maxMembers" class="error-form-message" />
          </div>
        </div>

        <!-- dates -->
        <div class="form-row">
          <div class="column">
            <label for="startAt" class="label-form">Start Date <span class="span-required">*</span></label>
            <Field name="startAt" type="datetime-local" class="input-el bg-white" />
            <ErrorMessage name="startAt" class="error-form-message" />
          </div>
          <div class="column">
            <label for="endAt" class="label-form">End Date <span class="span-required">*</span></label>
            <Field name="endAt" type="date" class="input-el bg-white" />
            <ErrorMessage name="endAt" class="error-form-message" />
          </div>
        </div>

        <!-- location and lessons -->
        <div class="form-row">
          <div class="column">
            <label for="location" class="label-form">Location <span class="span-required">*</span></label>
            <Field name="location" type="text" class="input-el bg-white" />
            <ErrorMessage name="location" class="error-form-message" />
          </div>
          <div class="column">
            <label for="lessons" class="label-form">Number of lessons <span class="span-required">*</span></label>
            <Field name="lessons" type="number" class="input-el bg-white" />
            <ErrorMessage name="lessons" class="error-form-message" />
          </div>
        </div>

        <!-- level and professor -->
        <div class="form-row">
          <div class="column">
            <label for="level" class="label-form">Level <span class="span-required">*</span></label>
            <Field name="level" as="select" class="input-el">
              <option disabled value="">Choose a Level</option>
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </Field>
            <ErrorMessage name="level" class="error-form-message" />
          </div>
          <div class="column">
            <label for="professor" class="label-form">Professor <span class="span-required">*</span></label>
            <Field name="professor" as="select" class="input-el">
              <option disabled value="">Choose a Professor</option>
              <option v-for="professor in professors" :key="professor.id" :value="professor.id">
                {{ professor.first_name }} {{ professor.last_name }}
              </option>
            </Field>
            <ErrorMessage name="professor" class="error-form-message" />
          </div>
        </div>

        <!-- Submit -->
        <div class="w-full flex items-center justify-start mt-[20px]">
          <Button :text="buttonText" />
        </div>
      </Form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import axios from "axios";
import Button from "./Button.vue";
import { convertToDateFormat } from "@/utils/convertToDateFormat";
import { convertToDateTimeFormat } from "@/utils/convertToDateTimeFormat";
import { currentCourseSchema} from "@/validation/currentCourseSchema.js";
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
const emit = defineEmits(["currentCourseChange"]);

const courseForm = ref(null);
const professors = ref([]);

const schema = currentCourseSchema();

/* Computed initial values */
const initialValues = computed(() => ({
  price: props.course?.price || "",
  maxMembers: props.course?.max_members || "",
  startAt: convertToDateTimeFormat(props.course?.start_at) || "",
  endAt: convertToDateFormat(props.course?.end_at) || "",
  lessons: props.course?.lessons || "",
  professor: props.course?.user_id || "",
  location: props.course?.location || "",
  level: props.course?.level || "",
}));

/* Watch API course for edit mode */
watch(
  () => props.course,
  (newCourse) => {
    if (!newCourse) return;
    if (courseForm.value) {
      courseForm.value.setValues({
        price: newCourse.price || "",
        maxMembers: newCourse.max_members || "",
        startAt: convertToDateTimeFormat(newCourse.start_at) || "",
        endAt: convertToDateFormat(newCourse.end_at) || "",
        lessons: newCourse.lessons || "",
        professor: newCourse.user_id || "",
        location: newCourse.location || "",
        level: newCourse.level || "",
      });
    }
  },
  { immediate: true }
);

/* Submit */
const handleCurrentCourseChange = (values) => {
  emit("currentCourseChange", values);
};

/* Fetch professors */
const getProfessors = async () => {
  try {
    const res = await axios.get("api/admin/get-professors");
    professors.value = res.data;
  } catch (e) {
    console.error(e);
  }
};

onMounted(() => getProfessors());
</script>
