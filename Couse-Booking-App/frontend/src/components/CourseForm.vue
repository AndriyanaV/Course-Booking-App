<template>
	<div class="w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<form class="w-full" @submit.prevent="handleCourseChange()">
				<div class="form-row w-full flex gap-[20px] h-[140px]">
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="name"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							Name Of Course (*)
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="form.name"
								type="text"
								placeholder="Enter course name"
								id="courseName"
								name="courseName"
								class="w-full rounded-xl h-full border pl-[10px]"
								required
							/>
						</div>
					</div>
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="course_language"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							Language (*)
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="form.language"
								type="text"
								placeholder="Enter language"
								id="language"
								name="language"
								class="w-full rounded-xl h-full border pr-[5px] pl-[10px]"
								required
							/>
						</div>
					</div>
				</div>

				<div
					class="image-cotainer w-full flex flex-col gap-[20px] h-[290px] pr-[20px]"
				>
					<label
						for="image"
						class="text-[#14003B] text-[18px] font-filroy font-medium"
						>Image (*)</label
					>
					<div class="w-full h-[200px]">
						<div class="flex items-center justify-start w-full">
							<label
								for="dropzone-file"
								class="flex flex-col items-center justify-center w-[40%] h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-white dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
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
									<p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
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
	import axios from "axios";

	const emit = defineEmits(["courseChange"]);

	const props = defineProps({
		course: Object,
		text: String,
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

<style>
</style>