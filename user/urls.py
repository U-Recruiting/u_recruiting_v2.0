#!/usr/bin/python3
# -*- coding:utf-8 -*-
# time    : 2018/11/8 10:49 AM
# author  : shenchen

from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerView, name='register'),
    path('get_verification_code/', views.get_verification_code, name='get_verification_code'),
    path('complte_user_info/', views.complte_user_info, name='complte_user_info'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('setpassword/', views.setpasswordView, name='setpassword'),
    path('reset/',views.reset,name='reset'),
    path('email_verify/',views.email_verify,name='email_verify'),
    path('privacy/',views.privacy,name='privacy'),
    path('updatepwd/',views.updatepwd,name='updatepwd'),
    path('changepwd/', views.changepwd, name='changepwd'),
    path('test', views.test, name='test'),
    path('basic_information/',views.basic_information,name='basic_information')
]