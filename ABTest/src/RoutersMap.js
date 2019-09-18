class RoutesMap {
	static get() {
		//业务子应用程序
		const Index = resolve => require(['./pages/Index.vue'], resolve);
		const Docs = resolve => require(['./pages/Docs.vue'], resolve);
		const TableSample = resolve => require(['./pages/TableSample.vue'], resolve);
		const ButtonSample = resolve => require(['./pages/ButtonSample.vue'], resolve);
		const IconSample = resolve => require(['./pages/IconSample.vue'], resolve);
		const InputSample = resolve => require(['./pages/InputSample.vue'], resolve);
		const ToastSample = resolve => require(['./pages/ToastSample.vue'], resolve);
		const ModalSample = resolve => require(['./pages/ModalSample.vue'], resolve);

		const LessonSample = resolve => require(['./pages/LessonSample.vue'], resolve);

		let routes = [
			{ path: '/', component: Index },
			{ path: '/index', component: Index },
			{ path: '/docs', component: Docs },
			{ path: '/table', component: TableSample },
			{ path: '/button', component: ButtonSample },
			{ path: '/icon', component: IconSample },
			{ path: '/input', component: InputSample },
			{ path: '/toast', component: ToastSample },
			{ path: '/modal', component: ModalSample },
			{ path: '/lesson', component: LessonSample }
		];
		return routes;
	}
}

module.exports = RoutesMap;
