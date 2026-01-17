<template>
	<div class="lg:w-[1200px] bg-white lg:py-[40px] py-[20px] lg:px-[40px] px-[20px] rounded shadow">
		<div class="w-full">
			<Form :validation-schema="schema" @submit="handleCurrentCourseChange"
				class="w-full flex flex-col gap-[40px] py-[40px]">
				<div class="form-row">
					<div class="column">
						<label for="price" class="label-form">
							Price ($)<span class="span-required">*</span>
						</label>
						<!-- We need name to connect it with schema and v-model for edit mode initial value -->
						<Field name="price" v-model="form.price" type="text" class="input-el" id="price"
							placeholder="Enter a price" />
						<ErrorMessage name="price" class="error-form-message " />
					</div>
					<div class="column">
						<label for="maxMembers" class="label-form">
							Max Members <span class="span-required"> * </span>
						</label>
						<Field name="maxMembers" v-model="form.members" type="number" class="input-el"
							id="maxMembers" placeholder="Enter max memebrs"/>
						<ErrorMessage name="maxMembers" class="error-form-message " />
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="startAt" class="label-form">
							Start Date <span class="span-required"> * </span>
						</label>
						<Field name="startAt" v-model="form.startAt" type="datetime-local" class="input-el bg-white"
							id="startAt" />
						<ErrorMessage name="startAt" class="error-form-message " />
					</div>
					<div class="column">
						<label for="end_at" class="label-form">
							End Date <span class="span-required"> * </span>
						</label>
						<Field name="endAt" v-model="form.endAt" type="date" class="input-el bg-white"
							id="endAt" />
						<ErrorMessage name="endAt" class="error-form-message " />
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="location" class="label-form">
							Location <span class="span-required"> * </span>
						</label>
						<Field name="location" v-model="form.location" type="text" class="input-el bg-white"
							id="location" placeholder="Enter a location" />
						<ErrorMessage name="location" class="error-form-message " />
					</div>
					<div class="column">
						<label for="lessons" class="label-form">
							Number of lessons <span class="span-required"> * </span>
						</label>
						<Field name="lessons" v-model="form.lessons" type="number" class="input-el bg-white"
							id="lessons" placeholder="Enter a number of lessons" />
						<ErrorMessage name="lessons" class="error-form-message " />
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="level" class="label-form">
							Level <span class="span-required"> * </span></label>
						<Field name="level" as="select" v-model="form.level" class="input-el" id="level">
							<option disabled value="">Choose a Level</option>
							<option value="beginner">Beginner</option>
							<option value="intermediate">Intermediate</option>
							<option value="advanced">Advanced</option>
						</Field>
						<ErrorMessage name="level" class="error-form-message" />
					</div>
					<div class="column">
						<label for="professor" class="label-form">
							Professor <span class="text-red-500"> * </span>
						</label>
						<Field name="professor" as="select" v-model="form.professor" class="input-el" id="professor">
							<option disabled value="">Choose a Professor</option>
							<option v-for="professor in professors" :key="professor.id" :value="professor.id">
								{{ professor.first_name }} {{ professor.last_name }}
							</option>
						</Field>
						<ErrorMessage name="professor" class="error-form-message" />
					</div>
				</div>

				<div class="w-full flex items-center justify-start mt-[20px]">
					<Button :text="buttonText" />
				</div>
			</Form>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import axios from "axios";
import { useRoute, useRouter } from "vue-router";
import { toast } from "vue3-toastify";
import Button from "./Button.vue";
import { convertToDateFormat } from "@/utils/convertToDateFormat";
import { convertToDateTimeFormat } from "@/utils/convertToDateTimeFormat";

const props = defineProps({
	course: Object,
	buttonText: String,
});

const emit = defineEmits(["currentCourseChange"]);

const router = useRouter();

const professors = ref("");

const schema = yup.object({
  price: yup
    .number()
    .typeError("Price must be a number")
    .positive("Price must be positive")
    .required("Price is required"),

  maxMembers: yup
    .number()
    .typeError("Max members must be a number")
    .integer("Max members must be an integer")
    .positive("Max members must be positive")
    .required("Max members is required"),

  startAt: yup
    .date()
    .typeError("Start date is required")
    .required("Start date is required"),

  endAt: yup
    .date()
    .typeError("End date is required")
    .min(
      yup.ref("startAt"),
      "End date cannot be before start date"
    )
    .required("End date is required"),

  location: yup
    .string()
    .required("Location is required"),

  lessons: yup
    .number()
    .typeError("Number of lessons must be a number")
    .integer("Number of lessons must be an integer")
    .positive("Number of lessons must be positive")
    .required("Number of lessons is required"),

  level: yup
    .string()
    .oneOf(["beginner", "intermediate", "advanced"], "Please choose a valid level")
    .required("Level is required"),

  professor: yup
    .string()
    .required("Professor is required"),
});

// Important for edit mode
const form = ref({
	price: "",
	members: "",
	startAt: "",
	endAt: "",
	lessons: "",
	professor: "",
	location: "",
	level: "",
});


watch(
	() => props.course,
	(newCourse) => {
		if (newCourse) {
			form.value.price = newCourse.price || "";
			form.value.members = newCourse.max_members || "";
			form.value.startAt = convertToDateTimeFormat(newCourse.start_at) || "";
			form.value.endAt = convertToDateFormat(newCourse.end_at) || "";
			form.value.lessons = newCourse.lessons || "";
			form.value.professor = newCourse.user_id || "";
			form.value.location = newCourse.location || "";
			form.value.level = newCourse.level || "";
		}
	},
	{ immediate: true }
);

const handleCurrentCourseChange = (values) => {
	emit("currentCourseChange", values);
};

const getProfessors = async () => {
	try {
		const response = await axios.get("api/admin/get-professors");
		professors.value = response.data;
	} catch (error) {
		toast.error(error);
	}
};

onMounted(() => {
	getProfessors();
});
</script>

<style scoped></style>