from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from index.models import *
from index.models import PositionInfo, OrgInfo
from django.core import serializers
# Create your views here.
import json


def delivery(request):
    # 当前用户
    # user = request.user
    #
    # print(user)
    #
    # # 当前用户简历
    # resume = user.resume_set.all()[0]
    #
    # # 简历所投岗位
    # positions = resume.positioninfo_set.all()
    #
    # print(positions)

    return render(request, 'deliverybox_test.html', locals())


def mycollection(request):
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False

    if request.method == 'GET':
        collections = Collection.objects.filter(user_id=user.id)
        positions = []
        for collection in collections:
            collection.position.adv = collection.position.positionAdvantage.split(',')[:2]
            positions.append(collection.position)
    return render(request, 'myjob_collection.html', locals())


def collect(request):
    print(request.POST)
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        position_id = request.POST.get('position_id', '')
        Collection.objects.create(position_id=position_id, user_id=user.id)
        data = {"message": "success"}
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")

    return HttpResponse('ok')


def companydetail(request):
    return render(request, 'companydetail.html')


def delivery_resumes(request):
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False
    return render(request, 'delivery_resumes.html', locals())


def get_delivery_status(request):
    status = dict(request.POST)['status'][0]

    user = request.user
    resume_info = user.resume_set.all().first()

    if status == 'all':
        delivery_position_info = resume_info.positionresumestatus_set.all()
    else:
        delivery_position_info = resume_info.positionresumestatus_set.filter(status=status)

    resume_status_info = json.loads(serializers.serialize('json', delivery_position_info), encoding='utf-8')
    # print(resume_status_info)
    position_list = format_position(resume_status_info)
    return JsonResponse(position_list, safe=False)


def format_position(status_list):
    position_list = []
    translate_dict = {
        'received': '投递成功',
        'notified': '通知面试',
        'passed': '已录用',
        'refused': '不合适',
    }
    for one_status in status_list:
        position_id = one_status['fields']['position']
        position = PositionInfo.objects.get(id=position_id)
        position_dict = {
            'position_name': position.name,
            'position_id': position.id,
            'mix_salary': position.start_salary,
            'max_salary': position.end_salary,
            'work_city': position.city,
            'org_name': OrgInfo.objects.get(id=position.org_id).name,
            'post_date': str(one_status['fields']['datetime']).replace('T', ' '),
            'status': translate_dict[one_status['fields']['status']]
        }
        position_list.append(position_dict)
    return position_list


def get_spss(request):
    return render(request, 'person_jianli.html')
