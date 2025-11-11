<template>
	<div
		class="min-w-[380px] h-auto flex flex-col items-=center rounded shadow bg-[#EFEFEF] mb-[30px] w-fit cursor-pointer"
	>
		<div class="w-[100%] flex items-start justify-center pt-[20px] h-full">
			<div
				class="w-[100px] h-[100px] rounded-full drop-shadow-[0_4px_5px_rgba(33,14,106,0.2)]"
			>
				<img
					:src="user.user_image_url"
					class="w-full h-full rounded-full drop-shadow-[0_4px_5px_rgba(33,14,106,0.2)]"
				/>
			</div>
		</div>
		<div class="w-[100%] flex flex-col items-between h-full">
			<div class="w-full  gap-[10px]">
				<div class="w-full flex items-center  justify-center pt-[20px]">
					<p class="text-[#15074D] font-bold  text-[18px]">
						{{ user.first_name }} {{ user.last_name }}
					</p>
				</div>
				<div class="w-full flex items-center  justify-center pt-[20px]">
					<p class="text-[#15074D] font-bold  text-[14px]">
						{{ user.email }}
					</p>
				</div>
				<div class="w-full flex items-center h-[33%] justify-center pt-[20px]">
					<p
						v-if="user.phone_number != 0"
						class="text-[#5C55AA] font-bold  text-[14px]"
					>
						{{ user.phone_number }}
					</p>
				</div>
			</div>
			<div
				class="w-full h-[50%] flex items-end justify-end gap-[10px] pb-[8px] pr-[8px]"
			>
				<div
					class="cursor-pointer hover:scale-105"
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
					class="cursor-pointer hover:scale-105"
					@click="
						$router.push({
							name: 'UserInfo',
							query: { userId: user.id },
						})
					"
				>
					<i class="fa-solid fa-eye fa-lg" style="color: #022f7e"></i>
				</div>
				<div class="cursor-pointer hover:scale-105" @click="deleteUser()">
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

	const deleteUser = async () => {
		emit("userDeleted", props.user);
	};
</script>

<style>
</style>