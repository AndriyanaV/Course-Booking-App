<template>
	<section
		class="w-full py-[150px] flex flex-col justify-center items-center bg-[#f5f5f4] lg:px-[40px] px-[20px]  h-full">
		<div
			class="container max-w-[1320px] mx-auto flex flex-col justify-center items-center text-center lg:gap-[60px] gap-[40px]">
			<Heading heading="Update User Info" color="#46A5BA" class="w-full font-bold  text-center" fontSize="46"
				fontWeight="600" />
			<UserForm :user="user" buttonText="Update User Info" :isAddMode="isAddMode" @userChange="updateUser" />
		</div>
	</section>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import axios from "axios";
import { toast } from "vue3-toastify";
import UserForm from "@/components/UserForm.vue";
import Heading from "@/components/Heading.vue";

const isAddMode = ref(false);

const route = useRoute();
const router = useRouter();
const userId = Number(route.query.userId);
const user = ref({});

const getUserInfo = async () => {
	try {
		const response = await axios.get(`api/admin/get-user/${userId}`);
		user.value = response.data;
	} catch (error) {
		toast(error.message || error.response.data.message);
	}
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
		router.push("/all-users").then(() => toast.success(response.data.message));
	} catch (error) {
		toast.error(error.message);
	}
};

onMounted(() => {
	getUserInfo();
});
</script>

<style></style>