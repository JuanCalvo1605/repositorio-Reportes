<script setup>
import login from './views/login.vue';

</script>

<template>
	<div class="app">
		<router-view />
		<!--<login/>
    	<sidebar />
    	-->
	</div>      
</template>

<style lang="scss">
:root {
	--primary: #98836A;
	--primary-alt: #98836A;
	--grey: #64748b;
	--dark: #181717;
	--dark-alt: #080606;
	--light: #f1f5f9;
	--sidebar-width: 300px;
}

* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Fira sans', sans-serif;
}

body {
	background: var(--light);
}

button {
	cursor: pointer;
	appearance: none;
	border: none;
	outline: none;
	background: none;
}

.app{
	display: flex;
	main{
		flex: 1 1 0;
		padding: 2rem;
		@media(max-width: 768px){
		padding-left: 6rem;
		}
	}
}
</style>
