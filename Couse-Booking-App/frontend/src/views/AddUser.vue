<template>
	<section class="w-full flex justify-center pt-[200px]">
		<AddUserForm @userAdded="addUser" />
	</section>
</template>

<script setup>
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import AddUserForm from "@/components/AddUserForm.vue";

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
			toast.success(response.data.message);
		} catch (error) {
			toast.error(error.response.data.message);
		}
	};
</script>

<style>
</style>