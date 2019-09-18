#!/usr/bin/python
# -*- coding: UTF-8 -*-

#请求相关查询信息
import json
import requests
from urllib import quote
class IcafeInfo:
    version = ''
    condition = ''
    info = ''

    def __init__(self,key,version,condition):
        self.version = version
        self.condition = condition
        self.key = key
    #返回字典格式的查询数据
    def get_info(self):
        if(self.key>0):
            url = '''http://icafe.baidu.com/api/spaces/BAIDUSEARCHIOS/cards/?u=chenran07&pw=Tntslx123&iql=''' + quote(self.condition)
        else:
            url =  '''http://icafe.baidu.com/api/spaces/BaiduSearchAndroid/cards/?u=chenran07&pw=Tntslx123&iql=''' + quote(self.condition)
        new_info  = requests.get(url)
        print url
        new_info = json.loads(new_info.text)
        pages = new_info['pageSize']
        print('page:'+str(pages)+'/n')
        if(pages > 1):  #如果存在多页数据，则继续请求并且拼装在同一组数据里面
            for page in range(2,pages+1):
                urldemo = url + '&page=' + str(page)
                print("page="+str(page)+"url="+url)
                info_tmp = requests.get(urldemo)

                info_tmp = json.loads(info_tmp.text)
                new_info['cards'].extend(info_tmp['cards'])
            self.info = new_info
            return self.info
        else:
            self.info = new_info
            return self.info



