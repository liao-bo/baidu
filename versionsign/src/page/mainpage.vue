<style scoped>
    .layout{
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }
    .layout-logo{
        width: 100px;
        height: 30px;
        background: #5b6270;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 15px;
        left: 20px;
    }
    .layout-nav{
        width: 420px;
        margin: 0 auto;
        margin-right: 20px;
    }
    .layout-footer-center{
        text-align: center;
    }
</style>
<template>
    <div class="layout">
        <Layout>
            <Header :style="{position: 'fixed', width: '100%', zIndex: '1000'}">
                <Row>
                    <Col span="6" :style ="{color: 'rgba(255, 255, 255, 0.65)', fontWeight:'bold', fontSize: '20px' }">
                       <span :style = "{float:'right'}">
                           版本签章平台
                       </span>
                    </Col>
                    <Col span="18" :style ="{color: 'rgba(255, 255, 255, 0.65)', fontSize: '20px'}">
                    <span :style = "{float:'right'}">
                        {{username}}
                    </span>
                    </Col>
                </Row>
            </Header>
            <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}">
                <versionsigncontent/>
            </Content>
            <Footer class="layout-footer-center">2019 &copy; QA-发版团队</Footer>
        </Layout>
    </div>
</template>
<script>
    import versionsigncontent from './versionsigncontent.vue'
    export default {
    	components:{versionsigncontent},
        
            data (){
                return{
                    username:'chenran07'
                }

            },
            created (){
                var user_name = this.$options.methods.getCookie('user_name');
                if(typeof(user_name) != "undefined"){ //以前登录过 直接跳过登录
                    this.username = user_name;
                }
            
                //this.$options.methods.login();
                this.username = 'demo';
            },
            methods:{

                login: function(){ //登录函数
                    const LOGINURL = 'https://itebeta.baidu.com/login';
                    var user_name = this.getCookie('user_name');
                    if(typeof(user_name) != 'object'){
                        return user_name;    
                    }
                    else{
                        const urlParams = new URL(window.location.href);
                        const redirectURL =
                        'http://release.baidu-int.com:8081/uuap/api.php?sourse='+
                        urlParams;
                        window.location.replace(redirectURL);
                    }

            },
            getCookie:function(name)
            {

                var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)"); //正则匹配
                if(arr=document.cookie.match(reg)){
                  return unescape(arr[2]);
                }
                else{
                 return null;
                }
            }
            }
            
        
        
    }
</script>
