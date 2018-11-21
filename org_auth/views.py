from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from PIL import Image
from index.models import PositionInfo, OrgInfo
import os
import json
from django.conf import settings
from user.models import MyUser

# Create your views here.


# @login_required(login_url='/user/login')
def home(request):
    id = 1537
    return render(request, 'myhome.html', locals())


def register01(request):
    user = request.user
    if request.method == 'POST':
        url = request.POST.get('main_page', '')
        name = request.POST.get('company_name', '')
        company_license = request.FILES.get('pic', '')
        orginfo = OrgInfo(url=url, name=name, user_id=user.id)
        orginfo.save()
        licese_path = os.path.join(settings.BASE_DIR, 'static/org_license/' + str(orginfo.id) + '.jpg')
        Image.open(company_license).save(licese_path)
        OrgInfo.objects.filter(user_id=user.id).update(lincese = licese_path)
        return redirect('/org_auth/register02')
    return render(request, 'register01.html', locals())


def register02(request):
    return render(request, 'register02.html')


def complete_orginfo(request):
    user = request.user

    if request.method == 'POST':

        print(request.FILES)
        print(request.POST)

        company_name = request.POST.get('company_name', '')
        logo = request.FILES.get('pic', '')
        city = request.POST.get('company_city', '')
        type = request.POST.get('select_industry_hidden', '')
        scale = request.POST.get('select_scale_hidden', '')
        tages = request.POST.get('labels', '')
        desc = request.POST.get('desc', '')
        createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        orginfo = user.orginfo_set.all().first()

        logo_path = os.path.join(settings.BASE_DIR, 'static/org_logo/' + str(orginfo.id) + '.jpg')
        Image.open(logo).save(logo_path)
        OrgInfo.objects.filter(user_id=user.id).update(name=company_name, avatar=logo_path,
                                                       type=type,  desc=desc, scale=scale,
                                                         city=city,
                                                        tags=tages,createTime=createTime)
        user.complete = 'yes'
        user.save()

        return HttpResponse(json.dumps({'url':'/org/my_org/create'}, ensure_ascii=False), content_type="application/json,charset=utf-8")

    return render(request, 'home.html', locals())


def home01(request):
    return render(request, 'home.html') ##完善公司信息
def myhome(request):
    user = request.user
    # user = MyUser.objects.get(id=198)
    if request.method == "GET":
        # name = OrgInfo.objects.filter(user_id =198).values()
        org_ifo = user.orginfo_set.all().first()
        print(org_ifo.id)
        org_ifo.tags = org_ifo.tags.split(",")
        return render(request, 'myhome.html', locals())

    if request.method == "POST":
        org_info = user.orginfo_set.all().first()
        logo = request.FILES.get('pic', '')
        city = request.POST.get('company_city', '')
        type = request.POST.get('select_industry_hidden', '')
        scale = request.POST.get('companySize', '')
        desc = request.POST.get('company_desc', '')
        if str(request.POST.get("label")).strip('') not in ['',' ']:
            tags = org_info.tags +','+ request.POST.get("label",'')
            print(tags)
        else:
            tags = org_info.tags
            # OrgInfo.objects.filter(user_id = user).update(logo = logo,citi = city,type = type,scale= scale,desc=desc)

        logo_path = os.path.join(settings.BASE_DIR, 'static/org_logo/' + str(org_info.id) + '.jpg')
            # Image.open(logo).save(logo_path)
        OrgInfo.objects.filter(user_id=user.id).update(avatar=logo_path,
                                                           type=type, desc=desc, scale=scale,
                                                           city=city,tags = tags
                                                           )
            # user.complete = 'yes'
        user.save()

        org_ifo = user.orginfo_set.all().first()
        org_ifo.tags = org_ifo.tags.split(",")
        return render(request, "myhome.html",locals())