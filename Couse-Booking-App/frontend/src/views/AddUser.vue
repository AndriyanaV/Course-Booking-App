<template>
	<section class="w-full flex flex-col justify-center py-[150px] gap-[60px] h-full items-center">
		<Heading heading="Add New User" color="#2430D6" class="w-full font-bold  text-center" fontSize="46" fontWeight="600"/>
		<UserForm text="Add" :isAddMode="isAddMode" @userChange="addUser" />
	</section>
</template>

<script setup>
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import { useRouter } from "vue-router";
	import { ref } from "vue";
	import UserForm from "@/components/UserForm.vue";
	import Heading from "@/components/Heading.vue";

	const router = useRouter();

	const isAddMode = ref(true);

	const addUser = async (form) => {
		const formData = new FormData();
		formData.append("first_name", form.firstName);
		formData.append("last_name", form.lastName);
		formData.append("email", form.email);
		formData.append("file", form.image);
		formData.append("phone_number", form.phoneNumber);
		formData.append("biography", form.biography);
		formData.append("password", form.password);
		formData.append("rola", form.rola);

		try {
			const response = await axios.post("api/admin/add-user", formData);

			router.push("/all-users").then(() => toast.success(response.data.message));
		} catch (error) {
			toast.error(error.response.data.message);
		}
	};
</script>

<style>
</style>