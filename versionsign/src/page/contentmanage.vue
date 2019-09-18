<style>
.modal-mask{
	position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.65);
    height: 100%;
    z-index: 1000;
    filter: alpha(opacity=50);
}
.modal-mask-hidden{
	display: none;
}


.versionsign-manage{

}
.modify-header{
	padding: 16px 24px;
	border-radius: 4px 4px 0px 0px;
	background: #fff;
	color: rgba(0,0,0,0.65);
	border-bottom:1px solid #e8e8e8;
}
.modify-title{
	margin: 0;
  font-size: 16px;
  line-height: 22px;
  font-weight: 500;
  color: rgba(0, 0, 0, 0.85);
}
.modify-body{
	padding: 24px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;
}
.modify-footer{
	border-top: 1px solid #e8e8e8;
	padding: 16px 24px;
	text-align: right;
	border-radius: 4px 4px 0px 0px;
}
.modify-button{
    line-height: 1.499;
    display: inline-block;
    font-weight: 400;
    text-align: center;
    -ms-touch-action: manipulation;
    touch-action: manipulation;
    cursor: pointer;
    background-image: none;
    border: 1px solid transparent;
    white-space: nowrap;
    padding: 0 15px;
    font-size: 14px;
    border-radius: 4px;
    height: 32px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
    -o-transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
    transition: all 0.3s cubic-bezier(0.645, 0.045, 0.355, 1);
    position: relative;
    -webkit-box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
    box-shadow: 0 2px 0 rgba(0, 0, 0, 0.015);
    color: rgba(0, 0, 0, 0.65);
    background-color: #fff;
    border-color: #d9d9d9;
}
.creat-new-version{
	position: relative;
    background-color: #fff;
    border: 0;
    border-radius: 4px;
    background-clip: padding-box;
    -webkit-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
</style>
<template>
  <div class="versionsign-manage modal-mask-hidden">
	<div class="version-data modal-mask" id="version-data">
		<div class="version-data-modify">
			<div class="modify-header">
				<div class="modify-title">
					修改版本数据
				</div>
			</div>
			<div class="modify-body">
			  <Row>
                <Col span="6" offset="6">对应端</Col>
                <Col span="6">待绑定数据</Col>
              </Row>
              <Row>
                <Col span="6" offset="6">对应版本</Col>
                <Col span="6">待绑定数据</Col>
              </Row>
			</div>
			<div class="modify-footer">
			  <button type="button" class="modify-button">
                <span>新增一个版本</span>
              </button>
              <button type="button" class="modify-button">
                <span>新增一次灰度</span>
              </button>
              <button type="button" class="modify-button">
                <span>删除一次灰度</span>
              </button>
              <button type="button" class="modify-button">
                <span>删除对应版本</span>
              </button>
			</div>
		</div>	
	</div>
	<div class="creat-new-version" id="creat-new-version">
	  <div class="modify-header">
	    <div class="modify-title">
	      <span>新增一个版本签章</span>
	    </div>
	  </div>
	  <div class="modify-body">
        <Row>
          <Col span="6" offset="6">端选择：</Col>
          <Col span="6">
            <template>
              <Select v-model="clientValue" style="width:200px">
                <Option v-for="item in clientList" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
            </template>
          </Col>
        </Row>
        <Row>
          <Col span="6" offset="6">版本输入：</Col>
          <Col span="6">
            <template>        
              <Input v-model="versionValue" placeholder="请输入版本号" style="width: 300px" />
            </template>
          </Col>
        </Row>
	  </div>
	  <div class="modify-footer">
	    <button type="button" class="modify-button">
          <span>取消</span>
        </button>
        <button type="button" class="modify-button">
          <span>确定</span>
        </button>
      </div>
	</div>
    <div class="team-modify" id="team-modify">
      <div class="modify-header">
        <div class="modify-title">
          <span>修改Teamname组</span>
        </div>
      </div>
      <div class="modify-body">
        <template v-for = "data in topicDatas">
          <topiccontent v-bind:columns = 'data.title' v-bind:data = 'data.data'></topiccontent>
        </template>
      </div>
      <div class="modify-footer">
        <button type="button" class="modify-button">
          <span>return</span>
        </button>
        <button type="button" class="modify-button">
          <span>新增一行</span>
        </button>
      </div>
    </div>
    <div class="creat-new-team" id="creat-new-team">
	  <div class="modify-header">
	    <div class="modify-title">
	      <span>Topic管理</span>
	    </div>
	  </div>
	  <div class="creat-new-version-body">
        <Row>
          <Col span="6" offset="6">团队名称：</Col>
          <Col span="6">
            <template>        
              <Input v-model="teamName" placeholder="团队名称" style="width: 300px" />
            </template>
          </Col>
        </Row>
        <Row>
          <Col span="6" offset="6">负责人：</Col>
          <Col span="6">
            <template>        
              <Input v-model="principle" placeholder="负责人" style="width: 300px" />
            </template>
          </Col>
        </Row>
        <Row>
          <Col span="6" offset="6">是否属于第三方</Col>
          <Col span="6">
            <template>        
              <Select v-model="isThirdPart" style="width:200px">
                <Option v-for="item in chooseData" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
            </template>
          </Col>
        </Row>
	  </div>
	  <div class="creat-new-version-footer">
	    <button type="button" class="modify-button">
          <span>取消</span>
        </button>
        <button type="button" class="modify-button">
          <span>确定</span>
        </button>
      </div>
	</div>
  </div>	
</template>

<script>
    import topiccontent from '../components/topiccontent.vue'
    export default {
    	components:{topiccontent},
        data () {
            return {
                clientList: [
                    {
                        value: 'Android',
                        label: 'Android'
                    },
                    {
                        value: 'iOS',
                        label: 'iOS'
                    }
                ],
                chooseData: [
                    {
                        value: 'yes',
                        label: '是'
                    },
                    {
                        value: 'no',
                        label: '否'
                    }
                ],
                clientValue: '',
                versionValue: '',
                teamName: '',
                principle: '',
                isThirdPart: '',
                topicDatas:[
		            {
		            title:[
		                {
		                    title: 'ID',
		                    key: 'id'
		                },
		                {
		                    title: '团队名称',
		                    key: 'teamName'
		                },
		                {
		                    title: '负责人',
		                    key: 'principle'
		                },
		                {
		                    title: '操作',
		                    key: 'operate'
		                }
		              ],
		            data:[
		                {
		                    id: '1',
		                    teamName: 'feed',
		                    principle: '贾',
		                    operate: 'delete',

		                },
		                {
		                    id: '1',
		                    teamName: 'feed',
		                    principle: '贾',
		                    operate: 'delete',

		                },
		                {
		                    id: '1',
		                    teamName: 'feed',
		                    principle: '贾',
		                    operate: 'delete',

		                },
		                {
		                    id: '1',
		                    teamName: 'feed',
		                    principle: '贾',
		                    operate: 'delete',

		                },
		                {
		                    id: '1',
		                    teamName: 'feed',
		                    principle: '贾',
		                    operate: 'delete',

		                },
		              ]
		            }
		        ]
            }
        }
    }
</script>