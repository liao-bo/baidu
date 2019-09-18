<style lang="less">
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
        background: #FFC125;
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
</style>

<template>
    <div class="layout">
        <Layout>
            <Header :style="{padding: 0}" id="Header">
                <div class="app-name">
                    BugsCheck
                </div>
                <div class="app-user-info">
                    <div class="item">
                        <Icon type="md-person" /> {{username}}
                    </div>
                    <div class="item" @click="userLogout">
                        <Icon type="md-exit" />
                    </div>
                </div>
            </Header>
            <Layout class="mid-layout">
                <Layout :style="{paddingLeft: '4px'}">
                    <Content class="content">
                        <router-view />
                        <Footer class="layout-footer-center">2019 @ 小杜Team-QA发版团队</Footer>
                        <Footer class="layout-footer-center">2019 @ 小杜Team-QA发版团队</Footer>
                       
                    </Content>

                </Layout>
            </Layout>
            

        </Layout>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                username: ''

            };
        },
        created() {
            console.log("App Created!");
            var user_name = this.$options.methods.getCookie('user_name');
            if (typeof (user_name) != "undefined") { //以前登录过 直接跳过登录
                this.username = user_name;
            }

            //this.$options.methods.login();
            this.username = 'admin';

        },
        methods: {
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
        }
    };
</script>