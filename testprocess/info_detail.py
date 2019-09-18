#!/usr/bin/python
# -*- coding: UTF-8 -*-

#将获取的信息根据topic，RD负责人，QA负责人进行分类
class Cluster:
    '''
    info:从icafe拉取的数据字典


    '''
    info = ''
    topic = {}
    qaowner = {}
    rdowner = {}
    creater = {}

    def __init__(self, info):
        self.info = info

    def set_topic(self):
        card_num = len(self.info['cards'])
        for num in range(0, card_num):
            topic_name = self.info['cards'][num]['properties'][0]['displayValue']
            topic_name = topic_name.replace('&amp;amp;','&',5)  #搞不懂为什么弄出来&会变成&amp;amp;，所以就把她替换回来了
            urlId = self.info['cards'][num]['sequence']
            if(self.topic.has_key(topic_name)):
                self.topic[topic_name]['num'] += 1
                self.topic[topic_name]['urlId'].append(urlId)
            else:
                newDic = {topic_name:{'num':1,'urlId':[urlId]}}
                self.topic.update(newDic)

    def set_qaowner(self):
        card_num = len(self.info['cards'])
        for num in range(0, card_num):
            qa_name = self.info['cards'][num]['properties'][25]['displayValue']
            urlId = self.info['cards'][num]['sequence']
            if (self.qaowner.has_key(qa_name)):
                self.qaowner[qa_name]['num'] += 1
                self.qaowner[qa_name]['urlId'].append(urlId)
            else:
                newDic = {qa_name: {'num': 1, 'urlId': [urlId]}}
                self.qaowner.update(newDic)

    def set_rdowner(self):
        card_num = len(self.info['cards'])
        for num in range(0, card_num):
            rd_name = self.info['cards'][num]['properties'][47]['displayValue']
            urlId = self.info['cards'][num]['sequence']
            if (self.rdowner.has_key(rd_name)):
                self.rdowner[rd_name]['num'] += 1
                self.rdowner[rd_name]['urlId'].append(urlId)
            else:
                newDic = {rd_name: {'num': 1, 'urlId': [urlId]}}
                self.rdowner.update(newDic)


    def get_topic(self):
        return self.topic

    def get_qaowner(self):
        return self.qaowner

    def get_rdowner(self):
        return self.rdowner
    



