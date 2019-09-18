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
        background: #fff;
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
            background-color: #9ACD32;
        }
    }

    #Header {
        background: #66CD00;
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

    .configManage {
        display: none;
    }

    .overlayer {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.65);
        height: 100%;
        width: 100%;
        z-index: 1000;
        opacity: .80;
        filter: alpha(opacity=50);
    }

    .wrap {
        position: fixed;
        overflow: auto;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        z-index: 1000;
        -webkit-overflow-scrolling: touch;
        /*outline: 0;*/
    }

    .modal {
        font-size: 14px;
        font-variant: tabular-nums;
        line-height: 1.5;
        color: rgba(0, 0, 0, 0.65);
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        list-style: none;
        position: relative;
        width: auto;
        margin: 0 auto;
        top: 150px;
        padding-bottom: 24px;
    }

    .content2 {
        margin-left: 30%;
        margin-right: 30%;
        position: relative;
        background-color: #fff;
        border: 0;
        border-radius: 4px;
        background-clip: padding-box;
        -webkit-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .moder-header {
        padding: 16px 24px;
        border-radius: 4px 4px 0 0;
        background: #fff;
        color: rgba(0, 0, 0, 0.65);
        border-bottom: 1px solid #e8e8e8;
    }

    .moder-body {
        padding: 24px;
        font-size: 14px;
        line-height: 1.5;
        word-wrap: break-word;
    }

    .moder-footer {
        border-top: 1px solid #e8e8e8;
        padding: 10px 16px;
        text-align: right;
        border-radius: 0 0 4px 4px;
    }
</style>
</style>

<template>
    <div class="layout">
        <Layout>
            <Header :style="{padding: 0}" id="Header">
                <div class="app-name">
                    百度App-AB实验预警平台
                </div>

                <div class="app-user-info">
                    <div class="item" @click="config()">配置</div>
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

                    </Content>
                    
                </Layout>
            </Layout>

            
        </Layout>
        <div v-bind:class="{configManage:configManageIsActive}">
            <div class="overlayer"></div>
            <div class="wrap">
                <div class="modal">
                    <div class="content2">
                        <div class="moder-header">
                            默认值设定
                        </div>
                        <div class="moder-body">
                            <Row>
                                <Col span="8" offset="4">
                                线上比对版本号：
                                </Col>
                                <Col span="8">
                                <input type="text" v-model='onlineNum'>
                                </Col>
                            </Row>
                            <br/>
                            <Row>
                                <Col span="8" offset="4">
                                发版版本号：
                                </Col>
                                <Col span="8">
                                <input type="text" v-model='releaseNum'>
                                </Col>

                            </Row>
                            <br/>
                            <Row>
                                <Col span="8" offset="4">
                                灰度版本号：
                                </Col>
                                <Col span="8">
                                    <input type="text" v-model='greyNum'>
                                </Col>

                            </Row>

                        </div>
                        <div class="moder-footer">
                            <Button @click="cancell()">取消</Button>
                            <Button @click="startconfig()">确定</Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                username: '',
                configManageIsActive: true,
                onlineNum:'', //线上比对版本号
                greyNum:'', //灰度版本号
                releaseNum: '',//发版版本号
                isManager:false,
                managerList:['chenran07','songhao03','admin']

            };
        },
        created() {
            console.log("App Created!");
            var instance = this;
            var user_name = this.$options.methods.getCookie('user_name');
            if (typeof (user_name) != "undefined") { //以前登录过 直接跳过登录
                this.username = user_name;
            }

            //this.$options.methods.login();
            this.username = 'admin';
            if(this.managerList.indexOf(this.username)>=0){
                this.isManager = true;
            }
            this.$options.methods.handleGetData({'key': 5}).then(function (value) {
                //console.log(value); 
                
                        instance.releaseNum = instance.$options.methods.changeStrToNum(value[0].releaseNum);
                        instance.greyNum = instance.$options.methods.changeStrToNum(value[0].greyNum);
                        instance.onlineNum = instance.$options.methods.changeStrToNum(value[0].onlineNum);
                        
                    })

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
            config() {
                this.configManageIsActive = false;
            },
            cancell() {
                this.configManageIsActive = true;

            },
            startconfig() {
                var instance = this;
                if(this.$options.methods.regMatch(instance.onlineNum)&&this.$options.methods.regMatch(instance.greyNum)&&this.$options.methods.regMatch(instance.releaseNum)){
                    
                    let onlinenum = instance.$options.methods.changeNumToStr(instance.onlineNum);
                    let greynum = instance.$options.methods.changeNumToStr(instance.greyNum);
                    let releasenum = instance.$options.methods.changeNumToStr(instance.releaseNum);
                    
                    this.$options.methods.handleGetData({'key': 4, 'onlineNum': onlinenum, 'greyNum': greynum, 'releaseNum': releasenum}).then(function (value) {
                        //console.log(value);
                        if(value){
                            instance.$Message.success('配置成功');
                            location.reload();
                        }
                        else{
                            instance.$Message.warning('配置失败');
                        }
                        
                        
                        // console.log(instance.list);
                    })
                    this.configManageIsActive = true;
                }
                else{
                    this.$Message.warning("请检查版本号是否正确，请输入三位版本号，如11.1.1")
                }
                
                

            },
            handleGetData(params) {
                var messsage = params;
                return new Promise((resolve, reject) => {
                    axios({
                        method: 'get',
                        url: 'http://release.baidu-int.com:8081/versionSign/abtest',
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
            regMatch(str){
                var matchStr = /^\d{1,2}\.\d{1,2}\.\d{1,2}$/;
                return matchStr.test(str);
            },
            changeNumToStr(str){
                var array = str.split('.');
                for(let i = 1;i < 3; i++){
                    if(array[i].length==1){
                        array[i] = '000'+array[i];
                    }else{
                        array[i] = '00'+array[i];
                    }
                    

                }
                //console.log(""+array[0]+array[1]+array[2]+'0000000');
                return ""+array[0]+array[1]+array[2]+'0000000';


            },
            changeStrToNum(str){
                let one =str.substring(0,2);
                let two = str.substring(2,6).replace(/^0+/,'');
                two  = two.length == 0?'0':two;
                let three = str.substring(6,10).replace(/^0+/,'');
                three = three.length==0?'0':three;
                //console.log(one+'.'+two+'.'+three);
                return one+'.'+two+'.'+three;

            }
        }
    };
</script>