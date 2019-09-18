import Globals from '../Globals';

import axios from 'axios';

export class APIHelper {

    static httper() {
        let _axios = axios.create({
            baseURL: Globals.getVariables().API_URL(),
            //如果ajax请求需要夹带cookie,则服务端设置Access-Control-Allow-Origin的值就不能是*,而应该是一个指定的host
            withCredentials: true
        });

        //所有的API请求response都会经过这里
        _axios.interceptors.response.use(function (res) {
            // if (res.data.code === 401) {
            //     location.href = `${Globals.getVariables().SSO_URL()}/sso/login?callback=${encodeURIComponent(location.href).toLowerCase()}`;
            // }
            return res;
        }, function (error) {
            return Promise.reject(error);
        });

        return _axios;
    }

    static get(path, params) {
        return APIHelper.httper().get(path, {params});
    }

    static delete(path, params) {
        return APIHelper.httper().delete(path, {params});
    }

    static post(path, params, body) {
        return APIHelper.httper().post(path, body, {params});
    }

    static put(path, params, body) {
        return APIHelper.httper().put(path, body, {params});
    }
}