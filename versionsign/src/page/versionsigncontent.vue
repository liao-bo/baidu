
<style>
.contaner{
	
  display: flex;
  flex-direction: column;

}
.version-choose{
  margin: 20px;
  
  font-size: 14px;
  line-height: 1.5;
  color: rgb(0,0,0,0.65);
  align-content: center;
}
.topic-content{
  margin: 20px;
  
}
.third-part-content{
  margin: 20px;
 
}
.change-data{
  margin: 5px;
}

.sign {
  visibility: hidden;
}

.overlayer {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.65);
    height: 100%;
    width: 100%;
    z-index: 1000;
    opacity:.80;
    filter: alpha(opacity=50);
}
.wrap {
    position: fixed;
    overflow: auto;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1000;
    -webkit-overflow-scrolling: touch;
    /*outline: 0;*/
}
.modal {
    font-size: 14px;
    font-variant: tabular-nums;
    line-height: 1.5;
    color: rgba(0, 0, 0, 0.65);
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    list-style: none;
    position: relative;
    width: auto;
    margin: 0 auto;
    top: 150px;
    padding-bottom: 24px;
}

.content {
    margin-left: 30%;margin-right: 30%;
    position: relative;
    background-color: #fff;
    border: 0;
    border-radius: 4px;
    background-clip: padding-box;
    -webkit-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}
