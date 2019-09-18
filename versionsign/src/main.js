// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import iView from 'iview';
import 'iview/dist/styles/iview.css';

// Vue.use(VueRouter);
Vue.use(iView)
import axios from 'axios'
// import VueAxios from 'vue-axios'

import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

// Vue.use(VueAxios)
Vue.prototype.$ajax = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
