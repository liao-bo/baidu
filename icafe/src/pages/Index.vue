<template>
	<div id="index">
		<div class="logo-frame">
			<img src="../assets/logo.png">
		</div>
		<h1>JayceVue 管理后台前端脚手架</h1>
		<h3>Vue.js</h3>
		<h3>iView</h3>
		<h3>VueRouter</h3>
		<h3>Vuex</h3>
	</div>
</template>

<script>
	// import SampleAPI from "../API/Sample";

	export default {
		name: "app",
		data() {
			return {
				msg: ""
			};
		},
		created() {
			//API 请求实例
			// SampleAPI.getData().then(res => {
			// 	console.log(res.data.data);
			// });
			// SampleAPI.postData().then(res => {
			// 	console.log(res.data.data);
			// });
		}
	};
</script>

<style scoped>
	#index {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	.logo-frame {
		margin: 1rem 0 1rem 0;
	}

	/* .logo-frame img {
		width: 100%;
	} */

	p {
		text-align: center;
		font-size: 2rem;
	}

	h1 {
		font-weight: normal;
	}
</style>