.moder-header {
    padding: 16px 24px;
    border-radius: 4px 4px 0 0;
    background: #fff;
    color: rgba(0, 0, 0, 0.65);
    border-bottom: 1px solid #e8e8e8;
}
.moder-body {
  padding: 24px;
  font-size: 14px;
  line-height: 1.5;
  word-wrap: break-word;
}
.moder-footer {
  border-top: 1px solid #e8e8e8;
    padding: 10px 16px;
    text-align: right;
    border-radius: 0 0 4px 4px;
}	
.lable-item {
    font-size: 14px;
    font-variant: tabular-nums;
    line-height: 1.5;
    color: rgba(0, 0, 0, 0.65);
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    list-style: none;
    margin-bottom: 24px;
    vertical-align: top;
}
.lable {
  float: right;
}
</style>
<template>
  <div class="contaner">
    <div class="version-choose">
        <Row>
          
          <Col span="6" offset="4">端:&nbsp;&nbsp; 
            <template>
              <RadioGroup v-model="client" @on-change="selectClient()">
                <Radio label="iOS">            
                  <span>iOS</span>
                </Radio>
                <Radio label="Android">
                  <span>Android</span>
                </Radio>
              </RadioGroup>
            </template>
          </Col>
          <Col span="5">版本选择:&nbsp;&nbsp;
            <template>
              <Select v-model="versionValue" @on-change="selectVersion()"style="width:200px">
                <Option v-for="item in versionList" :value="item.value" :key="item.value">{{ item.label }}</Option>
              </Select>
            </template>
          </Col>
          <Col span="5"><Button type = "primary" @click="startManageVersion()">版本管理</Button></Col>
          <Col span="4"> </Col>
        </Row>
    </div>
    <div class="topic-content">
      <Button href = '#' @click="topicManage()" class="change-data" type="primary">管理topic</Button>
     <!--  <Button href = '#' @click="urgeSign()" class="change-data" type="primary">签章提醒</Button> -->
      <br>
      <!-- 用作展示签章信息 -->
      <template>
        <Table :columns="columns" :data="data">
          <template slot-scope="{ row, index }" slot="topic">
            <div v-if="editIndex === index&&row.topic === editValue">
              <!-- <Input type="text" v-model="editTopic" /> -->
              <Select
                v-model="selectlist"
                filterable
                multiple
                remote
                :remote-method="getuser"
                :loading="loading">
                <Option v-for="(option, index) in userinfo" :value="option.username + ':' + option.name" :key="index">{{option.infotext}}</Option>
              </Select>
              <Button @click="handleSaveTopic(0, row.id, index)">保存</Button>
              <Button @click="cancell()">取消</Button>
            </div>            
            <a @click='handleEditTopic(0, row,index)' v-else ><span :style = "{fontSize:'14px'}">{{ row.topic }}</span></a>
          </template>
          <template slot-scope="{ row, index }" slot="principle">
            <div v-if="editIndex === index&&row.principle === editValue">
              <Input type="text" v-model="editPrinciple"/>
              <Button @click="handleSavePrinciple(0, row.id, index)">保存</Button>
              <Button @click="cancell()">取消</Button>
            </div>           
            <a @click="handleEditPrinciple(0, row, index)" v-else><span :style = "{fontSize:'14px'}">{{ row.principle }}</span></a>
          </template>
          <!-- 签章情况显示区域 -->
          <template slot-scope="{ row, index }" slot="firstGrey">           
            <a href="javascript:void(0);" @click="startSign(0, row, 'firstGrey', index)" v-if="row.firstGrey === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'firstGrey', index)" v-else-if="row.firstGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'firstGrey', index)" v-else="row.firstGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>
          </template>
          <template slot-scope="{ row, index }" slot="secondGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'secondGrey', index)" v-if="row.secondGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'secondGrey', index)" v-else-if="row.secondGrey === 'nPass'">
              <template>
               <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'secondGrey', index)" v-else="row.secondGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="thirdGrey">
            <a href="#" @click="startSign(0, row, 'thirdGrey', index)" v-if="row.thirdGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'thirdGrey', index)" v-else-if="row.thirdGrey === 'nPass'">
              <template>
               <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'thirdGrey', index)" v-else="row.thirdGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
           <template slot-scope="{ row, index }" slot="forthGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'forthGrey', index)" v-if="row.forthGrey === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'forthGrey', index)" v-else-if="row.forthGrey === 'nPass'">
              <template>
               <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'forthGrey', index)" v-else="row.forthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          
          <template slot-scope="{ row, index }" slot="fifthGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'fifthGrey', index)" v-if="row.fifthGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'fifthGrey', index)" v-else-if="row.fifthGrey === 'nPass'">
              <template>
               <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'fifthGrey', index)" v-else="row.fifthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="sixthGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'sixthGrey', index)" v-if="row.sixthGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'sixthGrey', index)" v-else-if="row.sixthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'sixthGrey', index)" v-else="row.sixthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="seventhGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'seventhGrey', index)" v-if="row.seventhGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'seventhGrey', index)" v-else-if="row.seventhGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'seventhGrey', index)" v-else="row.seventhGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="eighthGrey">
            <a href="javascript:void(0);" @click="startSign(0, row, 'eighthGrey', index)" v-if="row.eighthGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'eighthGrey', index)" v-else-if="row.eighthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'eighthGrey', index)" v-else="row.eighthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="official">
            <a href="javascript:void(0);" @click="startSign(0, row, 'official', index)" v-if="row.official === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'official', index)" v-else-if="row.official === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(0, row, 'official', index)" v-else="row.official === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a> 
          </template>
        </Table>
      </template>
    </div>
    <!-- 展示第三方的签章信息 -->
    <div class="topic-content">
      <Button href = '#' @click="relayManage()" class="change-data" type="primary">管理Relay</Button>
      <br>
      <!-- 用作展示签章信息 -->
      <template>
        <Table :columns="columns" :data="thirdPartData">
          <template slot-scope="{ row, index }" slot="topic">
            <div v-if="editThirdIndex === index&&row.topic === editValue">
              <Input type="text" v-model="editTopic" />
              <Button @click="handleSaveTopic(1, row.id, index)">保存</Button>
              <Button @click="cancell()">取消</Button>
            </div>            
            <a @click='handleEditTopic(1, row,index)' v-else><span :style = "{fontSize:'14px'}">{{ row.topic }}</span></a>
          </template>
          <template slot-scope="{ row, index }" slot="principle">
            <div v-if="editThirdIndex === index&&row.principle === editValue">
              <Input type="text" v-model="editPrinciple"/>
              <Button @click="handleSavePrinciple(1, row.id, index)">保存</Button>
              <Button @click="cancell()">取消</Button>
            </div>           
            <a @click="handleEditPrinciple(1, row, index)" v-else><span :style = "{fontSize:'14px'}">{{ row.principle }}</span></a>
          </template>
          <!-- 签章情况显示区域 -->
          <template slot-scope="{ row, index }" slot="firstGrey">           
            <a href="javascript:void(0);" @click="startSign(1, row, 'firstGrey', index)" v-if="row.firstGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'firstGrey', index)" v-else-if="row.firstGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'firstGrey', index)" v-else="row.firstGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>
          </template>
          <template slot-scope="{ row, index }" slot="secondGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'secondGrey', index)" v-if="row.secondGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'secondGrey', index)" v-else-if="row.secondGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'secondGrey', index)" v-else="row.secondGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="thirdGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'thirdGrey', index)" v-if="row.thirdGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'thirdGrey', index)" v-else-if="row.thirdGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'thirdGrey', index)" v-else="row.thirdGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
           <template slot-scope="{ row, index }" slot="forthGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'forthGrey', index)" v-if="row.forthGrey === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'forthGrey', index)" v-else-if="row.forthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'forthGrey', index)" v-else="row.forthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          
          <template slot-scope="{ row, index }" slot="fifthGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'fifthGrey', index)" v-if="row.fifthGrey === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'fifthGrey', index)" v-else-if="row.fifthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'fifthGrey', index)" v-else="row.fifthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="sixthGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'sixthGrey', index)" v-if="row.sixthGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'sixthGrey', index)" v-else-if="row.sixthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'sixthGrey', index)" v-else="row.sixthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="seventhGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'seventhGrey', index)" v-if="row.seventhGrey === 'pass'">
              <template>
                <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'seventhGrey', index)" v-else-if="row.seventhGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'seventhGrey', index)" v-else="row.seventhGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="eighthGrey">
            <a href="javascript:void(0);" @click="startSign(1, row, 'eighthGrey', index)" v-if="row.eighthGrey === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'eighthGrey', index)" v-else-if="row.eighthGrey === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'eighthGrey', index)" v-else="row.eighthGrey === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a>   
          </template>
          <template slot-scope="{ row, index }" slot="official">
            <a href="javascript:void(0);" @click="startSign(1, row, 'official', index)" v-if="row.official === 'pass'">
              <template>
               <Icon type="md-checkmark-circle" size="20" color="rgb(1, 223, 58)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'official', index)" v-else-if="row.official === 'nPass'">
              <template>
                <Icon type="md-close-circle" size="20" color="rgb(255, 0, 0)"/>
              </template>
            </a>
            <a href="javascript:void(0);" @click="startSign(1, row, 'official', index)" v-else="row.official === 'nullValue'">
              <template>
                <Icon type="md-help-circle" size="20" color="rgb(47, 10, 243)"/>
              </template>
            </a> 
          </template>
        </Table>
      </template>
    </div>
    <!-- 准入的弹窗 -->
    <div v-bind:class="{sign:signPassIsActive}">
    <div class="overlayer"></div>
    <div class = "wrap"  id="sign">
    <div class = "modal">
      <div class="content">
        <div class="moder-header">
          <div class="modal-title">
            Topic是否准入通过
          </div>
        </div>
        <div class="moder-body">
        <div class="lable-item">
        <Row>
          <Col span="8">
            <div class = "lable">
               对应的端：
            </div>
          </Col>
          <Col span="16">
             <div>
               {{client}}
            </div>
          </Col>
        </Row>
          
        </div>
        <div class="lable-item">
        <Row>
          <Col span="8">
            <div class = "lable">
              对应的版本：
            </div>
          </Col>
          <Col span="16">
             <div>
                {{versionValue}}
            </div>
          </Col>
        </Row>
          
        </div>
        <div class="lable-item">
        <Row>
          <Col span="8">
            <div class = "lable">
              对应的Topic：
            </div>
          </Col>
          <Col span="16">
             <div>
               {{editTopic}}
            </div>
          </Col>
        </Row>
          
        </div>
        <div>
        <Row>
        <Col span="8">
          <div class = "lable">
          测试是否通过:&nbsp;&nbsp;
          </div>
        </Col>
        <Col span="16">
          <div>
          <template>
                <RadioGroup v-model="isPass">
                  <Radio label="pass">            
                    <span>通过</span>
                  </Radio>
                  <Radio label="nPass">
                    <span>不通过</span>
                  </Radio>
                  <Radio label="nullValue">
                    <span>还未填写</span>
                  </Radio>
                </RadioGroup>
              </template>
          </div>
        </Col>
        </Row>
        </div>
        </div>
        <div class="moder-footer">
          <Button @click="signPassIsActive = 1">取消</Button>
          <Button type="primary" @click="handleIsPass()">确定</Button>
        </div>
      </div>
      </div>
    </div>
    
    </div>


    <versionManage v-bind:propClient='this.client' v-bind:propVersion='this.versionValue' 
    v-bind:propManageIsActive='this.propManageIsActive' v-on:listenManageEvent='cancellManage'></versionManage>


    <topicManage v-bind:propTopicManageIsActive = 'this.propTopicManageIsActive' v-bind:propData='this.propData' 
    v-bind:isThird='this.isThirdPart' v-bind:propClient='this.client' v-bind:propVersion='this.versionValue'
     v-on:listenTopicManageEvent='cancellTopicManage'></topicManage>


    <!--  <urgUser v-bind:propClient = 'this.client' v-bind:propVersion='this.versionValue' v-bind:propIni = 'this.propIni' v-bind:propUrgUserIsActive = 'this.propUrgUserIsActive' v-on:listenUrgeSignEvent='cancellUrgeSign'></urgUser> -->
  </div>
  
