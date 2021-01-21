# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong

class api_config(object):
    """接口配置信息"""
    login_url = 'https://caigou.jcebid.com'

    # 请求头
    headers={'Content-Type': 'application/json',
             'User-Agent':'Mozilla/5.0 (Android; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}

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
    #备案计划查看
    Record_plan_view='/service/api/projectRecordPlan/pageForView?'
    # 项目备案查看
    Project_record_view = '/service/api/project/pageForView?'
    # 控制价备案查看
    Controlprice_record_view='/service/api/biddingControlPriceRecord/pageForView'
    # 中标通知书备案查看
    acceptance_record_view = '/service/api/winBiddingNotificationFiling/pageForView'

    # 待办事项  已办事项
    to_do_list='/service/api/approval/workflow/task'


class zts_office(object):
    # 新增机构
    org_add='/api/org/add'
    # 修改机构信息
    org_saveChange = '/api/org/organ/saveChange'
    # 添加子机构
    org_sub_add = '/saas_platform/api/org/sub/organ/add'
    # 删除子机构
    org_sub = '/saas_platform/api/org/sub/organ'
    # 机构组织机构图
    orgAndDeptTree='/saas_platform/api/org/sub/orgAndDeptTree'
    # 机构组织架构图机构详细信息构图
    org_organ='/saas_platform/api/org/sub/organ'
    # 新增部门
    department_add='/saas_platform/api/org/department'
    # 删除部门
    department_del = '/saas_platform/api/org/department'
    # 更新部门信息
    department_sub = '/saas_platform/api/org/department'
    # 查询角色
    role_sele='/saas_platform/api/org/role/page'
    # 新增角色
    role_add='/saas_platform/api/org/role/add'
    # 更新角色
    role_sub = '/saas_platform/api/org/role'
    # 删除角色
    role_del = '/saas_platform/api/org/role'
    # 查询用户
    user_sele = '/saas_platform/api/org/user/findPage2'
    # 新增用户
    user_add = '/saas_platform/api/org/user/add'
    # 更新用户信息
    user_sub = '/saas_platform/api/org/user/update'
    # 移除部门用户
    user_del = '/saas_platform/api/org/user/deleteById'