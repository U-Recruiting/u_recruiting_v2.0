from django.shortcuts import render, redirect
from django.http import HttpResponse
from index.models import *
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import os
from . import utils


# Create your views here.
#add添加测试
# def myresume_test(request):
#     return render(request, "myresume.html")


# @login_required
def my_resume(request):
    user = request.user  # 可能为匿名用户
    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False
    #

    current_user = user

    user_info = current_user.userinfo_set.all().first()

    work_exp = current_user.workexp_set.all().first()

    project_exp = current_user.projectexp_set.all().first()

    edu_exp = current_user.educationexp_set.all().first()

    hunting_intent = current_user.huntingintent_set.all().first()
    # hunting_salary = hunting_intent.satrt_salary+'-'+hunting_intent.end_salary

    resume = current_user.resume_set.all().first()

    city = hunting_intent.city
    type = hunting_intent.position_type
    position = hunting_intent.position
    if hunting_intent.satrt_salary:
        start_salary = int(hunting_intent.satrt_salary[:-1])
    else:
        start_salary = 1000000000
    if hunting_intent.end_salary:
        end_salary = int(hunting_intent.end_salary[:-1])
    else:
        end_salary = 0

    relate_positions = PositionInfo.objects.filter(name__icontains=position)
    utils.guess_your_love(relate_positions, city, type, start_salary, end_salary)
    relate_positions = sorted(relate_positions, key=lambda relate_positions: relate_positions.point)[::-1][:4]

    return render(request, 'myresume.html', locals())