</template >
<script>
import topiccontent from '../components/topiccontent.vue'
import contentmanage from './contentmanage.vue'
import versionManage from '../components/versionManage.vue'
import topicManage from '../components/topicManage.vue'
import urgUser from '../components/urgUser.vue'
import axios from 'axios'
  export default{
    components:{topiccontent, contentmanage, versionManage, topicManage, urgUser},
    data(){
      return{
        client: 'iOS',
        isPass: 'nullValue',
        versionValue: '',
        signPassIsActive: 1, //决定签章弹窗是否展示
        passUrl:require("../assets/pass.jpg"), //通过时的显示图标
        nPassUrl:require("../assets/nPass.jpg"), //不通过时的显示图标
        nullValueUrl:require("../assets/nullValue.jpg"), //未选择时的显示图标
        propManageIsActive: 1,
        propTopicManageIsActive: 1,
        iOSVersionList:[],
        AndroidVersionList: [],
        versionList: [
                    {
                        value: '11.9',
                        label: '11.9'
                    }
                ],
        columns: [
          
        ],
        data: [
          

        ],
        thirdPartData: [],
        
        editIndex: -1,  // 当前聚焦的输入框的行数
        editThirdIndex: -1, //第三方聚焦的输入框的行数
        flag: -1, //当前是非第三方还是第三方，0：费第三方， 1：第三方
        editRow: -1, //当前聚焦的列数
        editValue: '', //保存当前的值
        editTopic: '',  // 第一列输入框，当然聚焦的输入框的输入内容，与 data 分离避免重构的闪烁
        editPrinciple: '',  // 第二列输入框
        editProcess: '', //保存被编辑的灰度的键值
        id: -1,
        isThirdPart: -1,
        propData: [],
        propUrgUserIsActive : 1,
        propIni : {},
        selectlist:[]
        
          
      }
    },
    created:function () {
      let instance = this;
      if(this.$cookies.isKey('client')){
        this.client = this.$cookies.get('client');

      }

      this.handleGetData(instance.client, instance.versionValue).then(function(value){
        console.log(value);

        //构建显示结构
        var versionValue = value['info']['version'];
        var versionLeng = versionValue.length; 
        var versionNewList = [];
        var iOSVersionList = [];
        var AndroidVersionList = [];
        instance.versionValue = versionValue[versionLeng-1]['versionNum'];
        for (let i = 0;i<versionLeng;i++){
           var versionJson = {
              value: versionValue[i]['versionNum'],
              label: versionValue[i]['versionNum']
           }
           versionNewList.push(versionJson);

        };
        for (let i = 0;i< value['info']['iosVersion'].length;i++){
           let versionJson = {
              value: value['info']['iosVersion'][i]['versionNum'],
              label: value['info']['iosVersion'][i]['versionNum']
           }
           iOSVersionList.push(versionJson);

        };
        for (let i = 0;i< value['info']['androidVersion'].length;i++){
           let versionJson = {
              value: value['info']['androidVersion'][i]['versionNum'],
              label: value['info']['androidVersion'][i]['versionNum']
           }
           AndroidVersionList.push(versionJson);

        };
        
        
        instance.versionList = versionNewList.reverse();
        instance.iOSVersionList = iOSVersionList.reverse();
        instance.AndroidVersionList = AndroidVersionList.reverse();

        var content = value['info']['nthird'];
        //console.log(content);
        var column = [
          {
            title: 'Topic',
            slot: 'topic',
            align:'center'
          },
          {
            title: '负责人',
            slot: 'principle',
            align:'center'
          },
          {
            title: '第一次灰度',
            slot: 'firstGrey',
            align:'center'
          }
        ];
        if(content[0].hasOwnProperty('secondGrey')){
          var Json = {
            title: '第二次灰度',
            slot: 'secondGrey',
            align:'center'
          };
         
          column.push(Json);
        };
        if(content[0].hasOwnProperty('thirdGrey')){
          var Json = {
            title: '第三次灰度',
            slot: 'thirdGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('forthGrey')){
          var Json = {
            title: '第四次灰度',
            slot: 'forthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('fifthGrey')){
          var Json = {
            title: '第五次灰度',
            slot: 'fifthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('sixthGrey')){
          var Json = {
            title: '第六次灰度',
            slot: 'sixthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('seventhGrey')){
          var Json = {
            title: '第七次灰度',
            slot: 'seventhGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('eigthGrey')){
          var Json = {
            title: '第八次灰度',
            slot: 'eigthGrey',
            align:'center'
          };
          column.push(Json);
        };
        //最后再加入正式版数据
        column.push({
            title: '正式版',
            slot: 'official',
            align:'center'
          });


        instance.data = value['info']['nthird']; 
        instance.thirdPartData = value['info']['third'];
        instance.columns = column;
        //console.log(instance.columns);
        })
    },
    methods: {
      selectClient () {
          var client = this.client;
          if(client =='iOS'){
            this.versionValue = this.iOSVersionList[0]['value'];
            
          }
          else{
            this.versionValue = this.AndroidVersionList[0]['value'];

          }
          var version = this.versionValue;
          var instance = this;
          this.$cookies.set('client',this.client);


      this.handleGetData(instance.client, instance.versionValue).then(function(value){
        

        //构建显示结构
        console.log(value);
        var versionValue = value['info']['version'];
        var versionLeng = versionValue.length;
        var versionNewList = [];
         instance.versionValue = versionValue[versionLeng-1]['versionNum'];
        for (var i = 0;i<versionLeng;i++){
           var versionJson = {
              value: versionValue[i]['versionNum'],
              label: versionValue[i]['versionNum']
           }
           versionNewList.push(versionJson);

        };
        instance.versionList = versionNewList.reverse();
        

        var content = value['info']['nthird'];
        //console.log(content);
        var column = [
          {
            title: 'Topic',
            slot: 'topic',
            align:'center'
          },
          {
            title: '负责人',
            slot: 'principle',
            align:'center'
          },
          {
            title: '第一次灰度',
            slot: 'firstGrey',
            align:'center'
          }
        ];
        if(content[0].hasOwnProperty('secondGrey')){
          var Json = {
            title: '第二次灰度',
            slot: 'secondGrey',
            align:'center'
          };
          column.push(Json);
        };
        if(content[0].hasOwnProperty('thirdGrey')){
          var Json = {
            title: '第三次灰度',
            slot: 'thirdGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('forthGrey')){
          var Json = {
            title: '第四次灰度',
            slot: 'forthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('fifthGrey')){
          var Json = {
            title: '第五次灰度',
            slot: 'fifthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('sixthGrey')){
          var Json = {
            title: '第六次灰度',
            slot: 'sixthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('seventhGrey')){
          var Json = {
            title: '第七次灰度',
            slot: 'seventhGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('eigthGrey')){
          var Json = {
            title: '第八次灰度',
            slot: 'eigthGrey',
            align:'center'
          };
          column.push(Json);
        };
        //最后再加入正式版数据
        column.push({
            title: '正式版',
            slot: 'official',
            align:'center'
          });


        instance.data = value['info']['nthird']; 
        instance.thirdPartData = value['info']['third'];
        instance.columns = column;
        })

        },
      selectVersion (){
        let instance = this;
        this.$cookies.set('version',this.versionValue);

      this.handleGetData(instance.client, instance.versionValue).then(function(value){
        //console.log(value);

        //构建显示结构
        var content = value['info']['nthird'];
        //console.log(content);
        var column = [
          {
            title: 'Topic',
            slot: 'topic',
            align:'center'
          },
          {
            title: '负责人',
            slot: 'principle',
            align:'center'
          },
          {
            title: '第一次灰度',
            slot: 'firstGrey',
            align:'center'
          }
        ];
        if(content[0].hasOwnProperty('secondGrey')){
          var Json = {
            title: '第二次灰度',
            slot: 'secondGrey',
            align:'center'
          };
          column.push(Json);
        };
        if(content[0].hasOwnProperty('thirdGrey')){
          var Json = {
            title: '第三次灰度',
            slot: 'thirdGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('forthGrey')){
          var Json = {
            title: '第四次灰度',
            slot: 'forthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('fifthGrey')){
          var Json = {
            title: '第五次灰度',
            slot: 'fifthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('sixthGrey')){
          var Json = {
            title: '第六次灰度',
            slot: 'sixthGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('seventhGrey')){
          var Json = {
            title: '第七次灰度',
            slot: 'seventhGrey',
            align:'center'
          };
          column.push(Json);
        };
         if(content[0].hasOwnProperty('eigthGrey')){
          var Json = {
            title: '第八次灰度',
            slot: 'eigthGrey',
            align:'center'
          };
          column.push(Json);
        };
        //最后再加入正式版数据
        column.push({
            title: '正式版',
            slot: 'official',
            align:'center'
          });


        instance.data = value['info']['nthird']; 
        instance.thirdPartData = value['info']['third'];
        instance.columns = column;
        })

      },
      topicManage (){
        this.isThirdPart = 0;
        this.propTopicManageIsActive = 0;
        this.propData = this.data;
        
      },
      relayManage (){
        this.isThirdPart = 1;
        this.propTopicManageIsActive = 0;
        this.propData = this.thirdPartData;
      },
      handleEditTopic (flag, row, index){
        if(flag ===0){
          this.editIndex = index;
        }
        else{
          this.editThirdIndex = index;
        }
        
        this.editValue = row.topic;
        this.editTopic = row.topic;
       
      },
      handleEditPrinciple (flag, row, index){
        if(flag ===0){
          this.editIndex = index;
        }
        else{
          this.editThirdIndex = index;
        }
        
        this.editValue = row.principle; 
        this.editPrinciple = row.principle;
      },
      handleSaveTopic (flag, id, index){
        let instance = this;
        if(flag === 0){
          this.data[index].topic = this.editTopic;
        }else{
          this.thirdPartData[index].topic = this.editTopic;
        }
        console.log(instance.data[index].topic)
        
        this.editIndex = -1;
        this.editValue = '';
        this.$options.methods.handleSendData(instance.client, instance.versionValue, 'topic', id, instance.editTopic);
      },
      handleSavePrinciple (flag, id, index){
        let instance = this;
        if(flag === 0){
          this.data[index].principle = this.editPrinciple;
          this.editIndex = -1;
          this.editValue = '';
          this.$options.methods.handleSendData(instance.client, instance.versionValue, 'principle', id, instance.editPrinciple);
        }else{
          this.thirdPartData[index].principle = this.editPrinciple;
          console.log(this.editPrinciple);
          this.editThirdIndex = -1;
          this.editValue = '';
          this.$options.methods.handleSendData(instance.client, instance.versionValue, 'principle', id, instance.editPrinciple);
        }
      },
      cancell (){
        this.editIndex = -1;
        this.editValue = '';
      },
      startSign (flag, row, value, index){
        this.flag = flag;
        this.id = row.id;
        this.signPassIsActive = 0;
        this.editTopic = row.topic;
        this.editProcess = value;
        if(flag ===0){
          this.editIndex = index;
          this.isPass = this.data[this.editIndex][this.editProcess];
        }
        else{
          this.editThirdIndex = index;
          this.isPass = this.thirdPartData[this.editThirdIndex][this.editProcess];
        }
        
         


      },
      handleIsPass(){
        let instance = this;
        this.signPassIsActive = 1;

        if (this.flag === 0) {
          this.data[this.editIndex][this.editProcess] = this.isPass;
          this.$options.methods.handleSendData (instance.client, instance.versionValue, instance.editProcess, instance.id, instance.isPass);
        }
        else{
          this.thirdPartData[this.editThirdIndex][this.editProcess] = this.isPass;
          this.$options.methods.handleSendData (instance.client, instance.versionValue, instance.editProcess, instance.id, instance.isPass);
        }
        
        
        this.editIndex = -1;
        this.editThirdIndex = -1;
        this.flag = -1;
        this.editProcess = '';
        this.id = -1;

      },
      handleSendData:(client,version,key,id,value) =>{
        var messsage = {'client':client, 'version':version, 'key':key,'id':id, 'value':value};
        axios({
          method:'get',
          url: 'http://release.baidu-int.com:8081/versionSign/updataversionclientinfo?id=1',
          params: {
            info: messsage
          }
        }).then(function(response){
          // console.log(response);
        }).catch(function(error){
          console.log(error);
        });
      },
      handleGetData (client, version){
        var messsage = {'client':client, 'version':version};
        return new Promise((resolve,reject) => {
          axios({
          method:'get',
          url: 'http://release.baidu-int.com:8081/versionSign/versionsigndata',
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
      startManageVersion () {
        this.propManageIsActive = 0;
      },
      cancellManage: function (data) {
          this.propManageIsActive = data[0];
          this.propVersion = data[1];
          //console.log(data);
      },
      cancellTopicManage:function(data){
          this.propTopicManageIsActive = data;
        },
      cancellUrgeSign (data){
        this.propUrgUserIsActive = data;
      },
      urgeSign: function (){
        var instance = this;
        this.propUrgUserIsActive = 0;
        var messsage = {'manage':'r', 'client':this.client, 'titleinfo':'','maininfo':'', 'infolist': ''};
        
         axios({
          method:'get',
          url: 'http://172.24.201.86:8888/workspace/urgsSign/manageConfigs.php',
          params: {
            info:messsage
          }
          
        }).then(function(response){
          
          instance.propIni = response.data;
        }).catch(function(error){
          console.log(error);
        });
      },
      getuser (info) {
        var instance = this;
        //console.log(this.selectlist);
              axios({
          method:'get',
          url: 'http://release.baidu-int.com:8081/versionSign/queryname',
          params:{
            username:info
          }
        }).then(function(response){
         

          var info = response.data.result;
          
           instance.userinfo = [];
           for (var i =0 ; i < info.length; i++) {
            
             var infojson = {
              username:info[i].username,
              name:info[i].name,
              department:info[i].departmentName,
              infotext:info[i].username + ' ' + info[i].name + ' 【' + info[i].departmentName +'】'
             };
             instance.userinfo.push(infojson);
             

           }

        }).catch(function(error){
          console.log(error);
        });

      },
    }
  }
</script>