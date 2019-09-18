#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import demjson
from icafe_info import IcafeInfo
from conditon_dic import Condition
from info_detail import Cluster


if __name__ == '__main__':
    label = '1'
    version = '11.3'
    timestart = '2018-12-7'


    newcondition = Condition(label,version,timestart)
    condition = newcondition.get_condition()
    newinfo = IcafeInfo(version,condition)
    info = newinfo.get_info()

    infoDetail = Cluster(info)

    infoDetail.set_topic()
    topicdetail = infoDetail.get_topic()
    for topicname in topicdetail.keys():
        print topicname

