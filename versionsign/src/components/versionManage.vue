<style>
.versionManage{
  display: none;
}
.versionCreate{
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
  <div v-bind:class="{versionManage:propManageIsActive}" id="versionManage">
    <div class="overlayer"></div>
    <div class="wrap">
      <div class="modal">
        <div class="content">
          <div class="moder-header">
            修改版本数据
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
               {{propClient}}
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
                {{propVersion}}
            </div>
          </Col>
        </Row>
          
        </div>


          <!-- <div>
            对应的端：{{propClient}}
          </div>
          <div>
            对应的版本：{{propVersion}}
          </div>  -->
          </div>
          <div class="moder-footer">
            <Button @click="cancellManage()">取消</Button>
            <Button @click="handleCreateVersion()">创建版本</Button>
            <Button @click="handleisCreateGrey()">新增一次灰度</Button>
            <Button @click="handleisDeleteGrey()">删除一次灰度</Button>
            <Button @click="handleisDeleteVersion()">删除对应版本</Button>
          </div>
        </div>
      </div>  
    </div>
    </div>
    <div v-bind:class="{versionCreate:versionCreateIsActive}" id="versionCreate">
      <div class="overlayer"></div>
      <div class="wrap">
      <div class="modal">
      <div class="content">
      <div class="moder-header">
        增加一个版本
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
               <template>
                <div>
                <RadioGroup v-model="propClient">
                  <Radio label="iOS">            
                    <span>iOS</span>
                  </Radio>
                  <Radio label="Android">
                    <span>Android</span>
                  </Radio>
                </RadioGroup>
                </div>
              </template>
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
                <Input type="text" v-model="newVersion" />
            </div>
          </Col>
        </Row>
          
        </div>
      </div>
      <div class="moder-footer">
        <Button @click="newVersionCreated()">创建</Button>
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
        <p>端：{{propClient}}</p>
        <p>版本号：{{alertVersion}}</p>
        
    </Modal>
</template>
  </div>
</template>
<script>
import axios from 'axios'
  export default{
    props:['propClient','propVersion','propManageIsActive'],
    data () {
      return{
        versionCreateIsActive: 1, //判断新增版本窗口是否正常展示
        newVersion:'',
        modal:false, //确定对话框是否展示
        handleKey:-1, //// key值控制后端做何中操作，0：创建新版本，1，增加一次灰度， 2.删除一次灰度，3.删除对应版本。
        title: '',
        alertVersion:''//提醒的版本号
      }
    },
    watch: {
      propClient: function(newval,oldval){
        this.client = newval;
        //console.log(1111);

      },
      propVersion: function(newval,oldval){
        this.newVersion = newval;
      }
    },
    methods: {
      dataManage (client, version, key){
        // key值控制后端做何中操作，0：增加一个新版本，1，增加一次灰度， 2.删除一次灰度，3.删除对应版本。
        var message = {'client':client, 'version':version, 'key':key};
         return new Promise((resolve,reject) => {
        axios({
          method:'get',
          url: 'http://release.baidu-int.com:8081/versionSign/manageversioninfo',
          params: {
            info: message
          }
        }).then(response => {
          resolve(response.data);
          }).catch(error => {
            reject(error);
            })
          })
      },
      //取消函数，回到主页
      cancellManage: function() {
        this.versionCreateIsActive =1;
        this.$emit('listenManageEvent',[1,'']);
      },
      //弹出创建版本弹窗 0
      handleCreateVersion () {
        this.versionCreateIsActive = 0;
        this.newVersion = this.propVersion;
        this.$emit('listenManageEvent',[1,'']);
        
        
      },
      //弹出是否创建一次灰度 1
      handleisCreateGrey () {
        var instance = this;
        this.versionCreateIsActive =1;
        this.$emit('listenManageEvent',[1,'']);
        this.modal = true;
        this.handleKey = 1;
        this.title = '是否新增一次灰度';
        this.alertVersion = this.propVersion;
        
      },
      // 是否删除一次灰度 2
      handleisDeleteGrey (){
        this.versionCreateIsActive =1;
        this.$emit('listenManageEvent',[1,'']);
        this.modal = true;
        this.handleKey = 2;
        this.title = '是否删除一次灰度';
        this.alertVersion = this.propVersion;
      },
      //是否删除一次版本
      handleisDeleteVersion (client, version){

        this.versionCreateIsActive =1;
        this.$emit('listenManageEvent',[1,'']);
        this.modal = true;
        this.handleKey = 3;
        this.title = '是否删除一个版本';
        this.alertVersion = this.propVersion;
      },
      ok () {
        var instance = this;

        if (this.handleKey === 0) {
          this.$options.methods.handleNewVersion(instance);
          this.newVersion = '';
          
        }
        else if(this.handleKey === 1){
          this.$options.methods.handleCreateGrey(instance);
          
        }
        else if (this.handleKey ===  2) {
          this.$options.methods.handleDeleteGrey(instance);
          
        }
        else if (this.handleKey === 3) {
          this.$options.methods.handleDeleteVersion(instance);
          
        }
        else{
          this.$options.methods.cancel(instance);
          
        }


        
      },
      cancel () {
        
      },
      //询问创建新版本 0
      newVersionCreated: function () {
        var instance = this;
        this.versionCreateIsActive =1;
        this.$emit('listenManageEvent',[1,instance.newVersion]);
        this.modal = true;
        this.handleKey = 0;
        this.title = '是否新增一个版本';
       
        this.alertVersion = this.newVersion;

      },
      //创建新版本
      handleNewVersion(instance){
        var client = instance.propClient;
        var version = instance.newVersion;

        instance.$options.methods.dataManage(client, version, 0).then(function(value){
          instance.title = '';
          location.reload();
          instance.alertVersion = "";

        });
        

      },
      // 创建一次灰度 1
      handleCreateGrey (instance) {
        var client = instance.propClient;
        var version = instance.propVersion;
        instance.$options.methods.dataManage(client, version, 1).then(function(value){

          instance.title = '';
          location.reload();
          instance.alertVersion = "";
        });
        

      },
      //删除一次灰度 2
      handleDeleteGrey (instance) {
        var client = instance.propClient;
        var version = instance.propVersion;
        instance.$options.methods.dataManage(client, version, 2).then(function(value){
          instance.title = '';
          location.reload();
          instance.alertVersion = "";
        });
        
      },
      //删除一个版本
      handleDeleteVersion (instance){
        var client = instance.propClient;
        var version = instance.propVersion;
        instance.$options.methods.dataManage(client, version, 3).then(function(value){
          console.log(value);
          instance.title = '';
          location.reload();
          instance.alertVersion = "";
        });
        
      }

    }  
  }
</script>