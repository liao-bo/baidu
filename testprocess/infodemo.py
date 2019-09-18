#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import requests
from urllib import quote
from conditon_dic import Condition
from icafe_info import IcafeInfo
from datetime import datetime


if __name__ == '__main__':
    time1 = datetime.now()
    key = 1
    label = '1'
    version = '11.8.0'
    version1 = '11.8.0'
    version2 = '11.8.0'
    version3 = '11.8.0'
    timestart = '2019-1-15'
    newcondition = Condition(key, label, version1, version2, version3, timestart)
    condition = newcondition.get_condition()
    print condition
    newinfo = IcafeInfo(key, version1, condition)
    info = newinfo.get_info()
    #data = json.loads(info)
    time2 = datetime.now()
    time = (time2-time1).seconds
    print time







