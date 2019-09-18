/**
 * @file Web前端项目工具类
 */

import {Message} from 'iview';

export default class Utils {

    /**
     * 时间戳转时间String
     * @param {number} ts 时间戳
     * @param {Function} formatFunc 字符串模版函数
     * @return {string} 时间显示字符串
     */
    static tsToDateStringFormat(ts, formatFunc) {
        function zeroPrefix(num) {
            return `${num < 10 ? '0' : ''}${num}`;
        }
        let tsInt = typeof ts === 'string' ? parseInt(ts, 10) : ts;
        let date = new Date(tsInt);

        let year = date.getFullYear();
        let month = zeroPrefix(date.getMonth() + 1);
        let day = zeroPrefix(date.getDate());
        let hour = zeroPrefix(date.getHours());
        let minute = zeroPrefix(date.getMinutes());
        let second = zeroPrefix(date.getSeconds());

        if (!formatFunc) {
            return `${year}-${month}-${day} ${hour}:${minute}:${second}`;
        }
        return formatFunc({year, month, day, hour, minute, second});
    }

    /**
     * 获取时间对象的秒级时间戳
     * @param {*} date 时间对象
     * @return {number} timestamp number
     */
    static getTimeStampSecond(date) {
        return Math.floor(date.getTime() / 1000);
    }

    /**
     * 获取当前时间的秒级时间戳
     * @return {number} timestamp number
     */
    static getTimeStampNowSecond() {
        return Utils.getTimeStampSecond(new Date());
    }

    /**
     * 获取时间对象的零点日期时间
     * @param {*} date 时间对象
     * @return {Date} date object
     */
    static getDateTimeZero(date) {
        date.setHours(0, 0, 0);
        return date;
    }

    /**
     * 获取时间对象的末点(23:59:59)日期时间
     * @param {*} date 时间对象
     * @return {Date} date object
     */
    static getDateTimeEnd(date) {
        date.setHours(23, 59, 59);
        return date;
    }

    /**
     * 显示错误Message(传入errInfo的code为0或者401时则自动不显示,code为0返回false,不为0返回true,用以业务逻辑判断是否执行后续程序)
     * @param {*} errInfo 错误信息对象
     * @return {boolean} code为0返回false,不为0返回true,用以业务逻辑判断是否执行后续程序
     */
    static showErrorMsg(errInfo = {}) {
        let code = errInfo.code === undefined || errInfo.code === null ? 500 : errInfo.code;
        // code = 0 表示不需要显示errMessage,则返回false,业务视图也不需要因显示errMessage而中断后续逻辑
        if (code === 0) {
            return false;
        }
        // 打印错误log方便调试
        console.log(errInfo);
        // 401 表示用户未登录,此时页面跳转,不需要显示Message
        if (code === 401) {
            return true;
        }
        Message.error(errInfo.msg || '未知异常导致加载失败!');
        return true;
    }
}