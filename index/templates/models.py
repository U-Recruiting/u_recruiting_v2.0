from django.db import models
from user.models import MyUser
# Create your models here.


class UserInfo(models.Model):
    avatar = models.CharField('头像', max_length=20, default=None, null=True)
    name = models.CharField('用户名', max_length=50, default=None, null=True)
    birthday = models.DateTimeField('出生日期',null=True)
    sex = models.CharField('性别', max_length=10, default=None,null=True)
    education = models.CharField('学历', max_length=20, default=None, null=True)
    work_years = models.CharField('工作年数', max_length=30,default=None,null=True)
    status = models.CharField('目前状态', max_length=100, default=None, null=True)
    city = models.CharField('城市', max_length=20, default=None,null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class WorkExp(models.Model):
    company = models.CharField('公司', max_length=50, default=None,null=True)
    tag = models.CharField('行业标签', max_length=20, default=None,null=True)
    department = models.CharField('部门', max_length=50, default=None,null=True)
    type = models.CharField('职位类型', max_length=50, default=None,null=True)
    position_name = models.CharField('职位名字', max_length=50, default=None,null=True)
    start_date = models.DateTimeField('起始时间',null=True)
    end_date = models.DateTimeField('终止时间',null=True)
    skill = models.CharField('技能', max_length=20, default=None,null=True)
    description = models.CharField('工作描述', max_length=500, default=None,null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class ProjectExp(models.Model):
    name = models.CharField('项目名称', max_length=50, default=None,null=True)
    position_name = models.CharField('职位名字', max_length=50, default=None,null=True)
    start_date = models.DateTimeField('起始时间',null=True)
    end_date = models.DateTimeField('终止时间',null=True)
    url = models.CharField('项目链接', max_length=100, default=None, null=True)
    description = models.CharField('项目描述', max_length=500, default=None, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class EducationExp(models.Model):
    school = models.CharField('学校', max_length=50, default=None, null=True)
    start_date = models.DateTimeField('起始时间', null=True)
    end_date = models.DateTimeField('终止时间', null=True)
    education = models.DateTimeField('学历', max_length=50, default=None, null=True) ##待改成char
    subject = models.CharField('专业', max_length=50, default=None, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class HuntingIntent(models.Model):
    position = models.CharField('求职意向', max_length=50, default=None, null=True)
    position_type = models.CharField('职位类型', max_length=20, default=None, null=True)
    city = models.CharField('期望城市', max_length=50, default=None, null=True)
    satrt_salary = models.CharField('期望起始薪资', max_length=20, default=None, null=True)
    end_salary = models.CharField('期望最高薪资', max_length=20, default=None, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


# class SelfProduct(models.Model):
#     url = models.CharField('作品链接', max_length=50, default=None, null=True)
#     desc = models.CharField('作品描述', max_length=500, default=None, null=True)
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class Resume(models.Model):
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE, default=None)
    work_exp = models.ForeignKey(WorkExp, on_delete=models.CASCADE, default=None)
    project_exp = models.ForeignKey(ProjectExp, on_delete=models.CASCADE, default=None)
    edu_exp = models.ForeignKey(EducationExp, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class OrgInfo(models.Model):

    name = models.CharField('公司名称', max_length=20, default=None, null=True)
    avatar = models.CharField('公司图标', max_length=50,default=None, null=True)
    type = models.CharField('公司类型', max_length=20, default=None, null=True)
    phase = models.CharField('公司所在阶段', max_length=50, default=None, null=True) #A轮
    desc = models.CharField('公司描述', max_length=500, default=None, null=True)
    scale = models.CharField('公司人数',max_length=50, null=True)
    url = models.CharField('公司网站', max_length=20, default=None,null=True)
    phone = models.CharField('联系方式', max_length=20, default=None,null=True)
    city = models.CharField('城市', max_length=20, default=None,null=True)
    email = models.EmailField('公司邮箱',null=True)
    tags = models.CharField('公司标签', max_length=200, default=None,null=True) #绩效奖金 通讯津贴...
    createTime = models.DateTimeField(default=None,null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class PositionInfo(models.Model):
    type = models.CharField('岗位类型', max_length=20, null=True)
    name = models.CharField('职位名称', max_length=20, null=True)
    department = models.CharField('所属部门', max_length=20, null=True)
    job_catagory = models.CharField('工作性质', max_length=20, null=True) #全职，兼职，实习
    start_salary = models.CharField('起始薪资', max_length=20, null=True)
    end_salary = models.CharField('最高薪资', max_length=20, null=True)
    city = models.CharField('工作城市', max_length=20, null=True)

    distinct = models.CharField('区/县', max_length=20, default=None, null=True)

    address = models.CharField('工作地址', max_length=100, null=True)
    work_exp = models.CharField('工作经验', max_length=20, null=True)
    edu_exp = models.CharField('学历要求', max_length=20, null=True)

    tags = models.CharField('职位标签', max_length=200, default=None,null=True)

    desc = models.CharField('职位描述', max_length=400, null=True)

    positionAdvantage = models.CharField('职位诱惑', max_length=200, default=None,null=True)
    subwayline = models.CharField('地铁线', max_length=20, default=None,null=True)
    linestaion = models.CharField('地铁线路', max_length=200, default=None,null=True)
    create_datetime = models.DateTimeField('创建时间',default=None,null=True)

    org = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, default=None) #
    resume = models.ManyToManyField(Resume)


class Collection(models.Model):
    position = models.ForeignKey(PositionInfo, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)


class Dynamic_Position(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    dynamic_search = models.IntegerField('搜索次数', null=True)
    position_info = models.ForeignKey(PositionInfo, on_delete=models.CASCADE, default=None)


class Dynamic_Org(models.Model):
    dynamic_id = models.AutoField('序号', primary_key=True)
    dynamic_search = models.IntegerField('搜索次数', null=True)
    org_info = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, default=None)




class PositionResumeStatus(models.Model):
    position = models.ForeignKey(PositionInfo, on_delete=models.CASCADE,default='')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE,default='')
    status = models.CharField('状态', max_length=20, default=None, null=True)


class Province(models.Model):
    province_code = models.CharField('省份代码', max_length=30, default=None, null=True)
    province_name = models.CharField('省份名称', max_length=50, default=None, null=True)


class City(models.Model):
    city_code = models.CharField('城市代码', max_length=30, default=None, null=True)
    city_name = models.CharField('城市名称', max_length=50, default=None, null=True)
    province_code = models.CharField('省份代码', max_length=30, default=None, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='所在省份')



class Distinct(models.Model):
    distinct_code = models.CharField('区代码', max_length=30, default=None, null=True)
    distinct_name = models.CharField('区名称', max_length=50, default=None, null=True)
    city_code = models.CharField('城市名称', max_length=50, default=None, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='所属城市')


class Job_Label1(models.Model):
    id = models.AutoField('一级标签', primary_key=True)
    name = models.CharField('一级标签名称', max_length=20, default=None, null=True)


class Job_Label2(models.Model):
    id = models.AutoField('二级标签', primary_key=True)
    name = models.CharField('二级标签名称', max_length=20, default=None, null=True)
    parent = models.ForeignKey(Job_Label1, on_delete=models.CASCADE,verbose_name='父标签ID', default=None)


class Job_Label3(models.Model):
    id = models.AutoField('三级标签', primary_key=True)
    name = models.CharField('三级标签名称', max_length=20, default=None, null=True)
    parent = models.ForeignKey(Job_Label2, on_delete=models.CASCADE,verbose_name='父标签ID', default=None)



