<template>
	<div
		class="flex w-[1100px] flex-col justify-start items-center gap-[10px] h-screen"
	>
		<div class="title-desc">
			<div class="title">
				<p>Course name</p>
			</div>
			<div class="description">
				<p>{{ course.name }}</p>
			</div>
		</div>
		<div class="title-desc">
			<div class="title">
				<p>Language</p>
			</div>
			<div class="description">
				<p>{{ course.language }}</p>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { ref, onMounted } from "vue";
	import { toast } from "vue3-toastify";
	import axios from "axios";
	const props = defineProps({
		courseId: String,
	});

	const course = ref("");
	const id = Number(props.courseId);
	console.log(typeof id);
	console.log(typeof Number(id));
	const getCourse = async () => {
		try {
			const token = localStorage.getItem("access_token");

			const response = await axios.get(`/api/admin/get-course/${id}`, {
				headers: {
					Authorization: `Bearer ${token}`, // Dodajemo token u header
				},
			});
			course.value = response.data;
		} catch (error) {
			toast.error(error.response?.data?.message || error.message);
		}
	};

	onMounted(() => {
		getCourse();
	});
</script>

<style>
</style>