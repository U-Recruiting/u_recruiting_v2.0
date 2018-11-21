#!usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""

from django.urls import path
from . import views

app_name = 'org'
urlpatterns = [

    # path('', views.test_eacharts),  # home 默认显示待处理简历
    path('create/', views.create, name='create'),  # 发布职位
    # path('create_success/', views.create_success, name='create_success'),

    path('my_org/<str:item>/', views.org_view),
    path('get_ajax_resumes/', views.get_ajax_resumes, name='get_resumes_db'),
    path('get_ajax_positions/', views.get_ajax_positions, name='get_positions_db'),
    path('get_html/', views.get_html, name='get_html'),
    path('interview_or_pass_or_refuse', views.interview_or_pass_or_refuse_ajax, name='update_resume_status'),
    path('delete_position/', views.delete_position, name='delete_position'),
    path('update_position_status/',views.update_position_status,name='update_position_status'),
    # path('get_photo/',views.get_photo, name='get_photo'),

    # 测试功能
    path('get_resumes/', views.get_resume, name='get_resumes'),
    path('get_position', views.get_position, name='get_position'),
]
