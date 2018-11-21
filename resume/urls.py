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
    path('myresume', views.my_resume, name='myresume'),

    path('edit_userinfo', views.edit_userinfo, name='edit_userinfo'),
    path('edit_workexp', views.edit_workexp, name='edit_workexp'),
    path('edit_projectexp', views.edit_projectexp, name='edit_projectexp'),
    path('edit_educationexp', views.edit_educationexp, name='edit_educationexp'),
    path('edit_huntingintent', views.edit_huntingintent, name='edit_huntingintent'),
    path('edit_avatar', views.edit_avatar, name='edit_avatar'),

    # path('mycollection',views.mycollection,name='mycollection'),
    path('mydelivery',views.mydelivery,name='mydelivery'),
    path('mysubscribe',views.mysubscribe,name='mysubscribe'),
    path('myrecommand',views.myrecommand,name = 'myrecommand'),
    path('preview',views.preview,name = 'preview'),





]