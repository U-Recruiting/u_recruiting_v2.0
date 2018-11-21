from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from index.models import *
from user.models import MyUser
from django.core import serializers
import datetime
import json
from . import utls


# Create your views here.

# @login_required(login_url='/user/login')


# def home(request):
#     user = MyUser.objects.get(email='1234@test.com')
#     orginfo = user.orginfo_set.all().first()
#     positions = orginfo.positioninfo_set.all()
#     received = utls.get_resume_item(positions, 'received')
#     print(received)
#     return render(request, 'resumes_view.html', locals())


def create(request):
    user = request.user
    # user = MyUser.objects.get(email='1234@test.com')
    orginfo = user.orginfo_set.all().first()

    position_info = dict(request.POST)

    create_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    position = PositionInfo(
        status='valid',
        type=position_info['position_type'][0],
        name=position_info['position_name'][0],
        department=position_info['department'][0],
        job_catagory='',
        start_salary=position_info['min_salary'][0],
        end_salary=position_info['max_salary'][0],
        city=position_info['work_city'][0],
        distinct='',
        address=position_info['position_address'][0],
        work_exp=position_info['work_experience'][0],
        edu_exp=position_info['edu_experience'][0],
        # tags=tags,
        # desc=desc,

        positionAdvantage=position_info['position_advantage'][0],
        desc=str(position_info['position_res'][0]).replace('\n', '==') + '==' + str(
            position_info['position_require'][0]).replace('\n', '==')
             + '==' + str(position_info['position_other'][0]).replace('\n', '=='),
        # positionRes=position_info['position_res'][0],
        # positionRequire=position_info['position_require'][0],
        # positionOther=position_info['position_other'][0],
        # subwayline=subwayline,
        # linestaion=linestaion,
        create_datetime=create_datetime,
        org_id=orginfo.id
    )
    position.save()

    # print(position_info)
    return JsonResponse({'message': 'success'}, safe=False)


def delete_position(request):
    user = request.user
    # user = MyUser.objects.get(email='1234@test.com')
    orginfo = user.orginfo_set.all().first()
    position_id = dict(request.POST)['position_id'][0]
    PositionInfo.objects.filter(id=position_id, org_id=orginfo.id).delete()
    return JsonResponse({'message': 'success'})


def get_ajax_resumes(request):
    """
    根据请求的项目返回对应的简历Json
    :param request:
    :return:
    """
    user = request.user
    # user = MyUser.objects.get(email='1234@test.com')
    # print(user.date_joined)
    org_info = user.orginfo_set.all().first()
    positions = org_info.positioninfo_set.all()

    order = dict(request.POST)['item'][0]
    received = utls.get_resume_item(positions, order)
    return JsonResponse(received, safe=False)


# @login_required(login_url='/user/login')


def get_ajax_positions(request):
    """
    获取公司对应职位
    ——————————
    :param request:
    :return: 职位列表
    """
    user = request.user
    # user = MyUser.objects.get(email='1234@test.com')
    orginfo = user.orginfo_set.all().first()
    status = dict(request.POST)['item'][0]

    positions = orginfo.positioninfo_set.filter(status=status).order_by('-create_datetime')

    json_positions = serializers.serialize('json', positions)
    positions_list = utls.format_position_item(json.loads(json_positions, encoding='utf-8'))

    return JsonResponse(positions_list, safe=False)


def interview_or_pass_or_refuse_ajax(request):
    print(request.POST)
    status = dict(request.POST)['status'][0]
    position_id = int(dict(request.POST)['position_id'][0])
    resume_id = int(dict(request.POST)['resume_id'][0])

    # interview_address = request.POST.get('interview_address', '')
    # interview_datatime = request.POST.get('interview_datatime', '')

    res = utls.update_pisition_resume_status(position_id=position_id, resume_id=resume_id,
                                             # interview_address=interview_address,
                                             # interview_datatime=interview_datatime,
                                             status=status)
    return JsonResponse(res, safe=False)


