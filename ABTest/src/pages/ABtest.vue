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
        border-bottom: 3px solid #66CD00;
    }

    .active {
        color: #66CD00;
    }

    .makeGrey {
        pointer-events: none;
        opacity: 0.5;
    }

    .title {
        background: #fff;
        margin-left: 100px;
        margin-right: 100px;
    }

    .tableContent {
        margin-left: 100px;
        margin-right: 100px;
    }

    .col {
        height: 35px;
        display: flex;
        align-items: center;


    }

    .col-content {}

    .title-odd {
        height: 35px;
        background: #66CD00;
        display: flex;
        align-items: center;

    }

    .title-even {
        height: 35px;
        background: #66CD00;
        display: flex;
        align-items: center;
    }

    .page {
        text-align: center;
    }
</style>
<template>
    <div>
        <template>
            <Modal v-model="showcase" :title='modalTitle' @on-ok="ok" @on-cancel="cancel">
                {{selfcase}}
            </Modal>
        </template>
        <div>
            <div>
                <template>
                    <br />
                    <br />
                    <Row>
                        </Col>
                        <Col span="5" offset='2' align="center">
                        <div @click="changeState(1)" :class="{'active':isactive1}">全部AB试验</div>

                        </Col>
                        <Col span="5" align="center">
                        <div @click="changeState(2)" :class="{'active':isactive2}">灰度风险</div>
                        </Col>
                        <Col span="5" align="center">
                        <div @click="changeState(3)" :class="{'active':isactive3}">发版风险</div>
                        </Col>
                        <Col span="5" align="center">
                        <div @click="changeState(4)" :class="{'active':isactive4}">自助查询</div>
                        </Col>
                    </Row>

                    <br />
                    <Row>
                        <Col offset='2' span="20">
                        <div class="line"></div>
                        </Col>
                    </Row>
                    <br />
                </template>
                <Row>
                    <div v-if='notSelfQuery'>
                        <Col span="4" offset="2" :class="{'makeGrey':isGrey[0]}" class="col">
                        <Row>
                            <Col span="12" align="right">
                            线上对比版本号：
                            </Col>
                            <Col span="12" align="left">
                            <input type="text" v-model='onlineNumEdit'>
                            </Col>

                        </Row>
                        </Col>
                        <Col span="4" :class="{'makeGrey':isGrey[1]}" class="col">
                        <Row>
                            <Col span="12" align="right">
                            灰度版本号:
                            </Col>
                            <Col span="12" align="left">
                            <input type="text" v-model='greyNumEdit'>
                            </Col>

                        </Row>
                        </Col>
                        <Col span="4" :class="{'makeGrey':isGrey[2]}" class="col">
                        <Row>
                            <Col span="12" align="right">
                            发版版本号：
                            </Col>
                            <Col span="12" align="left">
                            <input type="text" v-model='releaseNumEdit'>
                            </Col>

                        </Row>
                        </Col>
                        <Col span="4" offset="1" :class="{'makeGrey':isGrey[3]}" class="col">
                        <Row>
                            <Col span="12" align="right" class="col">
                            风险筛选：
                            </Col>
                            <Col span="12" align="left">
                            <Select v-model="risk" style="width:100px">
                                <Option v-for="item in riskList" :value="item.value" :key="item.value">{{ item.label }}
                                </Option>
                            </Select>
                            </Col>

                        </Row>
                        </Col>
                    </div>
                    <div v-else>
                        <Col span="16" offset='2'>
                        <Col span="4" align="right">
                        输入条件：
                        </Col>
                        <Col span="20" align="left">
                        <Input type="text" v-model='sqlQuery' width="400px"></Input>
                        </Col>
                        </Col>
                    </div>
                    <Col align="center" span="4">
                    <Button @click="query()" shape="circle" icon="ios-search"></Button>
                    </Col>
                </Row>
                <div>
                    <template>
                        <Row class="title">
                            <Col span='1' align="left" class="title-odd">
                            ID
                            </Col>
                            <Col span='5' align="left" class="title-even">
                            标题
                            </Col>
                            <Col span='2' align="left" class="title-odd">
                            负责人
                            </Col>
                            <Col span='3' align="left" class="title-even">
                            分支细节
                            </Col>
                            <Col span="3" align="left" class="title-odd">
                            开关
                            </Col>
                            <Col span="2" align="left" class="title-even">
                            流量层
                            </Col>
                            <Col span="1" align="left" class="title-odd">
                            偏差
                            </Col>
                            <Col span="1" align="left" class="title-even">
                            流量合
                            </Col>
                            <Col span="2" align="left" class="title-odd">
                            离目前天数
                            </Col>
                            <Col span="2" align="left" class="title-even">
                            <div @click="sort()">
                                <div v-if="sortLable == 0">
                                    风险标识
                                    <Icon type="ios-arrow-forward" />
                                </div>
                                <div v-else-if="sortLable == -1">
                                    风险标识
                                    <Icon type="ios-arrow-down" />
                                </div>
                                <div v-else="sortLable == 1">
                                    风险标识
                                    <Icon type="ios-arrow-up" />
                                </div>
                            </div>


                            </Col>
                            <Col span="2" align="left" class="title-odd">
                                插入时间
                                </Col>

                        </Row>

                        <template>
                            <div v-for="(item,name) in correntList" class="tableContent">

                                <Row type="flex" justify="center" align="middle">
                                    <Col span='1' align="middle" class="col">


                                    <a href="javascript:void(0)" @click="jump(item.EID)"
                                        class="col-content">{{item.EID}}</a>

                                    </Col>
                                    <Col span='5' align="left" class="col">
                                    <a href="javascript:void(0)" @click="jump(item.EID)">{{item.TITLE}}</a>
                                    </Col>
                                    <Col span='2' align="left" class="col">

                                    <!-- <input type="text" readonly style="border-style:none;" v-model="item.OWNER"> -->
                                    <Poptip trigger="hover" :content=item.OWNER>
                                        <input type="text" readonly style="border-style:none;" v-model="item.OWNER">
                                    </Poptip>
                                    </Col>
                                    <Col span='3' align="left" class="col">
                                    <!-- <input type="text" readonly style="border-style:none;" v-model="item.BRANCH"> -->
                                    <Poptip trigger="hover" :content=item.BRANCH>
                                        <input type="text" readonly style="border-style:none;" v-model="item.BRANCH">
                                    </Poptip>

                                    </Col>
                                    <Col span="3" align="left" class="col">
                                    <Poptip trigger="hover" :content=item.SWITCH>
                                        <input type="text" readonly style="border-style:none;" v-model="item.SWITCH">
                                    </Poptip>
                                    </Col>
                                    <Col span="2" align="left" class="col">
                                    <Poptip trigger="hover" :content=item.LAYER>
                                        <input type="text" readonly style="border-style:none;" v-model="item.LAYER">
                                    </Poptip>
                                    </Col>
                                    <Col span="1" align="left" class="col">
                                    {{item.DEVIATION}}
                                    </Col>
                                    <Col span="1" align="left" class="col">
                                    {{item.SUM}}
                                    </Col>
                                    <Col span="2" align="left" class="col">
                                    {{item.DAYS_DIFF}}
                                    </Col>
                                    <Col span="2" align="left" class="col">
                                    {{item.RISK}}
                                    </Col>
                                    <Col span="2" align="left" class="col">
                                        <Poptip trigger="hover" :content=item.INSERT_TIME>
                                            <input type="text" readonly style="border-style:none;" v-model="item.INSERT_TIME">
                                        </Poptip>
                                        </Col>
                                </Row>
                                <br>

                            </div>
                        </template>


                    </template>

                </div>
                <div class="page">
                    <template>
                        <Page :total=listLength show-total :current=correntPage :page-size=pageSize
                            @on-change='changePage' />
                    </template>
                </div>
                <br />
                <br />
                <br />
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
                list: [],
                correntList: [],
                listLength: -1,
                pageSize: 20,
                correntPage: 1,
                selfcase: '',
                modalState: 1, //存储当前为什么状态，1全部AB试验，2灰度风险，3发版风险
                showcase: false,
                modalTitle: '',
                isactive1: true,
                isactive2: false,
                isactive3: false,
                isactive4: false,
                notSelfQuery: true, //true时，非自助查询
                defaultOnlineNum: '',
                defaultGreyNum: '',
                defaultReleaseNum: '',
                onlineNumEdit: '', //线上比对版本号
                greyNumEdit: '', //灰度版本号
                releaseNumEdit: '',//发版版本号
                isGrey: [false, true, true, false],//使版本号编辑为置灰

                sqlQuery: 'SELECT * FROM AbtestCheck WHERE ( ROUND = (select MAX(ROUND) FROM AbtestCheck where ROUND < (SELECT MAX(ROUND) FROM AbtestCheck)) ) AND (SUM > 50) AND (DAYS_DIFF < 20) AND (START_VERSION >=11001200000000000 AND START_VERSION<=11001200000099000 AND END_VERSION>=11001200000001000 );',
                risk: '-1',
                isQueryBySql: false,
                sortLable: 0,
                riskList: [
                    {
                        value: '-1',
                        label: '全部'
                    },
                    {
                        value: '0',
                        label: '0'
                    },
                    {
                        value: '1',
                        label: '1'
                    },
                    {
                        value: '2',
                        label: '2'
                    },
                    {
                        value: '3',
                        label: '3'
                    },
                    {
                        value: '4',
                        label: '4'
                    },
                    {
                        value: '5',
                        label: '5'
                    },
                    {
                        value: '6',
                        label: '6'
                    },
                    {
                        value: '7',
                        label: '7'
                    },
                    {
                        value: '8',
                        label: '8'
                    },
                    {
                        value: '9',
                        label: '9'
                    },
                    {
                        value: '10',
                        label: '10'
                    },
                    {
                        value: '11',
                        label: '11'
                    },
                    {
                        value: '12',
                        label: '12'
                    },
                    {
                        value: '13',
                        label: '13'
                    },
                    {
                        value: '14',
                        label: '14'
                    },
                    {
                        value: '15',
                        label: '15'
                    }
                ]
            };
        },

        created() {
            var instance = this;
            this.$Spin.show();
            this.$options.methods.handleGetData({'key': 5}).then(function (value) {
                //console.log(value);

                instance.releaseNumEdit = instance.$options.methods.changeStrToNum(value[0].releaseNum);
                instance.defaultReleaseNum = instance.$options.methods.changeStrToNum(value[0].releaseNum);

                instance.greyNumEdit = instance.$options.methods.changeStrToNum(value[0].greyNum);
                instance.defaultGreyNum = instance.$options.methods.changeStrToNum(value[0].greyNum);
                instance.onlineNumEdit = instance.$options.methods.changeStrToNum(value[0].onlineNum);
                instance.defaultOnlineNum = instance.$options.methods.changeStrToNum(value[0].onlineNum);
                instance.$options.methods.handleGetData({'risk': instance.risk, 'key': 1, 'onlineNum': instance.$options.methods.changeNumToStr(instance.$options.methods.changeStrToNum(value[0].onlineNum)), 'greyNum': instance.$options.methods.changeNumToStr(instance.$options.methods.changeStrToNum(value[0].greyNum)), 'releaseNum': instance.$options.methods.changeNumToStr(instance.$options.methods.changeStrToNum(value[0].releaseNum))}).then(function (value) {

                    instance.list = value;
                    instance.listLength = value.length;
                    instance.correntList = value.slice(0, 20);
                    console.log(value);

                    instance.$Spin.hide();
                    let listLength = instance.list.length;
                    for (let i = 0; i < listLength; i++) {
                        if (instance.list[i]['OWNER'].length > 0) {
                            let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                            let name = '';
                            for (let j = 0; j < username.length; j++) {
                                instance.$options.methods.getuser(username[j]).then(function (value) {
                                    name += value.name + ' ';

                                    instance.list[i]['OWNER'] = name;
                                });
                            }


                        }

                    }


                }
                );
            });
        },
        methods: {
            changePage(index) {
                this.$Spin.show();
                this.correntPage = index;
                var list = this.list;
                if (index > this.listLength / 20) {
                    this.correntList = this.list.slice((index - 1) * 20);
                }
                else {
                    this.correntList = this.list.slice((index - 1) * 20, (index) * 20);
                }
                console.log(index);
                console.log(this.list);
                this.$Spin.hide();
            },

            jump(eid) {
                var href = "http://abtesting.baidu.com/static/aunceladmin/app.html#/experiment/18/" + eid;
                window.open(href);

            },
            sort() {

                this.$Spin.show();
                var sortLable = this.sortLable;
                var instance = this;
                if (sortLable == 0 || sortLable == -1) {
                    this.sortLable = 1;
                    this.list = instance.$options.methods.quickSortDown(instance.list);

                }
                else {
                    this.sortLable = -1;
                    this.list = instance.$options.methods.quickSortUp(instance.list);
                }
                var list = this.list;
                this.correntPage = 1;
                this.correntList = this.list.slice(0, 20);
                this.$Spin.hide();
            },
            changeState(num) {
                this.$Spin.show();
                if (num == 1) {
                    var instance = this;
                    this.isactive1 = true;
                    this.isactive2 = false;
                    this.isactive3 = false;
                    this.isactive4 = false;
                    this.isGrey = [false, true, true, false];
                    this.notSelfQuery = true;
                    this.modalState = 1;

                    this.isQueryBySql = false;

                    this.$options.methods.handleGetData({'risk': instance.risk, 'key': 1, 'onlineNum': instance.$options.methods.changeNumToStr(instance.onlineNumEdit), 'greyNum': instance.$options.methods.changeNumToStr(instance.greyNumEdit), 'releaseNum': instance.$options.methods.changeNumToStr(instance.releaseNumEdit)}).then(function (value) {
                        //console.log(value);
                        instance.list = value;
                        instance.$Spin.hide();
                        // console.log(instance.list);
                        let listLength = instance.list.length;
                        for (let i = 0; i < listLength; i++) {
                            if (instance.list[i]['OWNER'].length > 0) {
                                let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                                let name = '';
                                for (let j = 0; j < username.length; j++) {
                                    instance.$options.methods.getuser(username[j]).then(function (value) {
                                        //console.log(value.name);
                                        name += value.name + ' ';

                                        instance.list[i]['OWNER'] = name;
                                    });
                                }


                            }

                        }
                        instance.listLength = instance.list.length;
                        instance.correntPage = 1;
                        instance.correntList = instance.list.slice(0, 20);
                    })
                }
                else if (num == 2) {
                    var instance = this;
                    this.isactive1 = false;
                    this.isactive2 = true;
                    this.isactive3 = false;
                    this.isactive4 = false;
                    this.isGrey = [0, 0, 1, 0];
                    this.isQueryBySql = false;
                    this.notSelfQuery = true;
                    this.modalState = 2;
                    //console.log(this.isGrey);
                    this.$options.methods.handleGetData({'risk': instance.risk, 'key': 2, 'onlineNum': instance.$options.methods.changeNumToStr(instance.onlineNumEdit), 'greyNum': instance.$options.methods.changeNumToStr(instance.greyNumEdit), 'releaseNum': instance.$options.methods.changeNumToStr(instance.releaseNumEdit)}).then(function (value) {
                        //console.log(value);
                        instance.list = value;
                        instance.$Spin.hide();
                        // console.log(instance.list);

                        let listLength = instance.list.length;
                        for (let i = 0; i < listLength; i++) {
                            if (instance.list[i]['OWNER'].length > 0) {
                                let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                                let name = '';
                                for (let j = 0; j < username.length; j++) {
                                    instance.$options.methods.getuser(username[j]).then(function (value) {
                                        //console.log(value.name);
                                        name += value.name + ' ';
                                        //console.log(name);
                                        instance.list[i]['OWNER'] = name;
                                    });
                                }


                            }

                        }
                        instance.listLength = instance.list.length;
                        instance.correntPage = 1;
                        instance.correntList = instance.list.slice(0, 20);
                    })
                }
                else if (num == 3) {
                    var instance = this;
                    this.isactive1 = false;
                    this.isactive2 = false;
                    this.isactive3 = true;
                    this.isactive4 = false;
                    this.isGrey = [0, 1, 0, 0];
                    this.notSelfQuery = true;
                    this.isQueryBySql = false;
                    this.modalState = 3;
                    this.$options.methods.handleGetData({'risk': instance.risk, 'key': 3, 'onlineNum': instance.$options.methods.changeNumToStr(instance.onlineNumEdit), 'greyNum': instance.$options.methods.changeNumToStr(instance.greyNumEdit), 'releaseNum': instance.$options.methods.changeNumToStr(instance.releaseNumEdit)}).then(function (value) {
                        console.log(value);
                        instance.list = value;
                        instance.$Spin.hide();
                        // console.log(instance.list);
                        let listLength = instance.list.length;
                        for (let i = 0; i < listLength; i++) {
                            if (instance.list[i]['OWNER'].length > 0) {
                                let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                                let name = '';
                                for (let j = 0; j < username.length; j++) {
                                    instance.$options.methods.getuser(username[j]).then(function (value) {
                                        //console.log(value.name);
                                        name += value.name + ' ';
                                        //console.log(name);
                                        instance.list[i]['OWNER'] = name;
                                    });
                                }


                            }

                        }
                        instance.listLength = instance.list.length;
                        instance.correntPage = 1;
                        instance.correntList = instance.list.slice(0, 20);
                    })

                }
                else {
                    var instance = this;
                    this.isactive1 = false;
                    this.isactive2 = false;
                    this.isactive3 = false;
                    this.isactive4 = true;
                    this.notSelfQuery = false;
                    this.isQueryBySql = true;
                    instance.$Spin.hide();

                }

            },
            ok() {},
            cancel() {},
            info(title, selfcase) {
                //console.log(title + selfcase);
                this.modalTitle = title;
                this.selfcase = selfcase;
                this.showcase = true;
            },
            strToJson(str) {
                var json = eval('(' + str + ')');
                return json;
            },
            query() {
                var instance = this;
                instance.$Spin.show();
                if (this.isQueryBySql) {


                    //key=6时，按照sql语句进行查询
                    this.$options.methods.handleGetData({'risk': instance.risk, 'key': 6, 'sql': instance.sqlQuery}).then(function (value) {
                        console.log(value);
                        if (value) {
                            instance.list = value;
                            instance.listLength = instance.list.length;
                            let listLength = instance.list.length;
                            for (let i = 0; i < listLength; i++) {
                                if (instance.list[i]['OWNER'].length > 0) {
                                    let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                                    let name = '';
                                    for (let j = 0; j < username.length; j++) {
                                        instance.$options.methods.getuser(username[j]).then(function (value) {
                                            //console.log(value.name);
                                            name += value.name + ' ';
                                            //console.log(name);
                                            instance.list[i]['OWNER'] = name;
                                        });
                                    }


                                }

                            }
                            instance.correntPage = 1;
                            instance.correntList = instance.list.slice(0, 20);
                        }
                        else {

                            instance.$Message.success("请检查查询语句是否正确，拒绝select * from AbtestCheck;");
                        }



                        // instance.list = value;
                        instance.$Spin.hide();
                        // console.log(instance.list);

                    })

                }
                else {
                    if (instance.$options.methods.regMatch(instance.onlineNumEdit) && instance.$options.methods.regMatch(instance.releaseNumEdit) && instance.$options.methods.regMatch(instance.greyNumEdit)) {
                        let onlinenum = instance.$options.methods.changeNumToStr(instance.onlineNumEdit);
                        let greynum = instance.$options.methods.changeNumToStr(instance.greyNumEdit);
                        let releasenum = instance.$options.methods.changeNumToStr(instance.releaseNumEdit);
                        //console.log({'key': instance.modalState, 'onlineNum': onlinenum, 'greyNum': greynum, 'releaseNum': releasenum});
                        this.$options.methods.handleGetData({'risk': instance.risk, 'key': instance.modalState, 'onlineNum': onlinenum, 'greyNum': greynum, 'releaseNum': releasenum}).then(function (value) {
                            //instance.$Message.success("这是一个预留改变版本号的查询口");
                            //console.log(value);

                            instance.list = value;
                            //console.log(instance.$options.methods.quickSort(value));
                            instance.$Spin.hide();
                            // console.log(instance.list);
                            let listLength = instance.list.length;
                            for (let i = 0; i < listLength; i++) {
                                if (instance.list[i]['OWNER'].length > 0) {
                                    let username = instance.list[i]['OWNER'].replace(/^&/, '').split('&');

                                    let name = '';
                                    for (let j = 0; j < username.length; j++) {
                                        instance.$options.methods.getuser(username[j]).then(function (value) {
                                            //console.log(value.name);
                                            name += value.name + ' ';
                                            //console.log(name);
                                            instance.list[i]['OWNER'] = name;
                                        });
                                    }


                                }

                            }
                            instance.listLength = instance.list.length;
                            instance.correntPage = 1;
                            instance.correntList = instance.list.slice(0, 20);
                        })
                    }

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
            regMatch(str) {
                var matchStr = /^\d{1,2}\.\d{1,2}\.\d{1,2}$/;
                return matchStr.test(str);
            },
            changeNumToStr(str) {
                var array = str.split('.');
                for (let i = 1; i < 3; i++) {
                    if (array[i].length == 1) {
                        array[i] = '000' + array[i];
                    } else {
                        array[i] = '00' + array[i];
                    }


                }
                //console.log(["" + array[0] + array[1] + array[2] + '0000000', "" + array[0] + array[1] + array[2] + '0099000', "" + array[0] + array[1] + array[2] + '0001000']);

                return ["" + array[0] + array[1] + array[2] + '0000000', "" + array[0] + array[1] + array[2] + '0099000', "" + array[0] + array[1] + array[2] + '0001000'];


            },
            changeStrToNum(str) {
                let one = str.substring(0, 2);
                let two = str.substring(2, 6).replace(/^0+/, '');
                two = two.length == 0 ? '0' : two;
                let three = str.substring(6, 10).replace(/^0+/, '');
                three = three.length == 0 ? '0' : three;
                //console.log(one + '.' + two + '.' + three);
                return one + '.' + two + '.' + three;

            },
            getuser(info) {
                var instance = this;
                //console.log(this.selectlist);
                return new Promise((resolve, reject) => {
                    axios({
                        method: 'get',
                        url: 'http://release.baidu-int.com:8081/versionSign/querynamebyusername',
                        params: {
                            username: info
                        }
                    }).then(response => {
                        resolve(response.data.result);
                    }).catch(error => {
                        reject(error);
                    })
                })
            },
            quickSortUp(arr) {
                var instance = this;
                var len = arr.length;
                for (let i = 0; i < len - 1; i++) {
                    for (let j = 0; j < len - i - 1; j++) {
                        if (arr[j]['RISK'] > arr[j + 1]['RISK']) {
                            var swap = arr[j];
                            arr[j] = arr[j + 1];
                            arr[j + 1] = swap;
                        }
                    }
                }
                return arr;



                // if (arr.length < 2) {return arr;}
                // // 定义左指针
                // var left = 0;
                // // 定义右指针
                // var right = arr.length - 1;
                // //开启每一轮的排序
                // while (left < right) {
                //     // 寻找右边比arr[0]小的数的下标
                //     console.log(arr[right]);
                //     while (arr[right]['RISK'] >= arr[0]['RISK'] && left < right) {
                //         right = right - 1;
                //     }
                //     // 寻找左边比arr[0]大的数的下标
                //     while (arr[left]['RISK'] <= arr[0]['RISK'] && left < right) {
                //         left++;
                //     }
                //     //当左边指针与右边指针相遇后，交换arr[0]与当前两个指针所在的元素
                //     if (right == left) {
                //         let mid = arr[right];
                //         arr[right] = arr[0];
                //         arr[0] = mid;
                //         break;
                //     }
                //     // 当左指针小于右指针的位置，交换两个指针当前位置的元素
                //     let tem = arr[right];
                //     arr[right] = arr[left];
                //     arr[left] = tem;
                // }
                // //递归实现
                // return instance.$options.methods.quickSortUp(arr.slice(0, left)).concat(arr.slice(left, right + 1)).concat(instance.$options.methods.quickSortUp(arr.slice(right + 1)));
            },
            quickSortDown(arr) {


                var instance = this;
                var len = arr.length;
                for (let i = 0; i < len - 1; i++) {
                    for (let j = 0; j < len - i - 1; j++) {
                        if (arr[j]['RISK'] < arr[j + 1]['RISK']) {
                            var swap = arr[j];
                            arr[j] = arr[j + 1];
                            arr[j + 1] = swap;
                        }
                    }
                }
                return arr;


                // var instance = this;
                // if (arr.length < 2) {return arr;}
                // // 定义左指针
                // var left = 0;
                // // 定义右指针
                // var right = arr.length - 1;
                // //开启每一轮的排序
                // while (left < right) {
                //     // 寻找右边比arr[0]大的数的下标
                //     console.log(arr[right]);
                //     while (arr[right]['RISK'] <= arr[0]['RISK'] && left < right) {
                //         right = right - 1;
                //     }
                //     // 寻找左边比arr[0]小的数的下标
                //     while (arr[left]['RISK'] >= arr[0]['RISK'] && left < right) {
                //         left++;
                //     }
                //     //当左边指针与右边指针相遇后，交换arr[0]与当前两个指针所在的元素
                //     if (right == left) {
                //         let mid = arr[right];
                //         arr[right] = arr[0];
                //         arr[0] = mid;
                //         break;
                //     }
                //     // 当左指针小于右指针的位置，交换两个指针当前位置的元素
                //     let tem = arr[right];
                //     arr[right] = arr[left];
                //     arr[left] = tem;
                // }
                // //递归实现
                // return instance.$options.methods.quickSortDown(arr.slice(0, left)).concat(arr.slice(left, right + 1)).concat(instance.$options.methods.quickSortDown(arr.slice(right + 1)));
            }
        }
    }

</script>