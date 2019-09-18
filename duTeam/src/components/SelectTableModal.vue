<template>
    <Modal v-model="modalShow" width="600" :title="modalTitle" @on-ok="selectOk" @on-cancel="selectCancel">
        <div class="slot-panel">
            <slot name="search_panel"></slot>
        </div>
        <div v-if="selectType == 'mutiple'" class="table-tab">
            <Button-group>
                <Button @click="toggleType" :type="tableType.left">待选</Button>
                <Button @click="toggleType" :type="tableType.right">已选({{this.selectedDataset.length}})</Button>
            </Button-group>
        </div>
        <Table :highlight-row="selectType == 'single'" size="small" :columns="tableColumnSet" :data="tableDataset"
            height="300" @on-current-change="tableOnCurrentChange"></Table>
        <div v-show="tableType.isLeft" class="page-panel">
            <Page class="page-view" :total="datasetTotal" :current="currentIndex" :page-size="datasetPagesize"
                size="small" @on-change="onIndexChange" show-total></Page>
        </div>
    </Modal>
</template>

<style scoped>
    .table-tab {
        width: 100%;
        padding-bottom: 10px;
    }

    .page-panel {
        width: 100%;
        padding: 15px 0;
        text-align: center;
    }

    .page-view {
        float: right;
    }

    .slot-panel {
        width: 100%;
    }
</style>

