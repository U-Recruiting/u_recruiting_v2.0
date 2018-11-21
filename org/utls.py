#!usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:shenchen
@file: utls
@time: 2018/11/16
"""
from user.models import MyUser
from index.models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import json


def get_resume_item(positions, order: str):
    received = []
    for position in positions:
        position_resume_status = position.positionresumestatus_set.filter(status=order).order_by('-datetime')
        # resumes = []
        # print(position_resume_status)
        for one_position_resume_status in position_resume_status:
            one_resume = {}
            one_resume['name'] = one_position_resume_status.resume.user_info.name
            one_resume['mobile'] = one_position_resume_status.resume.user_info.user.mobile
            one_resume['email'] = one_position_resume_status.resume.user_info.user.email
            one_resume['sex'] = one_position_resume_status.resume.user_info.sex
            one_resume['education'] = one_position_resume_status.resume.user_info.education
            one_resume['school'] = one_position_resume_status.resume.user_info.school
            one_resume['work_years'] = one_position_resume_status.resume.user_info.work_years
            one_resume['city'] = one_position_resume_status.resume.user_info.city
            one_resume['position_name'] = position.name
            one_resume['address'] = position.address
            one_resume['position_id'] = one_position_resume_status.position_id
            one_resume['resume_id'] = one_position_resume_status.resume_id
            one_resume['post_date'] = str(one_position_resume_status.datetime).replace('T', ' ')
            one_resume['worked_position'] = one_position_resume_status.resume.work_exp.position_name
            one_resume['worked_company'] = one_position_resume_status.resume.work_exp.company
            received.append(one_resume)
        # received[position.name] = resumes
    return received


def format_position_item(positions):
    positions_list = []
    for position in positions:
        fields = position['fields']
        temp_dict = {
            "position_id": position['pk'],
            "position_name": fields['name'],
            "city": fields['city'],
            "position_type": fields['type'],
            "min_salary": fields['start_salary'],
            "max_salary": fields['end_salary'],
            "work_exp": fields['work_exp'],
            "edu_exp": fields['edu_exp'],
            "post_date": str(fields['create_datetime']).replace('T', ' ')
        }
        positions_list.append(temp_dict)
    # print(positions_list)
    return positions_list


def update_pisition_resume_status(position_id, resume_id, status):
    PositionResumeStatus.objects.filter(position_id=position_id, resume_id=resume_id).update(status=status,
                                                                                             # address=interview_address,
                                                                                             # datetime=interview_datatime
                                                                                             )
    # resume = PositionResumeStatus.objects.filter(resume_id=resume_id).first().resume
    # user = resume.user
    # user_email = user.email
    #
    # from_email = settings.DEFAULT_FROM_EMAIL
    #
    # position = PositionInfo.objects.filter(id=position_id).first()
    # org_name = position.org.name
    # if status == 'notified':
    #     message = '恭喜！您投递的 【' + org_name + '】的【' + position.name + '】岗已经通过筛选' + '\n' + '您的面试地址为: ' + interview_address + '\n' + '您的面试时间为: ' + interview_datatime
    # elif status == 'refused':
    #     message = '对不起 ！您投递的 【' + org_name + '】的【' + position.name + '】岗没有通过筛选'
    # elif status == 'passed':
    #     message = '恭喜！您投递的 【' + org_name + '】的【' + position.name + '】岗已经通过面试'
    # send_mail('岗位投递通知', message, from_email, [user_email])
    data = {'message': 'success'}
    return data
