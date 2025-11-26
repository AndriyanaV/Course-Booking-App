<template>
	<div class="lg:h-[60px] lg:min-w-[150px] h-[48px] min-w-[100px]">
		<button
			class="bg-[#46A5BA] hover:bg-[#4096a9] text-white font-bold py-2 px-4 rounded h-full min-w-[100px]  mt-[10px]"
			@click="handleClick()"
		>
			{{ text }}
		</button>
	</div>
</template>

<script setup>
	const props = defineProps({
		text: String,
	});

	const emit = defineEmits(["buttonClicked"]);

	const handleClick = () => {
		emit("buttonClicked");
	};
</script>

<style>
</style>