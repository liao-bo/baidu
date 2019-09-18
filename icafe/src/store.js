import Vue from 'vue';
import Vuex from 'vuex';
import iView from 'iview';

import App from './store/App';

Vue.use(Vuex);

export default new Vuex.Store({
    getters: {
        message: state => {
            return iView.Message;
        }
    },
    modules: {
        App
    }
});