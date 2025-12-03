<template>
	<div class=" lg:min-w-[30%] lg:w-[30%] w-[100%] min-w-[100%] h-auto flex flex-col items-=center rounded shadow-[0_4px_12px_rgba(0,0,0,0.06)] mb-[30px] cursor-pointer py-[20px] hover:scale-[1.05] transition-all ease-in relative"
		style="background-color: rgba(239, 239, 239, 0.45)">
		<div class="w-[100%] flex items-start justify-center pt-[20px] h-full">
			<div class="w-[100px] h-[100px] rounded-full ">
				<img :src="user.user_image_url" class="w-full h-full rounded-full " />
			</div>
		</div>
		<div class="w-[100%] flex flex-col items-between h-full">
			<div class="w-full  gap-[10px]">
				<div class="w-full flex items-center  justify-center pt-[20px]">
					<p class="text-language-heading font-bold  text-[18px]">
						{{ user.first_name }} {{ user.last_name }}
					</p>
				</div>
				<div class="w-full flex items-center  justify-center pt-[20px]">
					<p class="text-gray-600  text-[16px]">
						{{ user.email }}
					</p>
				</div>
				<div class="w-full flex items-center h-[33%] justify-center pt-[20px]">
					<p v-if="user.phone_number" class="text-gray-600  text-[16px]">
						{{ user.phone_number }}
					</p>
				</div>
			</div>
			<div class="w-fit h-fit flex items-end justify-end gap-[10px] absolute top-[10px] right-[10px]">
				<div class="cursor-pointer hover:scale-105 h-[20px] w-[20px]" @click="
					$router.push({
						name: 'UpdateUser',
						query: { userId: user.id },
					})
					">
					<img src="/images/pencil.svg" class="w-full h-full" />
				</div>
				<!-- <div
					class="cursor-pointer hover:scale-105"
					@click="
						$router.push({
							name: 'UserInfo',
							query: { userId: user.id },
						})
					"
				>
					<i class="fa-solid fa-eye fa-lg" style="color: #022f7e"></i>
				</div> -->
				<div class="cursor-pointer hover:scale-105 h-[20px] w-[20px]" @click="toggleConfirmCard">
					<img src="/images/delete-x.svg" class="w-full h-full" />
				</div>
			</div>
		</div>
		<!-- Confirm Card Component -->
		<ConfirmCard :confirmCard="confirmCard" @onDelete="deleteUser" @onCancelDelete="toggleConfirmCard" />
	</div>
</template>

<script setup>
import { toast } from "vue3-toastify";
import axios from "axios";
import { ref } from "vue";
import ConfirmCard from "./ConfirmCard.vue";
import { useConfirmCard } from '@/composables/useConfirmCard.js'; 

const props = defineProps({ user: Object });

const emit = defineEmits(["userDeleted"]);

const { confirmCard, toggleConfirmCard } = useConfirmCard();

const deleteUser = async () => {
	emit("userDeleted", props.user);
	toggleConfirmCard();
};
</script>

<style></style>