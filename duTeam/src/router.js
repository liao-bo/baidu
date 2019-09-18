import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            component: () => import('./pages/Index.vue')
        },
        {
            path: '/docs',
            component: () => import('./pages/Docs.vue')
        },
        {
            path: '/table',
            component: () => import('./pages/TableSample.vue')
        },
        {
            path: '/button',
            component: () => import('./pages/ButtonSample.vue')
        },
        {
            path: '/icon',
            component: () => import('./pages/IconSample.vue')
        },
        {
            path: '/input',
            component: () => import('./pages/InputSample.vue')
        },
        {
            path: '/toast',
            component: () => import('./pages/ToastSample.vue')
        },
        {
            path: '/modal',
            component: () => import('./pages/ModalSample.vue')
        },
        {
            path: '/lesson',
            component: () => import('./pages/LessonSample.vue')
        }
    ]
})
