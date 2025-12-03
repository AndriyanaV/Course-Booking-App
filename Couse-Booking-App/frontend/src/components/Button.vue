<template>
	<div 
		:class="[
			'lg:h-[44px] lg:min-w-[150px] w-fit h-[40px] min-w-[100px]',
			mt ? 'mt-[10px]' : ''
		]"
	>
		<button
			class="bg-[#46A5BA] hover:bg-[#4096a9] text-white font-bold w-full py-2 px-4 rounded h-full min-w-[100px]"
			@click="handleClick()"
		>
			{{ text }}
		</button>
	</div>
</template>

<script setup>
	const props = defineProps({
		text: String,
		mt: {
		type: Boolean,
		default: true, 
	},
	});

	const emit = defineEmits(["buttonClicked"]);

	const handleClick = () => {
		emit("buttonClicked");
	};
</script>

<style>
</style>