<template>
	<div class="w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<form class="w-full">
				<div class="form-row w-full flex gap-[20px] h-[140px]">
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="name"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							Name Of Course
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="courseName"
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
							Language
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								v-model="language"
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
				<!-- <div class="form-row w-full flex gap-[20px] h-[140px]">
					<div class="column w-[49%] flex flex-col gap-[20px] h-full">
						<label
							for="max_members"
							class="text-[#14003B] text-[18px] font-filroy font-medium"
						>
							Max Members
						</label>
						<div class="w-[80%] bg-white h-[60px]">
							<input
								type="text"
								placeholder="Enter max members of course"
								id="max_members"
								name="max_members"
								class="w-full rounded-xl h-full border pl-[10px]"
							/>
						</div>
					</div>
				</div> -->
				<div
					class="image-cotainer w-full flex flex-col gap-[20px] h-[290px] pr-[20px]"
				>
					<label
						for="image"
						class="text-[#14003B] text-[18px] font-filroy font-medium"
						>Image</label
					>
					<div class="w-full h-[200px]">
						<div class="flex items-center justify-start w-full">
							<label
								for="dropzone-file"
								class="flex flex-col items-center justify-center w-[40%] h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
							>
								<div
									class="flex flex-col items-center justify-center pt-5 pb-6 realtive"
								>
									<div v-if="imagePreview">
										<img
											:src="imagePreview"
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
									<!-- <p class="text-xs text-gray-500 dark:text-gray-400">
										SVG, PNG, JPG or GIF (MAX. 800x400px)
									</p> -->
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
							@click.prevent="AddCourse()"
						>
							Add
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
	import { ref } from "vue";
	import { toast } from "vue3-toastify";
	import { useRouter } from "vue-router";
	import axios from "axios";

	const router = useRouter();

	const courseName = ref("");
	const language = ref("");
	const image = ref(null); // Čuva informacije o fajlu
	const imagePreview = ref(null);

	const handleFileChange = (event) => {
		const file = event.target.files[0];
		if (!file) {
			image.value = null;
			imagePreview.value = null;
			return;
		}
		if (!file.type.startsWith("image/")) {
			toast.error("Please upload a valid image file!");
			return;
		}
		image.value = file;
		imagePreview.value = URL.createObjectURL(file);
	};

	const AddCourse = async () => {
		if (!image.value || !courseName.value || !language.value) {
			toast.error("Please enter all fields!");
			return;
		}
		const formData = new FormData();
		formData.append("name", courseName.value);
		formData.append("language", language.value);
		formData.append("file", image.value);
		const token = localStorage.getItem("access_token");

		// for (const pair of formData.entries()) {
		// 	console.log(`${pair[0]}: ${pair[1]}`);
		// }

		try {
			const response = await axios.post("api/admin/add-course", formData, {
				headers: {
					Authorization: `Bearer ${token}`,
				},
			});
			toast.success(response.data.message);
			router.push({ name: "AllCourses" });
		} catch (error) {
			toast.error(error.message);
		}
	};

	// const addCourse = async () => {
	// 	try {
	// 		axios.post("api/admin/add-course", formData, {
	// 			headers: {
	// 				Authorization: `Bearer ${token}`, // Dodajemo token u header
	// 			},
	// 		});
	// 		toast.success("New course addedd sucessfully!");
	// 	} catch (error) {
	// 		toast.error(error.message);
	// 	}
	// };
</script>

<style>
</style>