def edit_userinfo(request):
    user = request.user
    userinfo = user.userinfo_set.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        sex = request.POST.get('sex', '')
        education = request.POST.get('education', '')
        work_years = request.POST.get('work_years', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')
        status = request.POST.get('status', '')
        city = request.POST.get('city', '')
        if name:
            userinfo.update(name=name)
        if sex:
            userinfo.update(sex=sex)
        if education:
            userinfo.update(education=education)
        if work_years:
            userinfo.update(work_years=work_years)
        if email:
            request.POST.get('email', '')
        if mobile:
            user.mobile = mobile
        if status:
            request.POST.get('status', )
        if city:
            userinfo.update(city=city)
        user.save()

        resp = {}
        resp['name'] = userinfo[0].name
        resp['sex'] = userinfo[0].sex
        resp['education'] = userinfo[0].education
        resp['work_years'] = userinfo[0].work_years
        resp['email'] = userinfo[0].email
        resp['mobile'] = userinfo[0].mobile
        resp['status'] = userinfo[0].status
        resp['city'] = userinfo[0].city

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_workexp(request):
    user = request.user
    work_exp = user.workexp_set.all()
    if request.method == 'POST':

        company = request.POST.get('company', '')
        tag = request.POST.get('tag', '')
        department = request.POST.get('department', '')
        type = request.POST.get('type', '')
        position_name = request.POST.get('position_name', '')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        skill = request.POST.get('skill', '')
        description = request.POST.get('description', '')

        if company:
            work_exp.update(name=company)
        if tag:
            work_exp.update(tag=tag)
        if department:
            work_exp.update(name=department)
        if type:
            work_exp.update(department=type)
        if position_name:
            work_exp.update(position_name=position_name)
        if start_date:
            work_exp.update(start_date=start_date)
        if end_date:
            work_exp.update(end_date=end_date)
        if skill:
            work_exp.update(skill=skill)
        if description:
            work_exp.update(description=description)

        resp = {}
        resp['company'] = work_exp[0].company
        resp['tag'] = work_exp[0].tag
        resp['department'] = work_exp[0].department
        resp['type'] = work_exp[0].type
        resp['position_name'] = work_exp[0].position_name
        resp['start_date'] = work_exp[0].start_date
        resp['end_date'] = work_exp[0].end_date
        resp['skill'] = work_exp[0].skill
        resp['description'] = work_exp[0].description

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_projectexp(request):
    user = request.user
    project_exp = user.projectexp_set.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        position_name = request.POST.get('position_name')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        url = request.POST.get('url', '')
        description = request.POST.get('description', '')

        if name:
            project_exp.update(name=name)
        if start_date:
            project_exp.update(start_date=start_date)
        if end_date:
            project_exp.update(end_date=end_date)
        if url:
            project_exp.update(url=url)
        if position_name:
            project_exp.update(position_name=position_name)
        if description:
            project_exp.update(description=description)

        resp = {}
        resp['name'] = project_exp[0].name
        resp['start_date'] = project_exp[0].start_date
        resp['end_date'] = project_exp[0].end_date
        resp['url'] = project_exp[0].url
        resp['position_name'] = project_exp[0].position_name
        resp['description'] = project_exp[0].description

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_educationexp(request):
    user = request.user
    education_exp = user.educationexp_set.all()

    if request.method == 'POST':
        school = request.POST.get('school', '')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        education = request.POST.get('education', '')  ##待改成char
        subject = request.POST.get('subject', '')

        if school:
            education_exp.update(school=school)
        if start_date:
            education_exp.update(start_date=start_date)
        if end_date:
            education_exp.update(end_date=end_date)
        if education:
            education_exp.update(education=education)
        if subject:
            subject.update(subject=subject)

        resp = {}
        resp['school'] = education_exp[0].school
        resp['start_date'] = education_exp[0].start_date
        resp['end_date'] = education_exp[0].end_date
        resp['education'] = education_exp[0].education
        resp['subject'] = education_exp[0].subject

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_huntingintent(request):
    user = request.user
    huntingintent_exp = user.huntingintent_set.all()

    if request.method == 'POST':
        city = request.POST.get('expectCity', '')
        position = request.POST.get('expectPosition', '')
        position_type = request.POST.get('type', '')
        salary = request.POST.get('expectSalary', '')

        if position:
            huntingintent_exp.update(position=position)
        if position_type:
            huntingintent_exp.update(position_type=position)
        if city:
            huntingintent_exp.update(city=city)
        if salary:
            split_salary = salary.split('-')
            if len(split_salary) == 2:
                huntingintent_exp.update(satrt_salary=split_salary[0])
                huntingintent_exp.update(end_salary=split_salary[1])
            else:
                huntingintent_exp.update(satrt_salary='')
                huntingintent_exp.update(end_salary=split_salary[0])
        # resp = {}
        # resp['position'] = huntingintent_exp[0].position
        # resp['position_type'] = huntingintent_exp[0].position_type
        # resp['city'] = huntingintent_exp[0].city
        # start_salary = huntingintent_exp[0].satrt_salary
        # end_salary = huntingintent_exp[0].end_salary
        # if start_salary:
        #     resp['salary'] = start_salary+'-'+end_salary
        # else:
        #     resp['salary'] = end_salary
        # return redirect('/resume/myresume')
    return redirect('/resume/myresume')


def edit_avatar(request):
    user = request.user
    userinfo = user.userinfo_set.all()
    if request.method == 'POST':
        avatar = request.FILES.get('avatar', '')
        path = os.path.join(settings.BASE_DIR, 'resume/static/avatar/'+str(user.id)+'.jpg')
        img = Image.open(avatar)
        img.save(path)
    img_path = 'avadar/'+str(user.id)+'.jpg'

    return render(request, 'edit_avatar.html', locals())

# 我收藏的职位
def mycollection(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    hunting_position = user.huntingintent_set.all().first()

    city = hunting_position.city
    type = hunting_position.position_type
    position = hunting_position.position
    if hunting_position.satrt_salary:
        start_salary = int(hunting_position.satrt_salary[:-1])
    else:
        start_salary = 1000000000
    if hunting_position.end_salary:
        end_salary = int(hunting_position.end_salary[:-1])
    else:
        end_salary = 0

    relate_positions = PositionInfo.objects.filter(name__icontains=position)
    utils.guess_your_love(relate_positions, city, type, start_salary, end_salary)
    relate_positions = sorted(relate_positions, key=lambda relate_positions: relate_positions.point)[::-1][:4]

    return  render(request, 'myjob_collection.html', locals())

# 我投递的职位
def mydelivery(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    return  render(request,'myjob_delivery.html',locals())


# 我订阅的职位
def mysubscribe(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    return  render(request,'myjob_subscribe.html',locals())

# 我的推荐
def myrecommand(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False

    hunting_position = user.huntingintent_set.all().first()

    city = hunting_position.city
    type = hunting_position.position_type
    position = hunting_position.position
    if hunting_position.satrt_salary:
        start_salary = int(hunting_position.satrt_salary[:-1])
    else:
        start_salary = 1000000000
    if hunting_position.end_salary:
        end_salary = int(hunting_position.end_salary[:-1])
    else:
        end_salary = 0

    relate_positions = PositionInfo.objects.filter(name__icontains=position)
    utils.guess_your_love(relate_positions, city, type, start_salary, end_salary)
    relate_positions = sorted(relate_positions, key=lambda relate_positions: relate_positions.point)[::-1]

    return  render(request,'myjob_recommand.html',locals())

#简历预览
def preview(request):
    return render(request,'preview.html')
