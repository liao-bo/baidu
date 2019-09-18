/**
 * @file Global.js 全局变量和函数
 */

import Utils from './Utils';

const words = {
    LOADING: '加载中...',
    OPERATING: '操作中...',
    SAVING: '保存中...',
    UPDATING: '更新中...',
    DELETING: '删除中...',
    SAVE_OK: '保存成功!',
    UPDATE_OK: '更新成功!',
    DELETE_OK: '删除成功!',
    UNKNOWN_EXCEPTION: '未知错误导致程序异常'
}

const variables = {
    API_URL: function () {
        return process.env.VUE_APP_API_URL;
    },
    SSO_URL: function () {
        return process.env.VUE_APP_SSO_URL;
    }
}

export default {
    install(Vue, option) {
        Vue.prototype.$words = words;
        Vue.prototype.$variables = variables;
        Vue.prototype.$methods = Utils;
    },
    getWords() {
        return words;
    },
    getVariables() {
        return variables;
    },
    getMethods() {
        return Utils;
    }
}