<template>
	<section class="w-full flex justify-center pt-[200px]">
		<UpdateUserForm :user="user" @userUpdated="updateUser" />
	</section>
</template>

<script setup>
	import { useRoute, useRouter } from "vue-router";
	import { ref } from "vue";
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import UpdateUserForm from "@/components/UpdateUserForm.vue";

	const route = useRoute();
	const router = useRouter();
	const userId = Number(route.query.userId);
	const user = ref({});

	const getUserInfo = async () => {
		await axios
			.get(`api/admin/get-user/${userId}`)

			.then((response) => {
				user.value = response.data;
			})
			.catch(function (error) {
				console.log(error);
			});
	};

	const updateUser = async (form) => {
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
			const response = await axios.put(
				`api/admin/update-user/${userId}`,
				formData
			);
			toast.success(response.data.message);
		} catch (error) {
			toast.error(error.message);
		}
	};

	getUserInfo();
</script>

<style>
</style>