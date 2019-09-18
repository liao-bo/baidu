<template>
	<div class="modal-layout">
		<Button type="primary" @click="modal1 = true">显示对话框</Button>
		<Button type="primary" @click="showSelect">显示自定义选择组件</Button>
		<Modal v-model="modal1" title="普通的Modal对话框标题" @on-ok="ok" @on-cancel="cancel">
			<p>对话框内容</p>
			<p>对话框内容</p>
			<p>对话框内容</p>
		</Modal>
		<SelectTableModal ref="selectModal" :dataset="data1" :selected-dataset="data2" :column-set="columns1" :dataset-total="15"
		 :dataset-pagesize="5" modal-title="选择CP" :on-page-index-change="onTableModalIndexChange" :onSelectOk="onTableModalOk" :select-sort="true">
			<div slot="search_panel" class="search-bar">
				条件1：
				<Input v-model="searchQuery1" size="small" style="width:100px;"></Input>
				条件2：
				<Select v-model="searchQuery2" size="small" style="width:100px">
					<Option v-for="(item, index) in cityList" :value="item.value" :key="index">{{ item.label }}</Option>
				</Select>
				<Button type="primary" size="small" @click="searchData">搜索</Button>
			</div>
		</SelectTableModal>
		<br>
		<br> 更多细节请访问：
		<a href="https://www.iviewui.com/components/modal" target="_blank">https://www.iviewui.com/components/modal</a>
	</div>
</template>

<style scoped>
	.modal-layout {
		padding: 0.2rem 0 0 0.4rem;
	}

	.page-panel {
		width: 100%;
		padding: 15px 0;
		text-align: center;
	}

	.search-bar {
		width: 100%;
		padding: 4px 0 10px 0;
	}
</style>

<script>
	import SelectTableModal from '../components/SelectTableModal.vue';

	const testData = {
		page1: [
			{
				id: 1000,
				name: 'JayceVue'
			},
			{
				id: 1001,
				name: 'JayceVue'
			},
			{
				id: 1002,
				name: 'JayceVue'
			},
			{
				id: 1003,
				name: 'JayceVue'
			},
			{
				id: 1004,
				name: 'JayceVue'
			}
		],
		page2: [
			{
				id: 1005,
				name: 'JayceVue'
			},
			{
				id: 1006,
				name: 'JayceVue'
			},
			{
				id: 1007,
				name: 'JayceVue'
			},
			{
				id: 1008,
				name: 'JayceVue'
			},
			{
				id: 1009,
				name: 'JayceVue'
			}
		],
		page3: [
			{
				id: 1010,
				name: 'JayceVue'
			},
			{
				id: 1011,
				name: 'JayceVue'
			},
			{
				id: 1012,
				name: 'JayceVue'
			},
			{
				id: 1013,
				name: 'JayceVue'
			},
			{
				id: 1014,
				name: 'JayceVue'
			}
		],
		page4: [
			{
				id: 2000,
				name: 'Apple Inc'
			},
			{
				id: 2001,
				name: 'Google Inc'
			},
			{
				id: 2002,
				name: 'Microsoft Inc'
			}
		],
	}




	export default {
		components: {
			SelectTableModal
		},
		data() {
			return {
				modal1: false,
				modal2: false,
				columns1: [
					{
						title: 'ID',
						key: 'id',
						width: 100
					},
					{
						title: '供应商名称',
						key: 'name'
					}
				],
				data1: testData.page1,
				data2: [],
				searchQuery1: '',
				searchQuery2: '',
				cityList: [
					{
						value: 'beijing',
						label: '北京市'
					},
					{
						value: 'shanghai',
						label: '上海市'
					},
					{
						value: 'shenzhen',
						label: '深圳市'
					},
					{
						value: 'hangzhou',
						label: '杭州市'
					},
					{
						value: 'nanjing',
						label: '南京市'
					},
					{
						value: 'chongqing',
						label: '重庆市'
					}
				],
			}
		},
		methods: {
			ok() {
				this.$Message.info('点击了确定');
			},
			cancel() {
				this.$Message.info('点击了取消');
			},
			showSelect() {
				this.$refs.selectModal.showModal();
			},
			onTableModalIndexChange(index) {
				this.data1 = testData['page' + index];
			},
			onTableModalOk(data) {
				this.data2 = data;
			},
			searchData() {
				console.log(this.searchQuery1);
				console.log(this.searchQuery2);
				this.data1 = testData['page4'];
			}
		}
	}

</script>