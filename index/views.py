from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Job_Label1,Dynamic_Position,Dynamic_Org,PositionInfo
# Create your views here.
#
# from docx import Document

# @login_required(login_url='/user/login')
def index(request):

    #标签1，2，3

    lables = Job_Label1.objects.all()[:4]
    lables_4 =[]
    for index in range(4):
         lables_4.append(lables[index])
    hot_position_3 = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()[:3]
    hot_position_6 = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()[3:6]

    hot_company = Dynamic_Org.objects.select_related('org_info').order_by('-dynamic_search').all()[:10]


    latest_3 = PositionInfo.objects.order_by('-create_datetime').all()[:3]
    latest_6 = PositionInfo.objects.order_by('-create_datetime').all()[3:6]

    user = request.user #可能为匿名用户

    if user.is_active: #如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False
    return render(request, 'index.html', locals())

#返回关于我们界面
def aboutus(request):
    return render(request,'about.html')





