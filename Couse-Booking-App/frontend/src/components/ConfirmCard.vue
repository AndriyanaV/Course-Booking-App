<template>
    <div v-if="confirmCard"
			class="bg-white rounded-md cursor-pointer p-6 shadow-[0_10px_30px_rgba(2,6,23,0.08)] text-center w-full h-full absolute top-0 flex flex-col items-center justify-center">
			<div class="w-full h-fit flex flex-col gap-[6px]  text-red-300">
				<h3 class="text-[16px]">Are you sure?</h3>
				<p>This action cannot be undone.</p>
				<div class="w-full flex gap-[40px] justify-center mt-[14px]">
					<button class="w-1/2 bg-green-400 h-[44px] rounded-[16px] text-white font-bold hover:scale-[1.05]"
						@click="$emit('onDelete')">OK</button>
					<button class="w-1/2 bg-red-400 h-[44px] rounded-[16px] text-white font-bold hover:scale-[1.05]"
						@click="$emit('onCancelDelete')">Cancel</button>
				</div>
			</div>
		</div>
</template>

<script setup>
import { defineEmits } from 'vue';
import {defineProps } from 'vue';

const props = defineProps({
	confirmCard: Boolean,
});


</script>

<style scoped>
</style>