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
    ym_url='http://ymsp.jcebid.com'

    # 供应商列表查询
    supplier_list='/base-library/service/api/library/supplierPage'
    # 供应商黑名单列表查询
    Supplier_blacklist='/base-library/service/api/library/supplierBlackPage'
    # 供应商审核列表查询
    Supplier_audit='/base-library/service/api/library/supplierPageAudit'
    # 查看单一供应商信息
    single_supplier='/base-library/service/api/library/findSupplierInfoById?'
    # 新增保存
    preservation='/base-library/service/api/library/addSupplierLocalZanCun'
    # 新增提交
    Supplier_summit = '/base-library/service/api/library/addSupplierLocal'

    # 审核
    examine='/base-library/service/api/library/supplierAddToMDM?'

    # 加入黑名单
    join_blacklist='/base-library/service/api/library/updateSupplierClass'

    # 查看专家抽取列表信息
    expert_extraction_list='/service/api/expert/apply/findPage?'
    # 查看单一专家抽取列表信息
    single_expert_extraction = '/service/api/expert/apply/findInfo?'

    # 新增专家抽取后保存
    expert_extraction_increase='/service/api/expert/apply/add'

    # 修改专家抽取后保存
    expert_extraction_update = '/service/api/expert/apply/update'

    # 项目备案计划查询供应商
    project_supplierPage='/service/api/project/supplierPage?'



