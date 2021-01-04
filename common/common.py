# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong

class api_config(object):
    """接口配置信息"""
    login_url = 'https://caigou.jcebid.com'

    # 请求头
    headers={'Content-Type': 'application/json'}

    # 登陆接口
    login='/saas//api/org/login'

    biddinglogin='http://zts.kb.jcebid.com/ajaxLogin'


class ymjt(object):

    url='http://ymjt.jcebid.com'
    # 版本号
    version='/servicezh/startup/version?_=1609309805312'
    # 新增项目
    insert_project='/servicezh/api/project/add'
    # 查看项目
    select_project='/servicezh/api/project/list'
    # 删除项目
    delete_project='/servicezh/api/project/remove'
    # 查询招标项目
    select_Bidding_project='/servicezh/api/instance/list'

    # 查看开标项目
    select_Bidding='http://zts.kb.jcebid.com/tender/tenderList?1609732637764&pageNum=1&pageSize=10&_=1609732637582'


    username='http://zts.ztb.jcebid.com/integrated_management_system_api/api/user/list?pageNum=1&pageSize=10&_=1609752126293'