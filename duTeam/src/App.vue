<style >
    html,
    body {
        width: 100%;
        height: 100%;
    }

    .layout {
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        min-width: 1190px;
        height: 100vh;
        display: flex;
        flex-direction: column;
    }

    .layout-footer-center {
        text-align: center;
        height: 30px;
        line-height: 8px;
    }

    .app-name {
        float: left;
        color: #fff;
        font-size: 26px;
        padding: 0 40px;
    }

    .app-user-info {
        float: right;
        color: #fff;
        font-size: 18px;

        .item {
            float: left;
            padding: 0 10px;
        }

        .item:hover {
            background-color: #61697d;
        }
    }

    #Header {
        background: #2d8cf0;
    }

    .mid-layout {
        height: 100%;

        .sider {
            height: 100%;
            overflow-y: auto;
        }

        .sider::-webkit-scrollbar {
            width: 0;
        }

        .content {
            height: 100%;
            overflow: auto;
            background: #fff;
            padding: 10px 20px;
            margin: 0;
        }
    }
</style>

<template>
    <div class="layout">
        <Layout>
            <Header :style="{padding: 0}" id="Header">
                <div class="app-name">
                    百度App-QA门户
                </div>
                <div class="app-user-info">

                    <div class="item" @click="showchecklist">
                        <Badge dot :count='count' :offset=[15,0]>
                            审批
                        </Badge>
                    </div>
                    <div class="item">
                        <Icon type="md-person" /> {{username}}
                    </div>
                    <div class="item" @click="userLogout">
                        <Icon type="md-exit" />
                    </div>
                </div>
            </Header>
            <Layout class="mid-layout">

                <Content class="content">
                    <team :urlInfo="urlInfo" :username='username' :administratorlist="administratorlist"
                        :isAdministrator='isAdministrator'></team>
                    <!-- <router-view /> -->
                    <Footer class="layout-footer-center">2019 @ 小杜Team-QA发版团队</Footer>
                </Content>

            </Layout>

            
        </Layout>
        <approve :approveData="approvelist" :administrator="administratorlist"
            :propApproveManageIsActive="propApproveManageIsActive" :username="username"
            :isAdministrator="isAdministrator" v-on:listenapproveisactive='approveisactive'></approve>
    </div>
</template>

<script>
    import {mapGetters} from "vuex";
    import team from "./pages/team.vue"
    import approve from "./components/approve.vue"
    import axios from 'axios'

    export default {
        components: {
            team, approve
        },
        data() {
            return {
                username: '',
                urlInfo: [
                ],
                approvelist: [],
                administratorlist: [],
                propApproveManageIsActive: 1,//审批信息是否展示，0表示展示，1，表示不展示。
                isAdministrator: 0, //是否是管理员，0表示不是，1表示是
                count:0,
            }
        },

        created() {
            const modulTitle = ['团队文化','标准规范','常用工具','事务管理','新人培养','版本相关','稳定性'];
            console.log("App Created!");
            //Vuex 使用示例

            var user_name = this.$options.methods.getCookie('user_name');
            if (typeof (user_name) != "undefined") { //以前登录过 直接跳过登录
                this.username = user_name;
            }

            this.$options.methods.login();
            //this.username = 'admin';

            let instance = this;
            this.handleGetData({'key': 0}).then(function (value) {

                var duteamlist = value.duteamlist;
                instance.approvelist = value.approvelist;
                var titleJson = {'团队文化':[],'标准规范':[],'常用工具':[],'事务管理':[],'新人培养':[],'版本相关':[],'稳定性':[]};

                for (let i = 0; i < duteamlist.length; i++) {
                    if (titleJson.hasOwnProperty(duteamlist[i].title)) {
                        titleJson[duteamlist[i].title].push(duteamlist[i]);
                    } else {
                        titleJson[duteamlist[i].title] = [duteamlist[i]];
                    }
                }
                for (let key in titleJson) {
                    let json = {};

                    json['title'] = key;
                    json['list'] = titleJson[key];
                    instance.urlInfo.push(json);
                }

                for (let i = 0; i < value.administratorlist.length; i++) {
                    instance.administratorlist.push(value.administratorlist[i].username);
                }
                if (instance.administratorlist.indexOf(instance.username) > -1) {
                    instance.isAdministrator = 1;
                }
                for (let i = 0; i < value.approvelist.length; i++){
                    if(value.approvelist[i].isAccept == 'nullvalue'){
                        instance.count = 1;
                    }
                }
               // console.log(instance.administratorlist);
            })
        },
        methods: {
            onRouteChange(newVal, oldVal) {
                this.setCurrent(newVal.path);
            },
            onUserDropdownClick(name) {
                const dropActions = {
                    info: () => {},
                    security: () => {},
                    service: () => {},
                    logout: this.userLogout
                };
                if (dropActions[name]) {
                    dropActions[name]();
                }
            },
            userLogout() {
                const redirectURL =
                    'http://release.baidu-int.com:8081/uuap/api.php?logout=1';
                window.location.replace(redirectURL);
            },
            login: function () { //登录函数
                const LOGINURL = 'https://itebeta.baidu.com/login';
                var user_name = this.getCookie('user_name');
                if (typeof (user_name) != 'object') {
                    return user_name;
                }
                else {
                    const urlParams = new URL(window.location.href);
                    const redirectURL =
                        'http://release.baidu-int.com:8081/uuap/api.php?sourse=' +
                        urlParams;
                    window.location.replace(redirectURL);
                }

            },
            getCookie: function (name) {

                var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)"); //正则匹配
                if (arr = document.cookie.match(reg)) {
                    return unescape(arr[2]);
                }
                else {
                    return null;
                }
            },
            handleGetData(params) {
                var messsage = params;
                return new Promise((resolve, reject) => {
                    axios({
                        method: 'get',
                        url: 'http://release.baidu-int.com:8081/versionSign/duteam',
                        params: {
                            info: messsage
                        }
                    }).then(response => {
                        resolve(response.data);
                    }).catch(error => {
                        reject(error);
                    })
                })
            },
            showchecklist() {
                this.propApproveManageIsActive = 0;
            },
            approveisactive(value) {
                this.propApproveManageIsActive = value;
            }
        }
    };
</script>