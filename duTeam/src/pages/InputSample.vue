<template>
    <div class="input-layout">
        <Input v-model="value" placeholder="请输入..."></Input>
        <br><br>
        <Input v-model="value11">
        <span slot="prepend">http://</span>
        <span slot="append">.com</span>
        </Input>
        <br>
        <Input v-model="value12">
        <Select v-model="select1" slot="prepend" style="width: 80px">
            <Option value="http">http://</Option>
            <Option value="https">https://</Option>
        </Select>
        <Select v-model="select2" slot="append" style="width: 70px">
            <Option value="com">.com</Option>
            <Option value="org">.org</Option>
            <Option value="io">.io</Option>
        </Select>
        </Input>
        <br>
        <Input v-model="value13">
        <Select v-model="select3" slot="prepend" style="width: 80px">
            <Option value="day">日活</Option>
            <Option value="month">月活</Option>
        </Select>
        <Button slot="append" icon="ios-search"></Button>
        </Input>
        <br><br>
        更多细节请访问：
        <a href="https://www.iviewui.com/components/input" target="_blank">https://www.iviewui.com/components/input</a>
    </div>
</template>

<style scoped>
    .input-layout {
        padding: 0.2rem 0 0 0.4rem;
    }
</style>

<script>
    export default {
        data() {
            return {
                value: '',
                value11: '',
                value12: '',
                value13: '',
                select1: 'http',
                select2: 'com',
                select3: 'day'
            }
        }
    }

</script>