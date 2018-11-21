#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: utils
@time: 2018/11/17
"""

import http.client
from urllib.parse import urlencode
import json
from index.models import *

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
# account = "C54497082"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
# password = "f51f0849e2c3dc9aa8e1fef5d57de89f"


# def send_sms(text, mobile):
#     params = urlencode(
#         {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
#     headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
#     conn = http.client.HTTPConnection(host, port=80, timeout=30)
#     conn.request("POST", sms_send_uri, params, headers)
#     response = conn.getresponse()
#     response_str = response.read()
#     conn.close()
#     return response_str

def add_blank_resume(user):
    UserInfo.objects.create(name='',user_id=user.id )
    WorkExp.objects.create(name='',user_id=user.id )
    ProjectExp.objects.create(name='',user_id=user.id)
    EducationExp.objects.create(name='',user_id=user.id)
