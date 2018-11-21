#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/17
"""
from django.urls import path
from . import views
urlpatterns = [
    path('start/', views.spider),
    path('spider2/', views.spider2),
    path('spider3/', views.spider3),
]
