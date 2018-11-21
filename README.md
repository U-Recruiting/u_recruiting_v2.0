
#### 后台:
+ 1-user 
    + 用户注册登录
        - 完成,待优化   
+ 2-index 
    + 首页
        - 完成，待优化
+ 3-search 
    + 查询页，根据条件显示岗位信息简介
        - 完成，待优化
+ 4-position 
    + 岗位信息详情页,显示岗位详细信息, 包括岗位所属公司, 在此界面用户投递简历,收藏简历
        - 完成，待优化
    + 企业发布岗位信息
    
+ 5-shoot 
    + 处理投递简历后台流程
        - 完成,待优化
+ 6-mycenter
    + 投递箱
        - 完成,待优化
    + 处理收藏岗位信息后台流程
        - 完成, 待优化
+ 7-org 
    + 企业完善信息,home页
    + 筛选简历
    + 发布职位
+ 8-resume
    + 用户编辑简历


 ### 2018-11-16
 1.调整目录结构
    将原来org里面的内容全部移到了org_auth 
    将原来org_index内容全部移动到了org下面
 2.完成了简历投递，企业查看收到简历情况,并对收到简历进行操作
 
 ### 2018-11-17 01:10:00
 1. 修改register.html 添加jquery
 2。 配置手机发送验证码功能,在user.utils中
 
 123456 :pbkdf2_sha256$120000$StpGvQfO4vjm$yZ39kU/ejql4woM8dhRh1jypOoYoe/zzcgTF2EO2hw4=
 file: enctype="multipart/form-data"
 
 
5339024