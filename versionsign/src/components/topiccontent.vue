<template>
  <div>
    <Table  :columns="columns" :data="data"></Table>
  </div>
</template>
<script>
	export default{
		props:{
			'columns':Array,
			'data':Array
		},
		data () {
			return{
			}
		}
	}
</script>