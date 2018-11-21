from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.models import PositionInfo, PositionResumeStatus
from user.models import MyUser
import datetime
# Create your views here.
import json

def shoot(request):
    position_id = request.POST.get('position_id', '')
    # # 获取投递岗位
    position = PositionInfo.objects.get(id=position_id)
    print(position_id)
    # 该岗位那些人投递了

    position_resumed = []
    #
    # 该岗位所以简历
    resumed = position.resume.all()
    for resume in resumed:
        # 每个简历对应的除了查询岗位信息的所以岗位信息
        positions = resume.positioninfo_set.exclude(id=position.id)
        # 所以简历对应岗位信息汇总
        position_resumed += positions
    # 当前用户

    # 获取用户简历




    # 填入岗位信息表（多对多）

    user = request.user
    if user.is_active:
        print('asadmaskdnajdks')
        resume = user.resume_set.first()
        position.resume.add(resume)

        date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        prs = PositionResumeStatus.objects.filter(position_id=position.id, resume_id=resume.id)
        if not prs:
            PositionResumeStatus(position_id=position.id, resume_id=resume.id,datetime=date, status='received').save()
        data = {"to": "success"}
    else:
        url = '/user/login/?next=/position/{0}'.format(position_id)
        data = {"to":url}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")
