<template>
	<div class="w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<form class="w-full" @submit.prevent="handleCurrentCourseChange()">
				<div class="form-row">
					<div class="column">
						<label for="max_members" class="label-form">
							Price ($) <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<input
								v-model="form.price"
								type="text"
								placeholder="Enter price of course"
								id="price"
								name="price"
								class="input-el"
							/>
						</div>
					</div>
					<div class="column">
						<label for="max_members" class="label-form">
							Max Members <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<input
								v-model="form.members"
								type="text"
								placeholder="Enter max members of course"
								id="max_members"
								name="max_members"
								class="input-el"
							/>
						</div>
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="max_members" class="label-form">
							Start Date <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<input
								v-model="form.startAt"
								type="datetime-local"
								placeholder="Enter start date of course"
								id="start_at"
								name="start_at"
								class="input-el"
							/>
						</div>
					</div>
					<div class="column">
						<label for="max_members" class="label-form">
							End Date <span class="text-red-500"> * </span></label
						>
						<div class="input-container">
							<input
								v-model="form.endAt"
								type="date"
								placeholder="Enter end date of course"
								id="end_at"
								name="end_at"
								class="input-el"
							/>
						</div>
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="location" class="label-form">
							Location <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<input
								v-model="form.location"
								type="text"
								placeholder="Enter location of course"
								id="location"
								name="location"
								class="input-el"
							/>
						</div>
					</div>
					<div class="column">
						<label for="max_members" class="label-form"
							>Number of Lessons <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<input
								v-model="form.lessons"
								type="number"
								placeholder="Enter number of lessons of course"
								id="lessons"
								name="lessons "
								class="input-el"
							/>
						</div>
					</div>
				</div>
				<div class="form-row">
					<div class="column">
						<label for="location" class="label-form">
							Level <span class="text-red-500"> * </span></label
						>
						<div class="input-container">
							<select
								v-model="form.level"
								id="countries"
								class="h-[64px] bg-white border border-gray-300 text-black text-sm  rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
							>
								<option selected disabled>Choose a Level</option>
								<option value="beginner">Beginner</option>
								<option value="intermediate">Intermediate</option>
								<option value="advanced">Advanced</option>
							</select>
						</div>
					</div>
					<div class="column">
						<label for="max_members" class="label-form">
							Professor <span class="text-red-500"> * </span>
						</label>
						<div class="input-container">
							<select
								v-model="form.professor"
								id="countries"
								class="h-[64px] bg-white border border-gray-300 text-black text-sm  rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
							>
								<option
									v-for="professor in professors"
									:key="professor.id"
									:value="professor.id"
								>
									{{ professor.first_name }} {{ professor.last_name }}
								</option>
							</select>
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
	import { ref, onMounted, watch } from "vue";
	import axios from "axios";
	import { useRoute, useRouter } from "vue-router";
	import { toast } from "vue3-toastify";

	const props = defineProps({
		course: Object,
		text: String,
	});

	const emit = defineEmits(["currentCourseChange"]);

	const router = useRouter();

	const professors = ref("");

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

	function convertToDateFormat(dateString) {
		const date = new Date(dateString);
		const year = date.getFullYear();
		const month = String(date.getMonth() + 1).padStart(2, "0");
		const day = String(date.getDate()).padStart(2, "0");

		return `${year}-${month}-${day}`;
	}

	function convertToDateTimeFormat(dateTimeString) {
		const date = new Date(dateTimeString);
		const year = date.getFullYear();
		const month = String(date.getMonth() + 1).padStart(2, "0"); // Dodaj nulu ako je mesec jednocifren
		const day = String(date.getDate()).padStart(2, "0"); // Dodaj nulu ako je dan jednocifren
		const hours = String(date.getHours()).padStart(2, "0"); // Dodaj nulu ako je sat jednocifren
		const minutes = String(date.getMinutes()).padStart(2, "0"); // Dodaj nulu ako su minuti jednocifreni

		return `${year}-${month}-${day}T${hours}:${minutes}`;
	}

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

	const handleCurrentCourseChange = () => {
		if (
			!form.value.price ||
			!form.value.members ||
			!form.value.startAt ||
			!form.value.endAt ||
			!form.value.lessons ||
			!form.value.professor ||
			!form.value.location ||
			!form.value.level
		) {
			toast.error("Please enter all fields.");
			return;
		}
		emit("currentCourseChange", form.value);
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

<style scoped>
</style>