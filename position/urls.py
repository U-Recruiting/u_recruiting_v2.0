#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/13
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<int:position_id>', views.details, name='position'),
]

