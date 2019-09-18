<style>
    .ivu-card-body {
        height: 200px;

    }

    ul li {
        list-style-type: none;
    }

    ul {
        width: 100%;
        height: 100%;
    }

    .ivu-card {
        margin: 10px 10px 10px 10px;
    }

    .infoManage {
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

    .ivu-card-body {
        overflow: scroll;
    }

    .center {
        display: table-cell;
        vertical-align: middle;
        text-align: center;
    }
</style>
<template>
    <div>
        <Card >
            <p slot="title">
                {{mainData.title}}
            </p>
            <a href="#" slot="extra" @click="addInfo(mainData.title)">

                <Icon type="ios-add-circle" size="20" />
            </a>

            <ul>
                <li v-for="(item, index) in mainData.list">
                    <a :href="item.url" target="_blank" size='30'>{{ item.name }}</a>

                    <span :style="{float:'right'}">
                        <a href="#" @click="manage(item.name,item.url, item.title,item.id, index)"
                            v-if='isAdministrator'>
                            <Icon type="ios-construct-outline" />
                        </a>
                    </span>

                </li>
            </ul>
        </Card>
        <div v-bind:class="{infoManage:isShow}">
            <div class="overlayer"></div>
            <div class="wrap">
                <div class="modal">
                    <div class="content1">
                        <div class="moder-header">
                            管理链接信息
                        </div>
                        <div class="moder-body">
                            <div class="lable-item">
                                <Row>
                                    <Col span="4" class="center">
                                    <div >
                                        文字:
                                    </div>
                                    </Col>
                                    <Col span="20">
                                    <div>
                                        <Input type="text" v-model="name" />
                                    </div>
                                    </Col>
                                </Row>
                            </div>
                            <div class="lable-item">
                                <Row>
                                    <Col span="4" class="center">
                                    <div>
                                        链接：
                                    </div>
                                    </Col>
                                    <Col span="20">
                                    <div>
                                        <Input type="text" v-model="url" />
                                    </div>
                                    </Col>
                                </Row>
                            </div>
                        </div>
                        <div class="moder-footer">
                            <Button @click="cancellManage()">取消</Button>
                            <Button @click="add()" v-if="!showMove">添加</Button>
                            <Button @click="move()" v-if="showMove">删除</Button>
                            <Button @click="save()" v-if="showMove">保存</Button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <template>
            <Modal v-model="modal" :title=title @on-ok="ok" @on-cancel="cancel">
                <p>name：{{name}}</p>
                <p>url：{{url}}</p>
            </Modal>
        </template>
    </div>
</template>
<script>
    import axios from 'axios'
    export default {
        props: ['mainData', 'administratorlist', 'username', 'isAdministrator'],
        data() {
            return {
                isShow: 1, //是否弹出操作面板，1表示不，0表示弹出
                showMove: 0, // 0表示添加，1表示更改
                modaltitle: '', //操作模板的title
                name: '',  //操作list的名字
                url: '', //操作list的url
                modal: false, //是否弹出确认框，0表示不，1表示弹出
                title: '',  //表示弹出确认框的标题
                option: -1, //要做什么操作，0：删除，1：修改，2：添加。
                index: -1,
                id: -1 //操作部分的后端id
            }
        },
        methods: {
            addInfo(title) {
                this.isShow = 0;
                this.showMove = 0;
                this.modaltitle = title;
                console.log(this.isAdministrator);
            },
            manage(name, url, title, id, index) {
                this.isShow = 0;
                this.showMove = 1;
                this.name = name;
                this.url = url;
                this.index = index;
                this.id = id;
                this.modaltitle = title;

            },
            add() {
                // 新增一个url
                if (this.name.length > 0 && this.url.length > 0) {
                    this.option = 2;
                    this.modal = true;
                    this.isShow = 1;
                    this.title = "是否要添加";
                    this.modaltitle = this.mainData.title;
                }
                else {
                    this.$Message.warning('请填入url以及名称');

                }
            },
            save() {
                // 保存要更改的量
                if (this.name.length > 0 && this.url.length > 0) {
                    this.option = 1;
                    this.modal = true;
                    this.isShow = 1;
                    this.title = "是否保存更改";
                }
                else {
                    this.$Message.warning('请填入url以及名称');
                }

            },
            move() {
                // 移除变量
                if (this.name.length > 0 && this.url.length > 0) {
                    this.option = 0;
                    this.modal = true;
                    this.isShow = 1;
                    this.title = "是否要移除";
                }
                else {

                }

            },
            cancellManage() {
                this.isShow = 1;
            },
            cancel() {
                this.option = -1;
                this.modal = false;
                this.isShow = 1

            },
            ok() {
                var instance = this;
                if (this.option == 0) {
                    this.handleGetData({'key': 3, 'id': instance.id}).then(function (value) {
                        if (value) {
                            instance.$Message.success('删除成功');
                            location.reload();
                        }
                    })
                }
                else if (this.option == 1) {
                    this.handleGetData({'key': 2, 'username': 'admin', 'title': instance.modaltitle, 'name': instance.name, 'url': instance.url, 'id': instance.id}).then(function (value) {
                        if (value) {
                            instance.$Message.success('修改成功');
                            location.reload();
                        }
                    })

                }
                else if (this.option == 2) {
                    if (this.administratorlist.indexOf(this.username) > -1) {
                        this.handleGetData({'key': 1, 'username': instance.username, 'title': instance.modaltitle, 'name': instance.name, 'url': instance.url}).then(function (value) {
                            if (value) {
                                instance.$Message.success('添加成功');
                                location.reload();
                            }
                        })
                    } else {
                        this.handleGetApproveData({'key': 3, 'submitUsername': instance.username, 'moduleName': instance.modaltitle, 'urlName': instance.name, 'url': instance.url}).then(function (value) {

                            if (value) {
                                instance.$Message.success('添加到审批列表成功');
                                location.reload();
                            }
                        })
                    }

                } else {

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
    }
</script>