<style>
    .approveManage {
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

    .content {
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

    .lable {
        float: right;
    }
</style>
<template>
    <div>
        <div v-bind:class="{approveManage:propApproveManageIsActive}" id="versionManage">
            <div class="overlayer"></div>
            <div class="wrap">
                <div class="modal">
                    <div class="content">
                        <div class="moder-header">
                            审批列表
                        </div>
                        <div class="moder-body">
                            <div v-if='isAdministrator'>
                                <template>
                                    <Table height='300' :columns='columnsadministrator' :data='approveData'>
                                        <template slot-scope="{ row, index }" slot="moduleName">
                                            <span>{{ row.moduleName }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="urlName">
                                            <span>{{ row.urlName }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="url">
                                            <span>{{ row.url }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="submitUsername">
                                            <span>{{ row.submitUsername }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="submitTime">
                                            <span>{{ row.submitTime }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="action">
                                            <div v-if="row.isAccept == 'nullvalue'">
                                                <Row>
                                                    <Col span="10">
                                                    <Button @click="handleReject(row)">拒绝</Button>
                                                    </Col>
                                                    <Col span="10" offset='2'>
                                                    <Button @click="handleAccept(row)">通过</Button>
                                                    </Col>
                                                </Row>
                                            </div>
                                            <div v-else>
                                                    <span v-if="row.isAccept == '是'">已通过</span>
                                                    <span v-else>已打回</span>
                                            </div>

                                        </template>
                                    </Table>
                                </template>
                            </div>
                            <div v-else>
                                <template>
                                    <Table height='300' :columns='columnsnotadministrator' :data='approveData'>
                                        <template slot-scope="{ row, index }" slot="moduleName">
                                            <span>{{ row.moduleName }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="urlName">
                                            <span>{{ row.urlName }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="url">
                                            <span>{{ row.url }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="submitUsername">
                                            <span>{{ row.submitUsername }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="submitTime">
                                            <span>{{ row.submitTime }}</span>
                                        </template>
                                        <template slot-scope="{ row, index }" slot="state">
                                            <span v-if="row.isAccept == '是'">已通过</span>
                                            <span v-else-if="row.isAccept == '否'">已打回</span>
                                            <span v-else>未审批</span>

                                        </template>
                                    </Table>
                                </template>
                            </div>
                        </div>
                        <div class="moder-footer">
                            <Button @click="cancellManage()">确定</Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <template>

            <Modal v-model="modal" :title=title @on-ok="ok" @on-cancel="cancel">
                <p>模块名：{{moduleName}}</p>
                <p>名称：{{urlName}}</p>
                <p>URL：{{url}}</p>
                <p>提交人：{{submitUsername}}</p>
                <p>提交时间：{{submitTime}}</p>

            </Modal>
        </template>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        props: ['approveData', 'administrator', 'propApproveManageIsActive', 'username', 'isAdministrator'],
        data() {
            return {

                columnsadministrator: [
                    {
                        title: '模块名',
                        slot: 'moduleName',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: '名称',
                        slot: 'urlName',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: 'URL',
                        slot: 'url',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: '提交人',
                        slot: 'submitUsername',
                        width: 100,
                        align:'center'
                    },
                    {
                        title: '提交时间',
                        slot: 'submitTime',
                        width: 100,
                        align:'center'
                    },
                    {
                        title: '操作',
                        slot: 'action',
                        width: 150,
                        align:'center',
                        fixed: 'right'
                    },
                ],
                columnsnotadministrator: [
                    {
                        title: '模块名',
                        slot: 'moduleName',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: '名称',
                        slot: 'urlName',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: 'URL',
                        slot: 'url',
                        width: 200,
                        align:'center'
                    },
                    {
                        title: '提交人',
                        slot: 'submitUsername',
                        width: 100,
                        align:'center'
                    },
                    {
                        title: '提交时间',
                        slot: 'submitTime',
                        width: 100,
                        align:'center'
                    },
                    {
                        title: '状态',
                        slot: 'state',
                        width: 100,
                        align:'center'
                    }
                ],
                approveIsActive: 1, //判断新增版本窗口是否正常展示
                moduleName: '',
                urlName: '',
                url: '',
                submitUsername: '',
                submitTime: '',

                modal: false, //确定对话框是否展示
                handleKey: -1, //// key值控制后端做何中操作，0：拒绝，1，同意， 
                title: '',
                topic: '',   //提示的topic展示词，以及传输到后端的topic
                id: -1,

            }
        },
        methods: {


            ok() {
                var instance = this;
                if (this.handleKey == 0) {
                    this.$options.methods.handleGetData({key: '0', id: instance.id}).then(function (value) {
                        if(value){
                            instance.$Message.success('审批完成，已拒绝');
                            location.reload();
                        }   
                    })
                }
                else {
                    this.$options.methods.handleGetData({key: '1', id: instance.id, urlName: instance.urlName, url: instance.url, submitUsername: instance.submitUsername, moduleName: instance.moduleName}).then(function (value) {
                        if(value){
                            instance.$Message.success('审批完成，已接受');
                            location.reload();
                        }   
                    })
                }


            },
            cancel() {

            },
            cancellManage() {
                this.$emit('listenapproveisactive', 1);
            },
            handleGetData(params) {
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
            handleReject(row) {
                console.log(row);
                this.moduleName = row.moduleName;
                this.urlName = row.urlName;
                this.url = row.url;
                this.submitUsername = row.submitUsername;
                this.submitTime = row.submitTime;
                this.modal = true;
                this.handleKey = 0;
                this.id = row.id;
                this.title = '确定打回？';
                this.$emit('listenapproveisactive', 1);
                // this.$options.handleGetData({key:'0'}).then(function(value){
                //     console.log('审批不通过后的结果'+value);
                // })
            },
            handleAccept(row) {
                console.log(row);
                this.moduleName = row.moduleName;
                this.urlName = row.urlName;
                this.url = row.url;
                this.submitUsername = row.submitUsername;
                this.submitTime = row.submitTime;
                this.modal = true;
                this.handleKey = 1;
                this.id = row.id;
                this.title = '确定通过？';
                this.$emit('listenapproveisactive', 1);
                // this.$options.handleGetData({key:'1',urlName:row.urlName, url:row.url, submitUsername: row.submitUsername,moduleName: row.moduleName}).then(function(value){
                //     console.log('审批不通过后的结果'+value);
                // })
            }

        }
    }
</script>