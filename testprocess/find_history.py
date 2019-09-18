#!/usr/bin/python
# -*- coding: UTF-8 -*-

#请求相关查询信息
import json
import requests


class History:






    ios_url = "http://icafe.baidu.com/api/v2/space/BAIDUSEARCHIOS/issue/history"
    android_url = "http://icafe.baidu.com/api/v2/space/BaiduSearchAndroid/issue/history"


    body = {"username":"chenran07",
       "password" : "Wzqhjqsy123",
       "sequences" : [38270]
            }


    response = requests.post(ios_url, data = json.dumps(body))
