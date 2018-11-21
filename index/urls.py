#!/usr/bin/python3
# -*- coding:utf-8 -*-
# time    : 2018/11/8 10:49 AM
# author  : shenchen

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('aboutus/',views.aboutus),
]
