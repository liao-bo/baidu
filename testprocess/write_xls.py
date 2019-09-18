#!/usr/bin/python
# -*- coding: UTF-8 -*-

from icafe_info import IcafeInfo
from conditon_dic import Condition
from info_detail import Cluster
from conditon_dic import condition_name
from datetime import datetime
import xlwt

if __name__ == '__main__':

    timefirst = datetime.now()
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    topiclist = []  #存储涉及到的topic
    key = 0  #判断输出Android还是iOS，0为Android，1为iOS
    #version1 = '11.3.5 ' #输出Android的版本表示，直接输入数字，当切换到iOS是，需要使用3个表示，并且需要从icafe空间复制输入
    version1 = '11.10'
    version2 = '11.10'
    version3 = '11.10'
    timestart = '2019-06-04'  #版本上车的时间，格式为xxxx-xx-xx
    length = len(condition_name)
    """
    对condition进行遍历输出，并且写在Excel里面，
    对第一组数据查询完毕后，需要将涉及到的topic写入到excel，并且产生对应list，后续对其他list进行写入
    """
    for num in range(1,length+1):
        if(num == 1):
            label = str(num)  #标识查询条件
            newcondition = Condition(key,label, version1,version2,version3, timestart)
            condition = newcondition.get_condition()
            print condition
            newinfo = IcafeInfo(key,version1, condition)
            info = newinfo.get_info()

            infoDetail = Cluster(info)
            infoDetail.set_topic()
            topicdetail = infoDetail.get_topic()
            print(topicdetail)
            for topicname in topicdetail.keys():
                topiclist.append(topicname)
            worksheet.write(0,0,'度量项')
            worksheet.write(0,1,version1)
            worksheet.write(1, 0, condition_name['1'])
            worksheet.write(1, 1, info['total'])
            for col in range(0,len(topiclist)):
                worksheet.write(0,col+2,topiclist[col])
                worksheet.write(1,col+2,topicdetail[topiclist[col]]['num'])
            topicdetail.clear()
        else:
            label = str(num)
            #newcondition = Condition(label, version, timestart)
            newcondition = Condition(key,label, version1, version2, version3, timestart)
            condition = newcondition.get_condition()
            print condition
            newinfo = IcafeInfo(key,version1, condition)
            info = newinfo.get_info()

            infoDetail = Cluster(info)
            infoDetail.set_topic()
            topicdetail = infoDetail.get_topic()
            print(topicdetail)
            worksheet.write(num,0,condition_name[str(num)])
            worksheet.write(num,1,info['total'])
            for col in range(0, len(topiclist)):
                if(topicdetail.has_key(topiclist[col])):
                    worksheet.write(num, col+2,topicdetail[topiclist[col]]['num'])

            topicdetail.clear()



    if(key >0):
        filename = 'ios'+ version1
    else:
        filename = 'android'+ version1
    workbook.save(filename + '.xls')
    timeend = datetime.now()
    diff = (timeend - timefirst).seconds
    print("耗时为:" + str(diff))










