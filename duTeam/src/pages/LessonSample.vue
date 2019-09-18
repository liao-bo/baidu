<template>
    <div id="lesson_sample">
        <Button type="primary" @click="loadServerData">拉取接口数据</Button>
        <Table :columns="tableColumns" :data="tableData"></Table>
        <div id="demo_charts"></div>
    </div>
</template>

<style scoped>
    #demo_charts {
        margin-top: 20px;
        width: 720px;
        height: 480px;
    }
</style>

<script>
    import Echarts from "echarts";

    import axios from 'axios';

    export default {
        data() {
            return {
                tableColumns: [
                    {title: '姓名', key: 'name'},
                    {title: '年龄', key: 'age'},
                    {title: '地址', key: 'address'}
                ],
                tableData: [
                    {name: '王小明', age: 18, address: '北京市朝阳区芍药居'},
                    {name: '张小刚', age: 25, address: '北京市海淀区西二旗'},
                    {name: '李小红', age: 30, address: '上海市浦东新区世纪大道'},
                    {name: '周小伟', age: 26, address: '深圳市南山区深南大道'}
                ],
                demoCharts: null,
                demoChartsOpt: {
                    title: {
                        text: '某站点用户访问来源',
                        subtext: '纯属虚构',
                        x: 'center'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        left: 'left',
                        data: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎']
                    },
                    series: [
                        {
                            name: '访问来源',
                            type: 'pie',
                            radius: '55%',
                            center: ['50%', '60%'],
                            data: [
                                {value: 335, name: '直接访问'},
                                {value: 310, name: '邮件营销'},
                                {value: 234, name: '联盟广告'},
                                {value: 135, name: '视频广告'},
                                {value: 1548, name: '搜索引擎'}
                            ],
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                }
            }
        },
        created() {

        },
        mounted() {
            this.demoCharts = Echarts.init(document.getElementById('demo_charts'));
            this.demoCharts.setOption(this.demoChartsOpt);
        },
        methods: {
            loadServerData() {
                axios.get('http://localhost:8001/sample/lessondata').then(res => {
                    this.tableData = res.data.data;
                }).catch(error => {

                });
            }
        }
    }

</script>