def update_position_status(request):
    user = request.user
    # user = MyUser.objects.get(email='1234@test.com')
    orginfo = user.orginfo_set.all().first()
    position_id = dict(request.POST)['position_id'][0]
    status = dict(request.POST)['status'][0]
    position = PositionInfo.objects.filter(id=position_id, org_id=orginfo.id)

    position.update(status=status, create_datetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return JsonResponse({'message': 'success'})


def get_resume(request):
    """
    根据请求的项目返回对应的简历Json
    :param request:
    :return:
    """
    demo_json = [{"sex": "男",
                  "education": "硕士",
                  "email": "test@123.com",
                  "resume_id": 1,
                  "address": "亦庄文化园",
                  "name": "冰激淋",
                  "school": "联通学院",
                  "city": "北京",
                  "position_name": "java开发",
                  "position_id": 5312625,
                  "mobile": "18812312345",
                  "org": "中国联通",
                  "work_years": "1"},
                 {"sex": "女",
                  "education": "硕士",
                  "email": "test@123.com",
                  "resume_id": 1,
                  "address": "亦庄文化园",
                  "name": "大王卡",
                  "school": "联通学院",
                  "city": "北京",
                  "org": "中国移动",
                  "position_name": "java开发",
                  "position_id": 5312625,
                  "mobile": "18812312345",
                  "work_years": "1"}]
    order = dict(request.POST)['item'][0]
    if order == 'received':
        demo_json[0]['name'] = '你收到我的简历啦！'
        demo_json[1]['name'] = '你收到我的简历啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'notified':
        demo_json[0]['name'] = '我要找你面试啦！'
        demo_json[1]['name'] = '我要找你面试啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'passed':
        demo_json[0]['name'] = '我要入职啦！'
        demo_json[1]['name'] = '我也要入职啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'refused':
        demo_json[0]['name'] = '你拒绝了我！'
        demo_json[1]['name'] = '我也被你拒绝啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'filtered':
        return JsonResponse(demo_json, safe=False)


def get_position(request):
    position_demo = [{
        "position_id": "10086",
        "position_name": "Python开发",
        "city": "北京",
        "position_type": "全栈、爬虫、数据分析",
        "min_salary": "8k",
        "max_salary": "10k",
        "work_exp": "1-3年",
        "edu_exp": "本科及以上",
        "post_date": "2018-11-18 14:44:44"
    },
        {
            "position_id": "10086",
            "position_name": "Java开发",
            "city": "北京",
            "position_type": "全栈、爬虫、数据分析",
            "min_salary": "8k",
            "max_salary": "10k",
            "work_exp": "1-3年",
            "edu_exp": "本科及以上",
            "post_date": "2018-11-18 14:44:44"
        }
    ]
    order = dict(request.POST)['item'][0]
    if order == 'valid':
        position_demo[0]['position_name'] = '我是有效职位！'
        position_demo[1]['position_name'] = '我也是有效职位！'
        return JsonResponse(position_demo, safe=False)
    elif order == 'invalid':
        position_demo[0]['position_name'] = 'Oh！我下线了~~！'
        position_demo[1]['position_name'] = '~~！'
        return JsonResponse(position_demo, safe=False)


def get_html(request):
    """
    根据请求返回对应的部分页面
    :param request:
    :return:
    """
    order = dict(request.POST)['html'][0]
    html_dict = {
        'div_resume': 'resume_div/div_resume_content.html',
        'div_position': 'position_div/div_position_content.html',
        'create': 'create_div/create.html',
        'create_success': 'create_div/create_success.html',
        'spss':'data_spss/qiye.html',
    }

    return render(request, html_dict[order])


def org_view(request, item):
    # print(item)
    user = request.user
    if item in ['resumes', 'positions', 'create', 'create_success', 'spss']:
        return render(request, 'org_view.html', locals())
    else:
        return HttpResponse('404!!!')


def test_eacharts(request):
    return render(request, 'data_spss/qiye.html')
