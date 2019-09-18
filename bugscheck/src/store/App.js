/*
    Vuex Store Sample
    Vuex适用于在SPA前端应用中管理应用程序的一些全局状态,也可以理解为需要全局使用的数据,包括当前登录的用户信息,管理权限,以及一次加载可以在多处View中复用的数据
    很多项目也使用Vuex来规范应用程序的数据流,使应用程序的数据流呈单向(单向数据流),根据项目规模决定是否需要在项目全局采用单向数据流管理
*/

const GET_LOGIN_USER = 'getLoginUser';

const state = {
    loginUserInfo: {
        name: '',
        level: 0
    }
}

const getters = {
    loginUserInfo: state => state.loginUserInfo
}

const actions = {
    getLoginUser({ commit }, payload) {
        commit(GET_LOGIN_USER, { name: payload.name, level: payload.level });
    }
}

const mutations = {
    [GET_LOGIN_USER](state, res) {
        state.loginUserInfo = res;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}