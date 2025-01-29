<template>
	<div class="w-[1200px] bg-white py-[20px] px-[40px] rounded shadow">
		<div class="form wraper w-full flex flex-col gap-[40px]">
			<form class="w-full" @submit.prevent="updateActiveCourse()">
				<div class="form-row">
					<div class="column">
						<label for="max_members" class="label-form"> Price ($) </label>
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
						<label for="max_members" class="label-form"> Max Members </label>
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
						<label for="max_members" class="label-form"> Start Date </label>
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
						<label for="max_members" class="label-form"> End Date </label>
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
						<label for="location" class="label-form"> Location </label>
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
							>Number of Lessons
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
						<label for="location" class="label-form"> Level </label>
						<div class="input-container">
							<select
								v-model="form.level"
								id="countries"
								class="h-[64px] bg-white border border-gray-300 text-black text-sm font-gilroy rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
							>
								<option selected disabled>Choose a Level</option>
								<option value="beginner">Beginner</option>
								<option value="intermediate">Intermediate</option>
								<option value="advanced">Advanced</option>
							</select>
						</div>
					</div>
					<div class="column">
						<label for="max_members" class="label-form"> Pforessor </label>
						<div class="input-container">
							<select
								v-model="form.professor"
								id="countries"
								class="h-[64px] bg-white border border-gray-300 text-black text-sm font-gilroy rounded-xl focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
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
							Add
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
	import { toast } from "vue3-toastify";

	const props = defineProps({
		course: Object,
	});

	const emit = defineEmits(["activeCourseUpdated"]);

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

	const getProfessors = async () => {
		try {
			const response = await axios.get("api/admin//get-professors");
			professors.value = response.data;
		} catch (error) {
			toast.error(error);
		}
	};

	const updateActiveCourse = () => {
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
			toast.error("Please enter all filds.");
			return;
		}

		emit("activeCourseUpdated", form.value);
	};

	// async function getCourseInfo() {
	// 	await axios
	// 		.get(`api/current-courses/course-info/${props.courseId}`)

	// 		.then((response) => {
	// 			course.value = response.data;
	// 			price.value = course.value.price;
	// 			members.value = course.value.max_members;
	// 			lessons.value = course.value.lessons;
	// 			location.value = course.value.location;
	// 			level.value = course.value.level;
	// 			professor.value = course.value.user_id;
	// 		})
	// 		.catch(function (error) {
	// 			console.log(error);
	// 		});
	// }

	// const updateActiveCourse = async () => {
	// 	if (
	// 		!price.value ||
	// 		!members.value ||
	// 		!startAt.value ||
	// 		!endAt.value ||
	// 		!lessons.value ||
	// 		!professor.value ||
	// 		!location.value ||
	// 		!level.value
	// 	) {
	// 		toast.error("Please enter all filds.");
	// 		return;
	// 	}
	// 	try {
	// 		const response = await axios.put(
	// 			`api/admin/update-current-course/${courseId}`,
	// 			{
	// 				professor: professor.value,
	// 				price: price.value,
	// 				start_at: startAt.value,
	// 				end_at: endAt.value,
	// 				level: level.value,
	// 				location: location.value,
	// 				max_members: members.value,
	// 				lessons: lessons.value,
	// 			}
	// 		);
	// 		router
	// 			.push(`/all-current-courses/${courseId}`)
	// 			.then(() => toast.success(response.data.message));
	// 	} catch (error) {
	// 		toast.error(error);
	// 	}
	// };

	onMounted(() => {
		getProfessors();
	});
</script>

<style>
</style>