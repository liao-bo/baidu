<style scoped>
	#index {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
	}

	.logo-frame {
		margin: 1rem 0 1rem 0;
	}

	/* .logo-frame img {
			width: 100%;
		} */

	p {
		text-align: center;
		font-size: 2rem;
	}

	h1 {
		font-weight: normal;
	}

	.content {
		height: 100%;
		overflow: auto;
		background: #fff;
		padding: 10px 20px;
		margin: 0;

	}

	.line {
		width: 100%;
		border-bottom: 3px solid #FFC125;
	}
</style>
<template>
	<div id="index">
		<div class="select">
			<template>
				<Row>
					<Col span="3" offset='3' align="center">
					端:
					<template>
						<Select v-model="client" style="width:100px">
							<Option v-for="item in clientList" :value="item.value" :key="item.value">{{ item.label }}
							</Option>
						</Select>
					</template>
					</Col>
					<Col span="3" offset='2' align="center">
					topic:
					<template v-if="client =='Android'">
						<Select v-model="topic" multiple filterable style="width:100px">
							<Option v-for="item in androidTopicList" :value="item.value" :key="item.value">
								{{ item.label }}
							</Option>
						</Select>
					</template>
					<template v-else>
						<Select v-model="topic" multiple filterable style="width:100px">
							<Option v-for="item in iOSTopicList" :value="item.value" :key="item.value">{{ item.label }}
							</Option>
						</Select>
					</template>
					</Col>
					<Col span="3" offset='2' align="center">
					版本号:
					<Input v-model="version" placeholder="Enter version" style="width: 100px" />
					</Col>
					<Col span="3" offset='2' align="center">
					<Button @click="check()" :style="{color:'#FFA500'}">查询</Button>
					</Col>
				</Row>
				<br />
				<br />
				<Row>
					<Col offset='3' span="18">
					<div class="line"></div>
					</Col>


				</Row>
				<br />

			</template>
			<div class="content">
				<template>
					<div v-if="client =='Android'">
						<Row v-for="item in AndroidCondition">
							<Col offset='3' span='5' align="center">
							{{item.name}}
							</Col>

							<Col span='10' align="center">
							<Input v-model=item.liveCondition type="textarea">

							</Input>

							</Col>
							<Col span='2' align="center">
							<Button @click="copy(item.liveCondition)">复制</Button>
							</Col>
							<Col span='2' align="center">
								<Button @click="jump(item.href)">跳转</Button>
								</Col>

						</Row>
					</div>
					<div v-else>
						<Row v-for="item in iOSCondition">
							<div>
								<Col offset='3' span='5' align="center">
								{{item.name}}
								</Col>

								<Col span='10' align="center">
								<Input v-model=item.liveCondition type="textarea">

								</Input>

								</Col align="center">
								<Col span='2'>
								<Button @click="copy(item.liveCondition)">复制</Button>
								</Col>
								<Col span='2' align="center">
									<Button  @click="jump(item.href)">跳转</Button>
									</Col>
							</div>
						</Row>
					</div>
				</template>
			</div>
		</div>
	</div>
</template>

