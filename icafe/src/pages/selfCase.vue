<style scoped>
    #index {
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }
    .logo-frame {
        margin: 1rem 0 1rem 0;
    }
    p {
        text-align: center;
        font-size: 2rem;
    }
    h1 {
        font-weight: normal;
    }
    .content {
        height: 100%;
        overflow: auto;
        background: #fff;
        padding: 10px 20px;
        margin: 0;
    }
    .line {
        width: 100%;
        border-bottom: 3px solid #FFC125;
    }
</style>
<template>
    <div>
        <template>
            <Modal v-model="showcase" :title='modalTitle' @on-ok="ok" @on-cancel="cancel">
                {{selfcase}}
            </Modal>
        </template>
        <div id="index">
            <div class="select">
                <template>
                    <Row>
                        </Col>
                        <Col span="10" offset='4' align="center">
                        请选择版本号:
                        <template>
                            <Select v-model="version" style="width:200px">
                                <Option v-for="item in versionList" :value="item.value" :key="item.value">
                                    {{ item.label }}
                                </Option>
                            </Select>
                        </template>
                        <!-- <Input v-model="condition" placeholder="Enter version" style="width: 400px" /> -->
                        </Col>
                        <Col span="4" offset='2' align="center">
                        <Button @click="check()" :style="{color:'#FFA500'}">查询</Button>
                        </Col>
                    </Row>
                    <br />
                    <br />
                    <Row>
                        <Col offset='2' span="20">
                        <div class="line"></div>
                        </Col>
                    </Row>
                    <br />
                </template>
                <div class="content">
                    <template>
                        <Row>
                            <Col offset='1' span='2' align="center">
                            负责人
                            </Col>
                            <Col offset='1' span='2' align="center">
                            创建人
                            </Col>
                            <Col span='5' offset='1' align="center">
                            卡片标题
                            </Col>
                            <Col span='6' offset='1' align="center">
                            自测case
                            </Col>
                            <Col offset='1' span="2" align="center">
                            操作
                            </Col>
                        </Row>
                        <br />
                        <br />
                        <template>
                            <div v-for="(items,name) in list">
                                <div v-for="item in items">
                                    <Row align="middle">
                                        <Col offset='1' span='2' align="center">
                                        {{name}}
                                        </Col>
                                        <Col offset='1' span='2' align="center">
                                        {{item.createdUser.name}}
                                        </Col>
                                        <Col span='5' offset='1' align="center">
                                        <Input v-model=item.title>
                                        </Input>
                                        </Col>
                                        <Col span='6' offset='1' align="center">
                                        <Input v-model=item.case>
                                        </Input>
                                        </Col>
                                        <Col offset='1' span="2" align="center">
                                        <Button @click="info(item.title, item.case)">查看</Button>
                                        </Col>
                                    </Row>
                                    <br>
                                </div>
                            </div>
                        </template>

                    </template>
                </div>
            </div>
        </div>
    </div>
</template>
</div>
</div>
</div>
</template>
<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                version: '',
                condition: '',
                list: {},
                versionList: [
                    {
                        label: '11.9',
                        value: '11.9'
                    },
                    {
                        label: '11.10',
                        value: '11.10'
                    },
                    {
                        label: '11.11',
                        value: '11.11'
                    },
                    {
                        label: '11.12',
                        value: '11.12'
                    }
                ],
                selfcase: '',
                showcase: false,
                modalTitle: ''
            };
        },
        methods: {
            ok() {},
            cancel() {},
            info(title, selfcase) {
                console.log(title + selfcase);
                this.modalTitle = title;
                this.selfcase = selfcase;
                this.showcase = true;
            },
            strToJson(str) {
                var json = eval('(' + str + ')');
                return json;
            },
            check() {
                var instance = this;
                this.$Spin.show();
                var condition = "包含下级空间数据 = true AND 类型 = Feature AND ((子空间所属计划 ~ " + this.version + "版本) OR (随版版本 = " + this.version + " AND (空间 = 小程序[xiaochengxu00] OR 空间 = 小程序游戏[minigame01])))"
                // var condition = this.condition.replace(/"/g, '\\"');
                console.log(condition);
                this.$options.methods.handleGetData({'condition': condition}).then(function (value) {
                    console.log(value);
                    instance.list = value;
                    instance.$Spin.hide();
                    // console.log(instance.list);
                })
            },
            handleGetData(params) {
                var messsage = params;
                return new Promise((resolve, reject) => {
                    axios({
                        method: 'get',
                        url: 'http://release.baidu-int.com:8081/versionSign/icafeCheck',
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