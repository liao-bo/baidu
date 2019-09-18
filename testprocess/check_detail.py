#!/usr/bin/python
# -*- coding: UTF-8 -*-
#检查是否有相关信息未被填写
class checkDetail:

    topic_detail = {}
    qa_detail = {}
    rd_detail = {}

    def check_topic(self):
        card_num = len(self.info['cards'])
        for num in range(0, card_num):
            if(len(self.info['cards'][num]['properties'][0]['displayValue']) > 0):
                continue




