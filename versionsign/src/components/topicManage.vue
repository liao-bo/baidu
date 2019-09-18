<style>
.topicManage{
  display: none;
}
.topicCreate{
  display: none;
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
  <div>
    <div v-bind:class="{topicManage:propTopicManageIsActive}" id="versionManage">
    <div class="overlayer"></div>
    <div class="wrap">
      <div class="modal">
        <div class="content">
          <div class="moder-header">
            管理topic
          </div>
          <div class="moder-body">
              <Table height='350':columns="columns" :data="propData">
              <template slot-scope="{ row, index }" slot="topic">                
                <span >{{ row.topic }}</span>
              </template>
              <template slot-scope="{ row, index }" slot="principle">              
                <span >{{ row.principle }}</span>
              </template>
              <template slot-scope="{ row, index }" slot="isThirdPart">              
                <span >{{ row.isThirdPart }}</span>
              </template>
              <template slot-scope="{ row, index }" slot="action">
                <div>
                  <Button @click="handleDelete(row)">删除</Button>
                </div>
              </template>
            </Table>
          </div>
          <div class="moder-footer">
            <Button @click="cancellManage()">取消</Button>
            <Button @click="newTopic()">新增一行</Button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-bind:class="{topicCreate:topicCreateIsActive}" id="topicCreate">
      <div class="overlayer"></div>
      <div class="wrap">
      <div class="modal">
      <div class="content">
      <div class="moder-header">
        增加一个Topic
      </div>
      <div class="moder-body">
        <div class="lable-item">
        <Row>
          <Col span="8">
            <div class = "lable">
               Topic:
            </div>
          </Col>
          <Col span="16">
             <div>
                <Input type="text" v-model="createdTopic" />
            </div>
          </Col>
        </Row>
          
        </div>
        <div class="lable-item">
        <Row>
          <Col span="8">
            <div class = "lable">
              对应的负责人：
            </div>
          </Col>
          <Col span="16">
             <div>
                <!-- <Input type="text" v-model="createdPrinciple" @on-change="getuser()"/>
                <template>
                  <Table :columns='columnsinfo' :data='userinfo' :show-header='false'>
                    <template slot-scope="{ row, index }" slot="infotext">
                      <a href="javascript:void(0);" @click="getName(row)">
                        {{row.infotext}}
                      </a>
                    </template>
                    
                  </Table>
                </template> -->

                <Select
                v-model="selectlist"
                filterable
                multiple
                remote
                :remote-method="getuser"
                :loading="loading">
                <Option v-for="(option, index) in userinfo" :value="option.username + ':' + option.name" :key="index">{{option.infotext}}</Option>
            </Select>
            </div>
          </Col>
        </Row>
          
        </div>
      </div>
      <div class="moder-footer">
        <Button @click="newTopicCreated()">确定</Button>
        <Button @click="cancellManage()">取消</Button>
      </div>
    </div>
    </div>
    </div>  
    </div>
    <template>
    
    <Modal
        v-model="modal"
        :title=title
        @on-ok="ok"
        @on-cancel="cancel">
        <p>topic：{{topic}}</p>
        <p>负责人：{{principle}}</p>
        
    </Modal>
</template>
</div>
</template>
<script>
import axios from 'axios'
  export default{
    props:['propData','propTopicManageIsActive','propClient','propVersion', 'isThird'],
    data () {
      return{

        columns: [
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
            title: '第三方',
            slot: 'isThirdPart',
            align:'center'
          },
          {
            title: '操作',
            slot: 'action',
            align: 'center'
          }
        ],
        topicCreateIsActive: 1, //判断新增版本窗口是否正常展示
        createdPrinciple:'',
        createdTopic:'',

        modal:false, //确定对话框是否展示
        handleKey:-1, //// key值控制后端做何中操作，0：创建新版本，1，增加一次灰度， 2.删除一次灰度，3.删除对应版本。
        title: '',
        topic:'',   //提示的topic展示词，以及传输到后端的topic
        id : -1,
        principle:'', //提示的负责人展示词，以及传输到后端的负责人
        username:'', //存储负责人的邮箱前缀
        key : -1,
        isThirdPart:0,
        columnsinfo:[
        {
          title:'用户信息',
          slot:'infotext'
        }

        ],
        userinfo:[],   //存储后端传回来的用户信息
        
        selectlist:[],  //保存选择的结果
        loading:false
      }
    },
    watch: {
      propClient: function(newval,oldval){
        this.client = newval;
       

      },
      propVersion: function(newval,oldval){
        this.newVersion = newval;
      }
    },
    methods: {
      dataManage (client, version, topic,principle,isThird, key,id='-1'){
        // key值控制后端做何中操作，0：删除一个topic，1，增加一个topic
        var message = {'client':client, 'version':version, 'topic':topic, 'principle':principle, 'isThirdPart':isThird, 'key':key, 'id':id};
        axios({
          method:'get',
          url: 'http://release.baidu-int.com:8081/versionSign/managetopicinfo',
          params: {
            info: message
          }
        }).then(function(response){
          //console.log(response);
        }).catch(function(error){
          //console.log(error);
        });
      },
      //取消函数，回到主页
      cancellManage: function() {
        this.topicCreateIsActive =1;
        this.$emit('listenTopicManageEvent',1);
      },
      //弹出创建版本弹窗 0
      newTopic () {
        this.topicCreateIsActive = 0;
        this.$emit('listenTopicManageEvent',1);
        
        
      },
      handleDelete(row) {
        this.topic = row['topic'];
        this.principle = row['principle'];
        this.id = row['id'];
        this.key = 0;
        this.modal = true;
        this.title = '是否删除这一行';


      },
      newTopicCreated (){
        if (this.createdTopic.length > 0 && this.selectlist.length > 0) {
          
          for (var i = 0; i<this.selectlist.length; i++){
            var name = this.selectlist[i].split(":")[1];
            var username =  this.selectlist[i].split(":")[0];
            if (this.principle.length > 0) {
              this.principle = this.principle + ","+name;
              this.username = this,username + "," + username;
            }
            else{
              this.principle = name;
              this.username = username;
            }
            
          }

          this.topic = this.createdTopic;
          //this.principle = this.createdPrinciple;
          this.key = 1;
          this.modal = true;
          this.title = '是否添加这一行';
        }

      },
      ok () {
       
        this.$options.methods.dataManage(this.propClient, this.propVersion, this.topic,this.principle,this.isThird, this.key,this.id);
        this.topicCreateIsActive =1;
        this.$emit('listenTopicManageEvent',1);
        this.createdPrinciple = '';
        this.createdTopic = '';
        this.username = '';
        this.topic='';
        this.id = -1;
        this.principle = '';
        this.key = -1;
        location.reload();
      },
      cancel () {
        
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
      getName (row) {
        this.createdPrinciple = row.username;
      }

    }  
  }
</script>