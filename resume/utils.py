#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: utils
@time: 2018/11/21
"""
import datetime
import random
def guess_your_love(positions,city,type,start_salary,end_salary):

    for position in positions:

        now = datetime.datetime.now()
        post_time = position.create_datetime
        timedelta = (now - post_time).days


        tags = position.org.tags.split(',')[:3]
        position.org.tags = tags

        point = 0
        if position.city == city:
            point +=random.randint(30,34)
        if position.type == type:
            point += random.randint(24,27)
        if int(position.start_salary[:-1]) > end_salary:
            point += random.randint(33,35)
        if int(position.start_salary[:-1]) > start_salary:
            point += random.randint(28,30)
        position.point = point
        position.timedelta = timedelta