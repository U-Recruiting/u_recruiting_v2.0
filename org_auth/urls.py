#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register01/',views.register01, name='register01'),
    path('register02/',views.register02, name='register02'),
    path('complete_orginfo/', views.complete_orginfo, name='complete_orginfo'),
    path('myhome/',views.myhome, name='myhome')
]
