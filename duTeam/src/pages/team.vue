<style lang="less">
    .titleManage {
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

    .content1 {
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

    .lable-item {
        font-size: 14px;
        font-variant: tabular-nums;
        line-height: 1.5;
        color: rgba(0, 0, 0, 0.65);
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        list-style: none;
        margin-bottom: 24px;
        vertical-align: top;
    }

    .addmodalstart {
        text-align: center;
        /* display:flex;
        margin:auto;  */
        line-height: 200px;

    }
    .center {
        display: table-cell;
        vertical-align: middle;
        text-align: center;
    }
</style>

<template>
    <div>
        <Row>
            <Col span="6" v-for="(item, index) in urlInfo" :key="index">
            <Cell :mainData="item" :username='username' :administratorlist="administratorlist"
                :isAdministrator="isAdministrator">
            </Cell>
            </Col>
            <Col span="6" class="addmodalstart" style="height: 300px">
            <a href="#" @click="addmodalstart()">
                <Icon type="ios-add-circle-outline" size="100" />
            </a>
            </Col>
        </Row>
        <div v-bind:class="{titleManage:isManageShow}">
            <div class="overlayer"></div>
            <div class="wrap">
                <div class="modal">
                    <div class="content1">
                        <div class="moder-header">
                            请设置一个标题
                        </div>
                        <div class="moder-body">
                            <div class="lable-item">
                                <Row>
                                    <Col span="4" class="center">
                                    <div class="lable">
                                        标题:
                                    </div>
                                    </Col>
                                    <Col span="20">
                                    <div>
                                        <Input type="text" v-model="inserttitle" />
                                    </div>
                                    </Col>
                                </Row>
                            </div>
                        </div>
                        <div class="moder-footer">
                            <Button @click="cancellManage()">取消</Button>
                            <Button @click="addmodal()">添加</Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <template>
            <Modal v-model="modal" title="是否需要新增一項" @on-ok="ok" @on-cancel="cancel">
                <p>title：{{inserttitle}}</p>
            </Modal>
        </template>

    </div>
</template>

<script>

    import Cell from "../components/Cell.vue"

    import axios from 'axios'


    export default {
        components: {
            Cell
        },
        props: ['urlInfo', 'username', 'administratorlist', 'isAdministrator'],
        data() {
            return {
                isManageShow: 1,
                inserttitle: '',
                modal: false,
            };
        },

        methods: {
            addmodalstart: function () {
                this.isManageShow = 0;

            },
            addmodal: function () {
                if (this.inserttitle.length > 0) {
                    this.modal = true;
                    this.isManageShow = 1;
                }
            },
            ok() {
                var instance = this;
                this.isManageShow = 1;
                var json = {
                    title: this.inserttitle,
                    list: [
                        {
                            name: '請更改....',
                            url: '#'
                        }
                    ]
                };
                if (this.administratorlist.indexOf(this.username) > -1) {
                    this.handleGetData({'key': 1, 'username': instance.username, 'title': instance.inserttitle, 'name': '请更改....', 'url': '#'}).then(function (value) {
                        if(value){
                            instance.$Message.success('添加成功');
                            location.reload();
                        }   
                    })
                } else {
                    this.handleGetApproveData({'key': 3, 'submitUsername': instance.username, 'moduleName': instance.inserttitle, 'urlName': '请更改....', 'url': '#'}).then(function (value) {
                        if(value){
                            instance.$Message.success('已添加到审批列表');
                            
                        }   
                    })
                }
                this.inserttitle = '';

            },
            cancel() {
                this.modal = 0;
                this.isManageShow = 0;


            },
            cancellManage() {

                this.isManageShow = 1;
                this.modal = false;
                this.title = '';
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
            handleGetApproveData(params) {
                var messsage = params;
                return new Promise((resolve, reject) => {
                    axios({
                        method: 'get',
                        url: 'http://release.baidu-int.com:8081/versionSign/duteamapprove',
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
        }
    };
</script>