from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from index.models import *
from django.contrib.auth.decorators import login_required
from urllib.parse import unquote
import datetime


def searchView(request):
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
    if request.method == 'GET':

        kword = request.session.get('search_input', '')
        search_input_type = request.session.get('search_input_type', '')
        print('keyword', kword)
        page = request.GET.get('pn', 1)
        city = request.GET.get('city', '')
        distinct = request.GET.get('distinct', '')
        work_exp = request.GET.get('workExpSelectInput', '')
        edu_exp = request.GET.get('eduExpSelectInput', '')
        phase = request.GET.get('phase', '')
        scale = request.GET.get('scaleInput', '')
        type = request.GET.get('domainInput', '')
        domain = request.GET.get('domain', '')
        hot_position = request.GET.get('hot_position')

        if search_input_type == '职位':

            objects = PositionInfo.objects
            if city == '全国' or city=='':
                objects = objects.all()
            else:
                objects = objects.filter(city=city)
            if distinct:
                objects = objects.filter(distinct=distinct)
            if work_exp:
                if work_exp == '应届生':
                    objects = objects.filter(work_exp__icontains='应届')
                elif work_exp == '3年及一下':
                    objects = objects.filter(work_exp__icontains='1')
                elif work_exp == '3-5年':
                    objects = objects.filter(work_exp__icontains='3-5')
                elif work_exp == '5-10年':
                    objects = objects.filter(work_exp__icontains='5-10')
                elif work_exp == '10年以上':
                    objects = objects.filter(work_exp__icontains='5-10')

            if edu_exp:
                objects = objects.filter(edu_exp__icontains=edu_exp)
            if phase:
                objects = objects.filter(phase=phase)
            # if scale:
            #     orginfo = OrgInfo.objects.filter(scale=scale)
            #     objects = objects.filter(org=orginfo).all()
            if type:
                objects = objects.filter(type=type)
            if hot_position:
                hot_positionme = objects.filter(name__icontains=hot_position)

            if kword:
                # Q是SQL语句里的or语法
                position_info = objects.filter(Q(name__icontains=kword) | Q(type__icontains=kword)).all()
            else:
                position_info = objects.order_by('-create_datetime').all()[:500]

            # 分页功能
            paginator = Paginator(position_info, 15)
            try:
                position_list = paginator.page(page)

                for position in position_list:
                    tags = position.org.tags.split(',')
                    position.tags = tags

                    post_time = position.create_datetime

                    now = datetime.datetime.now()
                    timedelta = (now - post_time).days
                    position.timedelta = timedelta


            #
            except PageNotAnInteger:
                position_list = paginator.page(1)
            except EmptyPage:
                position_list = paginator.page(paginator.num_pages)

            position_exist = PositionInfo.objects.filter(name=kword)
            if position_exist:
                position_id = position_exist[0].id
                dynamic_position_info = Dynamic_Position.objects.filter(position_info_id=position_id).first()

                if dynamic_position_info:
                    dynamic_position_info.dynamic_search += 1
                    dynamic_position_info.save()

                else:
                    dynamic = Dynamic_Position(dynamic_search=1, position_info_id=position_id)
                    dynamic.save()
            return render(request, 'searchcomlist2.html', locals())

        if search_input_type == '公司':

            return redirect('/search/company')
        else:
            return render(request,'searchcomlist2.html', locals())

    else:
        # 处理POST请求，并重定向搜索页面。
        request.session['search_input'] = request.POST.get('search_input', '')
        request.session['search_input_type'] = request.POST.get('search_input_type', '')

        return redirect('/search/')


