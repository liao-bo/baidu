<template>
    <RadioGroup v-model="client">
        <Radio label="iOS">
            
            <span>iOS</span>
        </Radio>
        <Radio label="Android">
           
            <span>Android</span>
        </Radio>
    </RadioGroup>
   
</template>
<script>
    export default {
        data () {
            return {
                client: 'apple',
            }
        }
    }
</script>
