#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
#提供查询条件

import datetime
condition_name = {
        '1':'本版本所有有效Bug（客户端+第三方)',
        '2': '本版本所有有效客户端Bug',
        '3': '新版本发现有效客户端Bug数',
        '4': '新版本发现的新Bug数',
        '5': '老版本遗留bug',
        '6': '新版本发现的历史Bug数',
        '7': '版本Freeze后发现客户端Bug数',
        '8': '版本Freeze后发现客户端功能性Bug数',
        '9': '版本发现的客户端功能性Bug数',
        '10': '版本Freeze后发现客户端稳定性Bug数',
        '11': '版本发现的客户端稳定性Bug数',
        '12': '版本fix的bug数',
        '13': '新版本发现的新Bug Fix数',
        '14': '新版本发现的历史Bug Fix数',
        '15': '老版本遗留Bug Fix数',
        '16': '版本Freeze后Fix的客户端Bug数',
        '17': '遗留Bug数Active',
        '18': '遗留Bug数fix in future'

    }
class Condition:


    ioscondition_dic = {
        #  1. 本版本所有有效Bug（客户端+第三方）
        #  2. 本版本所有有效客户端Bug
        #  3. 新版本发现有效客户端Bug数
        #  4. 新版本发现的新Bug数
        #  5. 老版本遗留bug
        #  6. 新版本发现的历史Bug数
        #  7. 版本Freeze后发现客户端Bug数
        #  8. 版本Freeze后发现客户端功能性Bug数
        #  9. 版本发现的客户端功能性Bug数
        # 10. 版本Freeze后发现客户端稳定性Bug数
        # 11. 版本发现的客户端稳定性Bug数
        # 12. 版本fix的bug数
        # 13. 新版本发现的新Bug Fix数
        # 14. 新版本发现的历史Bug Fix数
        # 15. 老版本遗留Bug Fix数
        # 16. 版本Freeze后Fix的客户端Bug数

        '1': '''Bug方 in (客户端问题,第三方SDK) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion2旧版本遗留问题","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '2': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion2旧版本遗留问题","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '3': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '4': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '5': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion2旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '6': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '7': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59"''',
        '8': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '9': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '10': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59"''',
        '11': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '12': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion1Bugs","Vversion3新版本发现线上问题","Vversion2旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '13': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion1Bugs") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '14': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '15': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion2旧版本遗留问题") AND "Bug发现阶段(QA)" not in (自测/UT)''',
        '16': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in ("Vversion2旧版本遗留问题","Vversion1Bugs","Vversion3新版本发现线上问题") AND "Bug发现阶段(QA)" not in (自测/UT) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59"''',
        '17': '''流程状态 in (Active) AND 类型 in (Bug) AND 所属计划 in (历史问题/待计划,历史问题/待计划/音频冲突,历史问题/有计划,"iOS 11.6.0/要修复的线上问题/旧版本遗留问题") AND Bug方 in (客户端问题,第三方SDK)''',
        '18': '''类型 in (Bug) AND 所属计划 in (历史问题/待计划,历史问题/待计划/音频冲突,历史问题/有计划,"iOS 11.6.0/要修复的线上问题/旧版本遗留问题") AND Bug方 in (客户端问题,第三方SDK) AND Resolution in ("Fixed In Future")'''
    }

    androidcondition_dic = {
        #  1. 本版本所有有效Bug（客户端+第三方）
        #  2. 本版本所有有效客户端Bug
        #  3. 新版本发现有效客户端Bug数
        #  4. 新版本发现的新Bug数
        #  5. 老版本遗留bug
        #  6. 新版本发现的历史Bug数
        #  7. 版本Freeze后发现客户端Bug数
        #  8. 版本Freeze后发现客户端功能性Bug数
        #  9. 版本发现的客户端功能性Bug数
        # 10. 版本Freeze后发现客户端稳定性Bug数
        # 11. 版本发现的客户端稳定性Bug数
        # 12. 版本fix的bug数
        # 13. 新版本发现的新Bug Fix数
        # 14. 新版本发现的历史Bug Fix数
        # 15. 老版本遗留Bug Fix数
        # 16. 版本Freeze后Fix的客户端Bug数

        '1': '''Bug方 in (客户端问题,第三方问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '2': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '3': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '4': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '5': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '6': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '7': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59"''',
        '8': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '9': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND "Test Method" not in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '10': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59" AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '11': '''Bug方 in (客户端问题) AND Resolution not in ("Not a Bug",External,"By Design",Duplicate,"Not Repro",Incomplete,badcase持续跟进,fix_线上没复现,fix_线上干预解决,fix_策略解决,咨询) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND "Test Method" in (monkey,musi,鲁班,灰度,容灾,leakCanary)''',
        '12': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新功能引入问题,【version】新版本发现线上问题,【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '13': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新功能引入问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '14': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '15': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】线上版本遗留问题) AND Bug发现阶段（QA） not in (UT/自测)''',
        '16': '''Bug方 in (客户端问题) AND Resolution in (Fixed) AND Bug分析 in (【version】线上版本遗留问题,【version】新功能引入问题,【version】新版本发现线上问题) AND Bug发现阶段（QA） not in (UT/自测) AND 创建时间 > "timestart 23:59" AND 创建时间 < "timenow 23:59"''',
        '17': '''负责人 not in (yanghaoxiang) AND 流程状态 in (Active) AND 类型 in (Bug) AND 所属计划 in (历史问题/有计划,历史问题/待计划,"Android 11.6.0/要修复的线上问题/旧版本遗留问题") AND Bug方 in (客户端问题,第三方问题)''',
        '18': '''负责人 not in (yanghaoxiang) AND 类型 in (Bug) AND 所属计划 in (历史问题/有计划,历史问题/待计划,"Android 11.6.0/要修复的线上问题/旧版本遗留问题") AND Resolution in ("Fixed In Future") AND Bug方 in (客户端问题,第三方问题)'''
    }
    version = ''
    condition = ''
    label = 0
    # def __init__(self,label,version,timestart):
    #     self.label = label
    #     self.version = version
    #     self.condition = self.condition_dic.get(label)
    #     if(self.condition.find('time') != -1):
    #         self.condition = self.condition.replace('version', version)
    #         now_time = datetime.datetime.now().strftime('%Y-%m-%d')
    #         self.condition = self.condition.replace('timestart', timestart)
    #         self.condition = self.condition.replace('timenow', now_time)
    #     else:
    #         self.condition = self.condition.replace('version', version)

    def __init__(self,key,label,version1,version2,version3,timestart):
        self.label = label
        self.version = version1
        if(key > 0):
            self.condition = self.ioscondition_dic.get(label)
            self.condition = self.condition.replace('version1', version1)
            self.condition = self.condition.replace('version2', version2)
            self.condition = self.condition.replace('version3', version3)
            if(self.condition.find('time') != -1):
                now_time = datetime.datetime.now().strftime('%Y-%m-%d')
                self.condition = self.condition.replace('timestart', timestart)
                self.condition = self.condition.replace('timenow', now_time)
        else:
            self.condition = self.androidcondition_dic.get(label)
            self.condition = self.condition.replace('version', self.version)
            if(self.condition.find('time') != -1):
                now_time = datetime.datetime.now().strftime('%Y-%m-%d')
                self.condition = self.condition.replace('timestart', timestart)
                self.condition = self.condition.replace('timenow', now_time)
    def get_condition(self):
        return self.condition








