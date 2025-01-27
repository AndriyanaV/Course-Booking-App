<template>
	<nav
		class="w-full h-[90px] flex justify-center bg-[#f4f8ff] fixed z-40 top-0"
	>
		<div
			class="content w-[1320px] h-full flex items-center justify-between bg-[#f4f8ff]"
		>
			<div class="h-full flex items-center">
				<RouterLink
					class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
					active-class="text-blue-600 font-bold"
					to="/"
					>Homepage</RouterLink
				>
				<RouterLink
					class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
					to="all-courses"
					active-class="text-blue-600 font-bold"
					>All Courses</RouterLink
				>
				<RouterLink
					class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
					to="all-users"
					active-class="text-blue-600 font-bold"
					>All Users</RouterLink
				>
				<RouterLink
					class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
					to="/"
					active-class="text-blue-600 font-bold"
					>My Courses</RouterLink
				>
				<RouterLink
					class="block no-underline py-2 px-3 text-gray-900 rounded hover:bg-gray-100 font-gilroy"
					to="/"
					active-class="text-blue-600 font-bold"
					>My Courses</RouterLink
				>
			</div>

			<div class="flex h-full items-center gap-[15px]">
				<button
					class="bg-[#090DE7] hover:bg-blue-800 text-white font-semibold py-2 px-4 border border-gray-400 rounded h-[47px] w-[130px]"
				>
					Sign In
				</button>
				<button
					class="bg-gray-100 hover:bg-gray-300 text-black font-semibold py-2 px-4 border border-gray-400 rounded h-[47px] w-[130px]"
				>
					Sign Out
				</button>
				<div>
					<div class="w-[45px] h-[45px] rounded-full">
						<img
							src="/images/user.png"
							class="w-[98%] h-[98%] rounded-full border"
						/>
					</div>
				</div>
			</div>
		</div>
	</nav>
</template>

<script setup>
</script>

<style scoped>
</style>