from django.shortcuts import render
from django.http import HttpResponse
from index.models import PositionInfo, PositionResumeStatus
from user.models import MyUser
import datetime
# Create your views here.


def details(request, position_id):
    buttin_text = '投递简历'
    collect_url = '/static/imgs/nocollected.png'
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        print(user.is_active)
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
            resume = user.resume_set.first()
            psr = PositionResumeStatus.objects.filter(position_id=position_id, resume_id=resume.id)
            user_colletion = user.collection_set.all()
            # print(user_colletion.filter(position_id = position_id))
            user_collection_position = user_colletion.filter(position_id=position_id)

            if psr:
                shoot_disabled = "disabled"
                buttin_text = '已投递'
            if user_collection_position:
                collect_disabled = "disabled"
                collect_url = "/static/imgs/collected.png"

        else:
            logined = False
    else:
        logined = False

    position_info_detail = PositionInfo.objects.get(id=position_id)

    position_resumed = []
    resumed = position_info_detail.resume.all()
    for resume in resumed:
        # 每个简历对应的除了查询岗位信息的所以岗位信息
        positions = resume.positioninfo_set.exclude(id=position_info_detail.id)
        # 所以简历对应岗位信息汇总
        position_resumed += positions
    position_resumed = position_resumed[:2]


    post_time = position_info_detail.create_datetime

    desc = position_info_detail.desc
    desc_list = desc.split('==1、')

    if len(desc_list) >=1:
        duty = desc_list[0].split('==')
    if len(desc_list)>=2:
        require = desc_list[1].split('==')
        if len(require)>0:
            require[0] = '1、'+require[0]

    if len(desc_list) >=3:
        other = desc_list[2].split('==')
        if len(other)>0:
            other[0] = '1、'+other[0]


    now = datetime.datetime.now()
    timedelta = (now - post_time).days

    return render(request, 'jobinfo.html', locals())