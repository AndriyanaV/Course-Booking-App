<template>
	<div class="h-[60px] min-w-[150px]">
		<button
			class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded h-full min-w-[200px]"
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