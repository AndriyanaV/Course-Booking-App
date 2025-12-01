<template>
	<div class="lg:w-[1200px] h-auto bg-white py-[20px] lg:px-[40px] px-[20px] rounded-[14px] ">
		<div class="form wraper h-auto w-full flex flex-col gap-[40px]">
			<form class="w-full flex flex-col lg:gap-[40px] py-[40px] gap-[40px]" @submit.prevent="handleCourseChange">
				<div class=" w-[100%] flex lg:flex-row flex-col h-auto gap-[40px] lg:min-h-[140px]">
					<div class="column lg:min-w-[50%] min-w-[100%] flex flex-col items-start gap-[20px] h-full">
						<label for="name" class="text-gray-900 text-[18px] font-medium">
							Name Of Course <span class="text-red-400"> * </span>
						</label>
						<div class="lg:w-[80%] w-full bg-white lg:min-h-[60px]">
							<input v-model="form.name" type="text" placeholder="Enter course name" id="courseName"
								name="courseName" class="input-el" required />
						</div>
					</div>
					<div class="column lg:min-w-[50%] min-w-[100%] items-start flex flex-col gap-[20px] h-fit">
						<label for="course_language" class="text-gray-900 text-[18px] font-filroy font-medium">
							Language <span class="text-red-400"> * </span>
						</label>
						<div class="lg:w-[80%] bg-white lg:h-[60px]">
							<input v-model="form.language" type="text" placeholder="Enter language" id="language"
								name="language" class="input-el" required />
						</div>
					</div>
					
				</div>
				<div class="image-cotainer w-full flex flex-col items-start gap-[20px] h-[290px] pr-[20px]">
						<label for="image" class="text-[#14003B] text-[18px] font-filroy font-medium">Image <span
								class="text-red-500"> * </span></label>
						<div class="w-full lg:h-[200px]">
							<div class="flex items-center justify-start w-full ">
								<label for="dropzone-file"
									class="flex flex-col items-center justify-center lg:w-[40%] w-[100%] h-64 border border-gray-200 border-solid rounded-lg cursor-pointer hover:bg-gray-100">
									<div class="flex flex-col items-center justify-around pt-5 pb-6 realtive">
										<div v-if="form.imagePreview">
											<img :src="form.imagePreview" alt="Image preview" style="max-width: 200px"
												class="aboslute top-0" />
										</div>
										<svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400 absolute"
											aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
											viewBox="0 0 20 16">
											<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
												stroke-width="2"
												d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
										</svg>
										<p class="mb-2 text-sm text-gray-500 dark:text-gray-400 pt-[20px]">
											<span class="font-semibold mt-[5px]">Click to upload</span>
											or drag and drop
										</p>
									</div>
									<input id="dropzone-file" type="file" class="hidden" @change="handleFileChange" />
								</label>
							</div>
						</div>
					</div>


				<div class="w-full  flex items-center justify-start mt-[20px]">
					<Button :text="buttonText" @click="handleCourseChange" />
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
import { ref, watch } from "vue";
import { toast } from "vue3-toastify";
import Button from "./Button.vue";

const emit = defineEmits(["courseChange"]);

const props = defineProps({
	course: Object,
	buttonText: String,
});

const form = ref({
	name: "",
	language: "",
	image: "",
	imagePreview: "",
});

watch(
	() => props.course,
	(newCourse) => {
		if (newCourse) {
			form.value.name = newCourse.name || "";
			form.value.language = newCourse.language || "";
			form.value.imagePreview = newCourse.course_image_url || "";
			form.value.image = newCourse.course_image_url || "";
		}
	},
	{ immediate: true }
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

const handleCourseChange = () => {
	if (!form.value.image || !form.value.name || !form.value.language) {
		toast.error("Please enter all fields!");
		return;
	}

	emit("courseChange", form.value);
};
</script>

<style></style>