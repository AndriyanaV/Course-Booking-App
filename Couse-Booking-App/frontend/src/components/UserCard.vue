<template>
	<div
		class="w-[420px] h-[175px] flex items-start rounded shadow bg-[#EFEFEF] mb-[30px]"
	>
		<div class="w-[50%] flex items-start justify-center pt-[10px] h-full">
			<div
				class="w-[100px] h-[100px] rounded-full drop-shadow-[0_4px_5px_rgba(33,14,106,0.2)]"
			>
				<img
					:src="user.user_image_url"
					class="w-full h-full rounded-full drop-shadow-[0_4px_5px_rgba(33,14,106,0.2)]"
				/>
			</div>
		</div>
		<div class="w-[50%] flex flex-col items-between h-full">
			<div class="w-full h-[50%] gap-[10px]">
				<div class="w-full flex items-center h-[33%] justify-center pt-[20px]">
					<p class="text-[#15074D] font-bold font-gilroy text-[18px]">
						{{ user.first_name }} {{ user.last_name }}
					</p>
				</div>
				<div class="w-full flex items-center h-[33%] justify-center pt-[20px]">
					<p class="text-[#15074D] font-bold font-gilroy text-[14px]">
						{{ user.email }}
					</p>
				</div>
				<div class="w-full flex items-center h-[33%] justify-center pt-[20px]">
					<p
						v-if="user.phone_number != 0"
						class="text-[#5C55AA] font-bold font-gilroy text-[14px]"
					>
						{{ user.phone_number }}
					</p>
				</div>
			</div>
			<div
				class="w-full h-[50%] gap-[10px] flex items-end justify-end gap-[10px] pb-[8px] pr-[8px]"
			>
				<div
					class="cursor-pointer"
					@click="
						$router.push({
							name: 'UpdateUser',
							query: { userId: user.id },
						})
					"
				>
					<i class="fas fa-edit fa-lg" style="color: #1f11df"></i>
				</div>
				<div
					class="cursor-pointer"
					@click="
						$router.push({
							name: 'UserInfo',
							query: { userId: user.id },
						})
					"
				>
					<i class="fa-solid fa-eye fa-lg" style="color: #022f7e"></i>
				</div>
				<div class="cursor-pointer" @click="deleteUser()">
					<i class="fa-solid fa-trash-can fa-lg" style="color: #d40c0c"></i>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
	import { toast } from "vue3-toastify";
	import axios from "axios";
	const props = defineProps({ user: Object });

	const emit = defineEmits(["userDeleted"]);

	console.log(props.user.name);

	const deleteUser = async () => {
		try {
			if (confirm("Are you sure?")) {
				const response = await axios.delete(
					`api/admin/delete-user/${props.user.id}`
				);
				toast.success(response.data.message);
				emit("userDeleted", props.user);
			}
		} catch (error) {
			toast.error(error.message);
		}
	};
</script>

<style>
</style>