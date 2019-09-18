<style>
.urgManage{
  display: none;
}
.urge{
  display: none;
}
.shouldurge{
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
    font-size: 14px;
    color: #17233d;
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
		<div>
    <div v-bind:class="{urgManage:propUrgUserIsActive}" id="versionManage">
    <div class="overlayer"></div>
    <div v-bind:class="{urge:urgeisactive}">
    <div class="wrap">
      <div class="modal">
        <div class="content">
          <div class="moder-header">
            签章提醒
          </div>
          <div class="moder-body">
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                     titleinfo:
                  </div>
                </Col>
                <Col span="18">
                  <div>
                    <Input type="textarea" :rows="3"  v-model = "propIni['titleinfo']"/>
                   
                  </div>
                </Col>
              </Row>
          
            </div>
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                    maininfo:
                  </div>
                </Col>
                <Col span="18">
                   <div>
                     <Input type="textarea" :rows="3"  v-model = "propIni['maininfo']" />
                  </div>
                </Col>
              </Row>
          
            </div>
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                    infolist:
                  </div>
                </Col>
                <Col span="18">
                   <div>
                      <Input type="textarea" :rows="3" v-model = "propIni['infolist']"/>
                  </div>
                </Col>
              </Row>
          
            </div>
          </div>
          <div class="moder-footer">
            <Button @click="cancell()">取消</Button>
            <Button @click="begin()" type = 'primary'>确定</Button>
          </div>
        </div>
      </div>
    </div>
    </div>
    <div v-bind:class="{shouldurge:shouldurgeisactive}">
    <div class="wrap">
      <div class="modal">
        <div class="content">
          <div class="moder-header">
            是否催签章
          </div>
          <div class="moder-body">
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                     titleinfo:
                  </div>
                </Col>
                <Col span="18">
                  <div>
                    <span>
                      {{propIni['titleinfo']}}
                    </span>
                   
                  </div>
                </Col>
              </Row>
          
            </div>
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                    maininfo:
                  </div>
                </Col>
                <Col span="18">
                   <div>
                    <span>
                      {{propIni['maininfo']}}
                    </span>
                    
                  </div>
                </Col>
              </Row>
          
            </div>
            <div class="lable-item">
              <Row>
                <Col span="6">
                  <div class = "lable">
                    infolist:
                  </div>
                </Col>
                <Col span="18">
                   <div>
                    <span>
                      {{propIni['infolist']}}
                    </span>
                  </div>
                </Col>
              </Row>
          
            </div>
            
          </div>
          <div class="moder-footer">
            <Button @click="cancell()">取消</Button>
            <Button @click="writelist()">白名单</Button>
            <Button @click="selftest()">自测</Button>

            <Button @click="ok()" type='primary' disabled v-show="!canclick">确定</Button>
            <Button @click="ok()" type='primary' v-show="canclick">确定</Button>
          </div>
        </div>
        </div>
      </div>
    </div>
  </div>
	</div>
 <!--  <Modal
        v-model="modal"
        :title=title
        @on-ok="ok"
        @on-cancel="cancel">
        <p>titleinfo:{{titleinfo}}</p>
        <p>maininfo:{{maininfo}}</p>
        <p>infolist:{{infolist}}</p>
        
    </Modal> -->
</div>
</template>

<script>
import axios from 'axios'
	export default{
    props:['propIni','propUrgUserIsActive','propClient','propVersion'],
    data () {
      return{
        modal:false,
        title:'是否催签章',
        titleinfo:'',
        maininfo:'',
        infolist:'',
        urgeisactive:0,
        shouldurgeisactive:1,
        canclick:false





      }
    },
    methods: {
      cancell (){
        this.$emit('listenUrgeSignEvent',1);
        this.canclick = false;
      },
      begin () {

        var data = this.propIni;
        this.titleinfo = data['titleinfo'];
        this.maininfo = data['maininfo'];
        this.infolist = data['infolist'];
        this.urgeisactive = 1;
        this.shouldurgeisactive = 0;

        
      },
      ok () {

          var messsage = {'manage':'w', 'client':this.propClient, 'titleinfo':this.titleinfo,'maininfo':this.maininfo, 'infolist': this.infolist, 'mode':0};
          axios({
          method:'get',
          url: 'http://172.24.201.86:8888/workspace/urgsSign/manageConfigs.php',
          params: {
            info: messsage
          }
          
        }).then(function(response){
          console.log(response.data);
        }).catch(function(error){
          console.log(error);
        });

        this.urgeisactive = 0;
        this.shouldurgeisactive = 1;
        this.$emit('listenUrgeSignEvent',1);
        this.canclick = false;

      },
      selftest () {
        var messsage = {'manage':'w', 'client':this.propClient, 'titleinfo':this.titleinfo,'maininfo':this.maininfo, 'infolist': this.infolist, 'mode':1};

          axios({
          method:'get',
          url: 'http://172.24.201.86:8888/workspace/urgsSign/manageConfigs.php',
          params: {
            info: messsage
          }
          
        }).then(function(response){
          console.log(response.data);
        }).catch(function(error){
          console.log(error);
        });
        this.canclick = true;

      },
      writelist () {
        var messsage = {'manage':'w', 'client':this.propClient, 'titleinfo':this.titleinfo,'maininfo':this.maininfo, 'infolist': this.infolist, 'mode':2};
          axios({
          method:'get',
          url: 'http://172.24.201.86:8888/workspace/urgsSign/manageConfigs.php',
          params: {
            info: messsage
          }
          
        }).then(function(response){
          console.log(response.data);
        }).catch(function(error){
          console.log(error);
        });
        this.canclick = true;

      }

    }
  }  
</script>