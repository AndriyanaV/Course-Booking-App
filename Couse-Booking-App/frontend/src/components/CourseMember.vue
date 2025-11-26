<template>
	<div
		class="w-full px-[40px] flex items-center justify-between border-top pt-[20px]"
	>
		<div class="w-[60%] flex items-center gap-[12px] text-gray-600">
			<div class="w-[40px] h-[40px] rounded-full">
				<img :src="member.user_image_url" class="w-full h-full rounded-full" />
			</div>
			<p>{{ member.first_name }} {{ member.last_name }}</p>
			<p class="font-medium">{{ member.email }}</p>
		</div>
		<div
			v-if="userRole === 'admin'"
			class="w-[160px] h-[44px]  text-white"
			@click="cancelReservation()"
		>
			<button
				class="w-full h-full rounded bg-green-500 hover:bg-red-500 hover:text-white"
			>
				Cancel resevation
			</button>
		</div>
	</div>
</template>

<script setup>
	import axios from "axios";
	import { toast } from "vue3-toastify";
	import { ref, onMounted } from "vue";
	import { useUserRole } from "@/composables/useUserRole.js";

	const { userRole, checkUserRole } = useUserRole();

	const props = defineProps({
		member: Object,
	});

	const emit = defineEmits(["memberDeleted"]);

	const cancelReservation = () => {
		emit("memberDeleted", props.member);
	};

	onMounted(() => {
		checkUserRole();
	});
</script>

<style>
</style>