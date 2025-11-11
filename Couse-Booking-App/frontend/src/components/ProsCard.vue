<template>
    <div class="w-ful min-h-[200px] rounded-[16px] p-[20px] flex flex-col gap-[14px] bg-white mt-[10px] items-center justify-center cursor-pointer hover:scale-105 group transition-transform duration-300">
        <div class="w-full flex justify-start h-[30%]">
            <div class="w-[35px] h-[35px] bg-[#886df6] p-[8px] rounded-full transform transition-transform duration-300 
                    group-hover:-translate-y-2">
                <img :src="imgSrc" class="w-full h-full object-cover"/>
            </div>
        </div>
        <div class="w-full h-[70%] flex flex-col gap-[10px] text-gray-950">
            <p class="font-semibold text-gray-900">{{title}}</p>
            <p class="text-base text-gray-600">{{desc}}</p>
        </div>
    </div>

</template>
<script setup>
defineProps({
		title: String,
        desc:String,
		imgSrc: String,
	});

</script>

<style>
</style>