<script>

	export default {

		data() {
			return {
				showCondition: 1,
				client: '',
				clientList: [
					{
						value: 'iOS',
						label: 'iOS'
					},
					{
						value: 'Android',
						label: 'Android'
					}
				],
				topic: [],
				topicCondition: '',
				androidTopicList: [
					{
						value: 'Feed',
						label: 'Feed'
					},
					{
						value: 'Feed：广告',
						label: 'Feed：广告'
					},
					{
						value: 'Feed：播放内核',
						label: 'Feed：播放内核'
					},
					{
						value: '视频',
						label: '视频'
					},
					{
						value: 'TTS',
						label: 'TTS'
					},
					{
						value: '搜索',
						label: '搜索'
					},
					{
						value: '搜索-浏览内核',
						label: '搜索-浏览内核'
					},
					{
						value: '游戏中心',
						label: '游戏中心'
					},
					{
						value: '基础功能',
						label: '基础功能'
					},
					{
						value: '"互动(评论&分享&关注&点赞&投票&表情)"',
						label: '互动(评论&分享&关注&点赞&投票&表情)'
					},
					{
						value: 'APS',
						label: 'APS'
					},
					{
						value: 'UGC',
						label: 'UGC'
					},
					{
						value: '"用户成长(Push&渠道&运营)"',
						label: '用户成长(Push&渠道&运营)'
					},
					{
						value: '超级兴趣',
						label: '超级兴趣'
					},
					{
						value: '基础性能',
						label: '基础性能'
					},
					{
						value: '基础技术',
						label: '基础技术'
					},
					{
						value: '垂类：小视频',
						label: '垂类：小视频'
					},
					{
						value: '第三方&插件&SDK',
						label: '第三方&插件&SDK'
					},
					{
						value: '闪屏',
						label: '闪屏'
					},
					{
						value: '灰度',
						label: '灰度'
					},
					{
						value: '容灾',
						label: '容灾'
					},
					{
						value: '内存',
						label: '内存'
					},
					{
						value: '静态代码扫描',
						label: '静态代码扫描'
					},
					{
						value: 'StrictMode',
						label: 'StrictMode'
					},
					{
						value: '其他',
						label: '其他'
					},
					{
						value: '流浪Bug',
						label: '流浪Bug'
					},
					{
						value: '小程序',
						label: '小程序'
					},
					{
						value: '小程序游戏',
						label: '小程序游戏'
					},
					{
						value: '垂类：小说',
						label: '垂类：小说'
					},
					{
						value: '垂类：动漫',
						label: '垂类：动漫'
					},
					{
						value: '搜索：播放内核',
						label: '搜索：播放内核'
					},
					{
						value: 'his/sug',
						label: 'his/sug'
					},
					{
						value: '直播',
						label: '直播'
					},
					{
						value: 'Talos',
						label: 'Talos'
					},
					{
						value: '语音搜索SDK',
						label: '语音搜索SDK'
					}
				],
				iOSTopicList: [
					{
						value: 'Feed',
						label: 'Feed'
					},
					{
						value: '广告',
						label: '广告'
					},
					{
						value: 'TTS',
						label: 'TTS'
					},
					{
						value: '视频',
						label: '视频'
					},
					{
						value: '直播',
						label: '直播'
					},
					{
						value: 'Talos',
						label: 'Talos'
					},
					{
						value: '小程序',
						label: '小程序'
					},
					{
						value: '小程序-小游戏',
						label: '小程序-小游戏'
					},
					{
						value: '搜索',
						label: '搜索'
					},
					{
						value: '视频播放内核',
						label: '视频播放内核'
					},
					{
						value: 'his/sug',
						label: 'his/sug'
					},
					{
						value: '垂类：小说',
						label: '垂类：小说'
					},
					{
						value: '垂类：动漫',
						label: '垂类：动漫'
					},
					{
						value: '"基础功能(基础功能&新特性&个人中心&皮肤中心&首页)"',
						label: '基础功能(基础功能&新特性&个人中心&皮肤中心&首页)'
					},
					{
						value: '游戏中心',
						label: '游戏中心'
					},
					{
						value: '"互动(评论&分享&关注&点赞&投票)"',
						label: '互动(评论&分享&关注&点赞&投票)'
					},
					{
						value: '"用户成长(Push&渠道&运营)"',
						label: '用户成长(Push&渠道&运营)'
					},
					{
						value: 'UGC',
						label: 'UGC'
					},
					{
						value: '基础性能',
						label: '基础性能'
					},
					{
						value: '"基础技术(网络库&热修复&组件化&AI&APS&UBC)"',
						label: '"基础技术(网络库&热修复&组件化&AI&APS&UBC)"'
					},
					{
						value: '垂类：小视频',
						label: '垂类：小视频'
					},
					{
						value: '第三方&插件&SDK',
						label: '第三方&插件&SDK'
					},
					{
						value: '灰度',
						label: '灰度'
					},
					{
						value: 'Monkey',
						label: 'Monkey'
					},
					{
						value: 'Musi',
						label: 'Musi'
					},
					{
						value: '内存',
						label: '内存'
					},
					{
						value: '容灾',
						label: '容灾'
					},
					{
						value: '其他',
						label: '其他'
					},
					{
						value: 'APS',
						label: 'APS'
					},
					{
						value: '超级兴趣',
						label: '超级兴趣'
					},
					{
						value: '搜索—大搜',
						label: '搜索—大搜'
					},
					{
						value: '流浪Bug',
						label: '流浪Bug'
					},
					{
						value: '语音搜索SDK',
						label: '语音搜索SDK'
					}
				],
				version: '',
				AndroidCondition: [
					{
						name: '本版本所有有效Bug（客户端+第三方）',
						condition: 'Bug方 in (客户端问题,第三方问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '本版本所有有效客户端Bug',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现有效客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的新Bug数(千行bug率)',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '老版本遗留bug',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的历史Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端功能性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本发现的客户端功能性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端稳定性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本发现的客户端稳定性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本fix的bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的新Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新功能引入问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的历史Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '老版本遗留Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后Fix的客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】线上版本遗留问题,【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					}
				],
				iOSCondition: [
					{
						name: '本版本所有有效Bug（客户端+第三方）',
						condition: 'Bug方 in (客户端问题,第三方SDK) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题","Vversion旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '本版本所有有效客户端Bug',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题","Vversion旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现有效客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的新Bug数(千行bug率)',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '老版本遗留bug',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的历史Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端功能性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本发现的客户端功能性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后发现客户端稳定性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本发现的客户端稳定性Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本fix的bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("VversionBugs","Vversion新版本发现线上问题","Vversion旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的新Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("VversionBugs") AND Bug发现阶段（QA） not in (UT/自测) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '新版本发现的历史Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '老版本遗留Bug Fix数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					},
					{
						name: '版本Freeze后Fix的客户端Bug数',
						condition: 'Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion旧版本遗留问题","VversionBugs","Vversion新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND Topic in (topicCondition)',
						liveCondition: '',
						href:''
					}
				]
			}
		},
		methods: {
			check() {
				if (this.client.length > 0 && this.topic.length > 0 && this.version.length > 0) {
					this.showCondition = 1;
					this.topicCondition = '';
					console.log(this.topicCondition);
					console.log(this.topic);
					for (let i = 0; i < this.topic.length; i++) {
						this.topicCondition += this.topic[i] + ',';

					}
					this.topicCondition = this.topicCondition.substr(0, this.topicCondition.length - 1);
					if (this.client == 'Android') {
						for (let i = 0; i < this.AndroidCondition.length; i++) {
							this.AndroidCondition[i].liveCondition = this.AndroidCondition[i].condition.replace(/version/g, this.version).replace(/topicCondition/g, this.topicCondition);
							this.AndroidCondition[i].href = "http://newicafe.baidu.com/issues/space/BaiduSearchAndroid?viewMode=list&newFilterMode=true&c=[type][status][owner][createTime]&iql="+this.iOSCondition[i].liveCondition;
						}
					}
					else {
						for (let i = 0; i < this.iOSCondition.length; i++) {
							this.iOSCondition[i].liveCondition = this.iOSCondition[i].condition.replace(/version/g, this.version).replace(/topicCondition/g, this.topicCondition);
							this.iOSCondition[i].href = "http://newicafe.baidu.com/issues/space/BAIDUSEARCHIOS?viewMode=list&newFilterMode=true&c=[type][status][owner][createTime]&iql="+this.iOSCondition[i].liveCondition;
						}
					}
				}
				else {
					this.$Message.warning('请选择端，topic以及版本号');
				}

			},
			jump(href) {
				window.open(href);
			},
			copy(message) {
				let instance = this;
				console.log("dao;e");
				this.$copyText(message).then(function (e) {
					instance.$Message.success("复制成功");
				}, function (e) {
					instance.$Message.warning("复制失败");
					console.log(e);
				})
			}
		}
	};
</script>