<script>
    export default {
        props: {
            dataset: Array,                                     //表格数据源
            selectedDataset: {                                  //已选择表格数据源
                type: Array,
                default: function () {
                    return [];
                }
            },
            datasetTotal: {type: Number, default: 0},         //数据总数
            datasetPagesize: {type: Number, default: 10},     //每页显示数据条数
            currentIndex: {type: Number, default: 1},         //Page控件当前选中页码
            modalTitle: {type: String, default: 'Select'},    //弹层标题
            columnSet: Array,                                   //表格列配置
            onPageIndexChange: Function,                        //当组件内页码变更时的回调
            onSelectOk: Function,                               //当点击确定完成选择操作的回调
            onSelectCancel: Function,                           //当点击取消的回调
            selectType: {                                       //选择类型（单选：single，多选：mutiple）
                type: String,
                default: 'mutiple',
                validator: function (value) {
                    return value == 'single' || value == 'mutiple';
                }
            },
            selectSort: {                                       //已选择列表支持排序功能（多选模式下）
                type: Boolean,
                default: false
            }
        },
        data() {
            return {
                tableType: {
                    isLeft: true,
                    left: 'primary',
                    right: 'default',
                },
                modalShow: false,
                originSelectedDataset: [],
                addColumn: {
                    title: '添加',
                    width: 90,
                    align: 'center',
                    render: (h, params) => {
                        return h('Button', {
                            props: {type: 'text', icon: 'md-add'},
                            on: {
                                click: () => {
                                    this.tableOnAdd(params);
                                }
                            }
                        });
                    }
                },
                delColumn: {
                    title: '删除',
                    width: 90,
                    align: 'center',
                    render: (h, params) => {
                        return h('Button', {
                            props: {type: 'text', icon: 'md-trash'},
                            on: {
                                click: () => {
                                    this.tableOnDel(params);
                                }
                            }
                        });
                    }
                },
                sortColumn: {
                    title: '排序',
                    width: 70,
                    align: 'center',
                    render: (h, params) => {
                        var self = this;
                        return h('input', {
                            domProps: {
                                value: this.selectedSortIndexes[params.index]
                            },
                            'class': 'ivu-input ivu-input-small',
                            on: {
                                input: function (e) {
                                    self.selectedSortIndexes[params.index] = e.target.value;
                                }
                            }
                        });
                    }
                },
                localColumnSet: [],
                selectedColumnSet: [],
                selectedSortIndexes: [],
            };
        },
        computed: {
            tableDataset() {
                return this.tableType.isLeft ? this.dataset : this.selectedDataset;
            },
            tableColumnSet() {
                return this.tableType.isLeft ? this.localColumnSet : this.selectedColumnSet;
            }
        },
        watch: {
            'selectedDataset': 'updateSelectedIndexes'
        },
        created() {
            this.columnSet.forEach(function (element) {
                this.localColumnSet.push(element);
                this.selectedColumnSet.push(element);
            }, this);

            if (this.selectType != 'single') {
                this.localColumnSet.push(this.addColumn);
            }
            if (this.selectSort) {
                this.selectedColumnSet.push(this.sortColumn);
            }
            this.selectedColumnSet.push(this.delColumn);
        },
        methods: {
            //多选情况下，切换待选列表和已选列表
            toggleType() {
                this.tableType.isLeft = !this.tableType.isLeft;
                this.tableType.left = this.tableType.isLeft ? 'primary' : 'default';
                this.tableType.right = this.tableType.isLeft ? 'default' : 'primary';
            },
            //关闭选择弹窗时，需要重置的一些状态
            closeModal() {
                this.tableType.isLeft = true;
                this.tableType.left = this.tableType.isLeft ? 'primary' : 'default';
                this.tableType.right = this.tableType.isLeft ? 'default' : 'primary';
                this.modalShow = false;
            },
            //点下确认按钮时
            selectOk() {
                if (this.selectSort && !this.selectedIndexesChecked()) {
                    this.$Message.error('排序数据填写有误!');
                    return;
                }
                if (this.onSelectOk) {
                    this.onSelectOk(this.selectedDataset);
                }
                this.closeModal();
            },
            //点下取消按钮时
            selectCancel() {
                this.selectedDataset.splice(0, this.selectedDataset.length);
                if (this.originSelectedDataset && this.originSelectedDataset.length > 0) {
                    this.originSelectedDataset.forEach(function (element) {
                        this.selectedDataset.push(element);
                    }, this);
                }
                this.closeModal();
            },
            //显示选择弹窗组件
            showModal() {
                this.modalShow = true;
                this.originSelectedDataset = [];
                if (this.selectedDataset && this.selectedDataset.length > 0) {
                    this.selectedDataset.forEach(function (element) {
                        this.originSelectedDataset.push(element);
                    }, this);
                }
            },
            //多选时，待选列表点击添加条目按钮
            tableOnAdd(params) {
                this.selectedDataset.push(params.row);
            },
            //多选时，已选列表点击删除条目按钮
            tableOnDel(params) {
                this.selectedDataset.splice(params.index, 1);
            },
            //单选时，当选项发生改变时
            tableOnCurrentChange(row, oldRow) {
                this.selectedDataset.splice(0, this.selectedDataset.length);
                this.selectedDataset.push(row);
                // this.selectedDataset[0] = row;
                if (this.selectType === 'single') {
                    this.selectOk();
                }
            },
            //待选列表页码被点击改变时
            onIndexChange(index) {
                if (this.onPageIndexChange) {
                    this.onPageIndexChange(index);
                }
            },
            //更新已选列表排序索引
            updateSelectedIndexes() {
                let indexArr = [];
                for (let i = 0; i < this.selectedDataset.length; i++) {
                    indexArr.push(`${i + 1}`);
                }
                this.selectedSortIndexes = indexArr;
            },
            //已选列表索引合法性检查
            selectedIndexesChecked() {
                let selectedSortData = new Array(this.selectedSortIndexes.length);
                try {
                    for (let i = 0; i < this.selectedSortIndexes.length; i++) {
                        let index = parseInt(this.selectedSortIndexes[i]) - 1;
                        if (index < 0 || index >= this.selectedSortIndexes.length) {return false;}
                        let item = this.selectedDataset[i];
                        if (!item) {return false;}
                        selectedSortData[index] = item;
                    }
                } catch (e) {
                    return false;
                }
                this.selectedDataset.splice(0, this.selectedDataset.length);
                for (let i = 0; i < selectedSortData.length; i++) {
                    this.selectedDataset.push(selectedSortData[i]);
                }
                this.updateSelectedIndexes();
                return true;
            }
        }
    }

</script>