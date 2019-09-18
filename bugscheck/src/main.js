import Vue from 'vue';
import App from './App.vue';
import router from './router';

import iView from 'iview';
import 'iview/dist/styles/iview.css';

import VueClipboard from 'vue-clipboard2'
 
Vue.use(VueClipboard)

Vue.use(iView);

// import global from './Globals';
// Vue.use(global);

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App)
}).$mount('#app');