class RoutesMap {
	static get() {
		//业务子应用程序
		const Index = resolve => require(['./pages/Index.vue'], resolve);
		

		let routes = [
			{ path: '/', component: Index }
		];
		return routes;
	}
}

export default RoutesMap;
