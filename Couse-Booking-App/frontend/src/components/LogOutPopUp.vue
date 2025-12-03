<template>
	<section v-if="userStore.showLogoutPopUp" @click="userStore.toggleLogoutPopUp" class="fixed inset-0 bg-black/50 flex justify-center items-center z-50" >
		<div @click.stop class="bg-white p-8 rounded-lg shadow-md max-w-md w-[90%] text-center flex flex-col gap-[20px]">
			<p class="text-gray-700 mb-6 text-lg">
				Do you want to log out?
			</p>

			<div class="flex justify-center gap-4">
				<button
					class="bg-red-500 hover:bg-red-600 text-white font-semibold px-5 py-2 rounded"
					@click="logout"
				>
					Logout
				</button>

				<button
					class="bg-gray-500 hover:bg-gray-600 text-white font-semibold px-5 py-2 rounded"
					@click="userStore.toggleLogoutPopUp"
				>
					Cancel
				</button>
			</div>
		</div>
	</section>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { useLogout } from "@/composables/useLogout";

const userStore = useUserStore();
const { logout } = useLogout();

</script>

<style>
</style>