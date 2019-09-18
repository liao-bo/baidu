<template>
	<div id="docs">
		<h2>
			<Icon type="document-text"></Icon>解决方案相关文档</h2>
		<ul>
			<li>
				<a href="https://cn.vuejs.org/" target="_blank">Vue.js 中文官方网站</a>
			</li>
			<li>
				<a href="https://www.iviewui.com/" target="_blank">iView 前端UI组件库</a>
			</li>
			<li>
				<a href="http://router.vuejs.org/zh-cn/" target="_blank">vue-router 前端路由组件中文文档</a>
			</li>
			<li>
				<a href="https://vuex.vuejs.org/zh-cn/" target="_blank">Vuex Vue.js应用程序状态管理模式</a>
			</li>
			<li>
				<a href="https://github.com/vuejs/vue-cli" target="_blank">vue-cli 脚手架构建工具</a>
			</li>
		</ul>
		<h2>
			<Icon type="document-text"></Icon>其他工具文档</h2>
		<ul>
			<li>
				<a href="https://segmentfault.com/a/1190000008470355" target="_blank">Axios 基于Promise的HTTP请求客户端</a>
			</li>
			<li>
				<a href="http://echarts.baidu.com/" target="_blank">ECharts，一个纯 Javascript 的图表库</a>
			</li>
		</ul>
	</div>
</template>

<style scoped>
	#docs {
		padding: 0.2rem 0 0 0.4rem;
	}

	h1,
	h2 {
		font-weight: normal;
	}

	h2 i {
		margin-right: 0.4rem;
	}

	ul {
		font-size: 1rem;
		padding: 1rem 0 1rem 0.5rem;
	}

	li {
		margin-bottom: 0.2rem;
	}
</style>

<script>
	export default {
		data() {
			return {}
		}
	}
</script>