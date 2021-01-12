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

    # 供应商列表查询
    supplier_list='/base-library/service/api/library/supplierPage'
    # 供应商黑名单列表查询
    Supplier_blacklist='/base-library/service/api/library/supplierBlackPage'
    # 供应商审核列表查询
    Supplier_audit='/base-library/service/api/library/supplierPageAudit'
    # 查看单一供应商信息
    single_supplier='/base-library/service/api/library/findSupplierInfoById?'