# 公司查询列表页
def companyView(request):
    print('---------------------------------------------------')
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

        kword = request.session.get('search_input', '')
        page = request.GET.get('pn', 1)
        city = request.GET.get('city', '')
        distinct = request.GET.get('distinct', '')
        work_exp = request.GET.get('workExpSelectInput', '')
        edu_exp = request.GET.get('eduExpSelectInput', '')
        phase = request.GET.get('phaseSelectInput', '')
        scale = request.GET.get('scaleInput', '')
        type = request.GET.get('domainInput', '')
        hot_position = request.GET.get('hot_position')


        objects = OrgInfo.objects
        if city == '全国' or city=='':
            objects = objects.all()
        else:
            objects = objects.filter(city=city)
        if distinct:
            objects = objects.filter(distinct=distinct)
        if work_exp:
            objects = objects.filter(work_exp=work_exp)
        if edu_exp:
            objects = objects.filter(edu_exp=edu_exp)
        if phase:
            if phase == '初创型':
                objects = objects.filter(phase__icontains='不需要')
            elif phase == '成长型':
                objects = objects.filter(Q(phase__icontains='A') | Q(phase__icontains='B'))
            elif phase == '成熟型':
                objects = objects.filter(Q(phase__icontains='C') | Q(phase__icontains='D'))
            else:
                objects = objects.filter(phase__icontains='上市')
        if scale:
            orginfo = OrgInfo.objects.filter(scale=scale)
            objects = objects.filter(org=orginfo).all()
        if type:
            objects = objects.filter(domain__icontains=type)
        if hot_position:
            hot_positionme = objects.filter(name__icontains=hot_position)

        if kword:
            # Q是SQL语句里的or语法
            org_info = objects.filter(name__icontains=kword).all()
        else:
            org_info = objects.order_by('-createTime').all()[:200]
        # all_org = OrgInfo.objects.all()

        org_filter = []
        for i in org_info:
            if len(i.name) < 15:
                org_filter.append(i)

        # 分页功能
        paginator = Paginator(org_filter, 16)
        try:
            org_list = paginator.page(page)
            for org in org_list:
                org.positioninfos = org.positioninfo_set.all()[:1]

            for org in org_list:
                tags = org.tags.split(',')[:1]
                org.tags = tags

            # for orginfo in posorg_listition_list:
            #     tags = position.org.tags.split(',')
            #     position.tags = tags
            #
            #     post_time = position.create_datetime
            #
            #     now = datetime.datetime.now()
            #     timedelta = (now - post_time).days
            #     position.timedelta = timedelta

            # position_companys = {}
            # for one_position in  position_list:
            #     org = one_position.org
            #     position_company = {}
            #     position_company['tags'] = org.tags.split(',')
            #     position_companys[one_position.id] = position_company
        #
        except PageNotAnInteger:
            org_list = paginator.page(1)
        except EmptyPage:
            org_list = paginator.page(paginator.num_pages)

        orginfo_exist = OrgInfo.objects.filter(name=kword)
        if orginfo_exist:
            orginfo_id = orginfo_exist[0].id
            dynamic_org_info = Dynamic_Org.objects.filter(org_info_id=orginfo_id).first()

            if dynamic_org_info:
                dynamic_org_info.dynamic_search += 1
                dynamic_org_info.save()

            else:
                dynamic = Dynamic_Org(dynamic_search=1, org_info_id=orginfo_id)
                dynamic.save()
        return render(request, 'companylist.html', locals())
    else:
        # 处理POST请求，并重定向搜索页面。
        request.session['search_input'] = request.POST.get('search_input', '')

        return redirect('/search/company')

        # return render(request,'companydetail.html',locals())


def details(request, org_id):
    # buttin_text = '投递简历'
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        print(user.is_active)
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
            resume = user.resume_set.first()
            # psr = PositionResumeStatus.objects.filter(position_id=position_id, resume_id=resume.id)
            # if psr:
            #     disabled = "disabled"
            #     buttin_text = '已投递'
        else:
            logined = False
    else:
        logined = False
    #
    org_info_detail = OrgInfo.objects.get(id=org_id)

    org_positions = org_info_detail.positioninfo_set.all()

    for position in org_positions:
        post_time = position.create_datetime
        now = datetime.datetime.now()
        timedelta = (now - post_time).days
        position.timedelta = timedelta

    #
    # position_resumed = []
    # resumed = position_info_detail.resume.all()
    # for resume in resumed:
    #     # 每个简历对应的除了查询岗位信息的所以岗位信息
    #     positions = resume.positioninfo_set.exclude(id=position_info_detail.id)
    #     # 所以简历对应岗位信息汇总
    #     position_resumed += positions
    # position_resumed = position_resumed[:2]
    #
    #
    # post_time = position_info_detail.create_datetime
    #
    # desc = position_info_detail.desc
    # desc_list = desc.split('==1、')
    #
    # if len(desc_list) >=1:
    #     duty = desc_list[0].split('==')
    # if len(desc_list)>=2:
    #     require = desc_list[1].split('==')
    #     if len(require)>0:
    #         require[0] = '1、'+require[0]
    #
    # if len(desc_list) >=3:
    #     other = desc_list[2].split('==')
    #     if len(other)>0:
    #         other[0] = '1、'+other[0]
    #
    #
    # now = datetime.datetime.now()
    # timedelta = (now - post_time).days
    tags = org_info_detail.tags.split(',')[:4]
    org_info_detail.tags = tags
    print(locals())
    return render(request, 'companydetail.html', locals())


# 职位详情页
def jobinfoView(request):
    # user = request.user
    # if user.is_active:
    #     logined = True
    #     user_real_name = user.userinfo_set.all().first().name
    # else:
    #     logined = False
    return render(request, 'jobinfo.html', locals())


# 查看更多
def searchmoreView(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    hot_position = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()
    latest = PositionInfo.objects.order_by('-create_datetime').all()
    return render(request, 'searchcomlist.html', locals())
