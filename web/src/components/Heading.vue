<template>
	<div>
		<h1 :style="{
			color: color,
			fontSize: fontSize  + 'px',
		}" :class="fontWeight ? '' : 'font-semibold'">
			{{ heading }}
		</h1>
	</div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
defineProps({
	heading: String,
	color: String,
	fontWeight: String,
	fontSize: Number,
});

const fontSize = ref(70)

const updateFontSize = () => {
	fontSize.value = window.innerWidth < 1024 ? 32 : 70
}

onMounted(() => {
  updateFontSize()
  window.addEventListener('resize', updateFontSize)
})

onUnmounted(() => {
  window.removeEventListener('resize', updateFontSize)
})
</script>

<style scoped></style>