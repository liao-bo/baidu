<template>
	<div class="toast-layout">
		<Button type="primary" @click="info">显示普通提醒</Button>
		<br>
		<br>
		<Button @click="success">显示成功提示</Button>
		<br>
		<br>
		<Button @click="warning">显示警告提示</Button>
		<br>
		<br>
		<Button @click="error">显示错误提示</Button>
		<br>
		<br>
		<Button @click="loading">显示加载中...</Button>
		<br>
		<br>
		<Button @click="time">显示一个10秒的提示</Button>
	</div>
</template>

<style scoped>
	.toast-layout {
		padding: 0.2rem 0 0 0.4rem;
	}
</style>

<script>
	export default {
		data() {
			return {};
		},
		components: {},
		created() { },
		methods: {
			info() {
				this.$Message.info("这是一条普通的提醒");
			},
			success() {
				this.$Message.success("这是一条成功的提示");
			},
			warning() {
				this.$Message.warning("这是一条警告的提示");
			},
			error() {
				this.$Message.error("对方不想说话，并且向你抛出了一个异常");
			},
			loading() {
				const msg = this.$Message.loading("正在加载中...", 0);
				setTimeout(msg, 3000);
			},
			time() {
				this.$Message.info("我将在10秒后消失", 10);
			}
		}
	};
</script>