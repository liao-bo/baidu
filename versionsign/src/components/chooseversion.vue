<template>
    <Select v-model="model1" style="width:200px">
        <Option v-for="item in versionList" :value="item.value" :key="item.value">{{ item.label }}</Option>
    </Select>
</template>
<script>
    export default {
        data () {
            return {
                versionList: [
                    {
                        value: '11.5',
                        label: '11.5'
                    },
                    {
                        value: '11.6',
                        label: '11.6'
                    },
                    {
                        value: '11.7',
                        label: '11.7'
                    },
                    {
                        value: '11.8',
                        label: '11.8'
                    },
                    {
                        value: '11.9',
                        label: '11.9'
                    }
                ],
                model1: ''
            }
        }
    }
</script>
