# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import main_init
from models.db_con import Db_Connection
import unittest,json,random,time
from url_api.ymsp.ymsp_api import Oalogin

config = main_init.Init_Config('172.17.52.68','ym_core_library','root','123456')
mysql_db=Db_Connection(config.msqlserver,config.msqdb,config.msqusername,config.msqpassword)
ymsp=Oalogin()

class Mycount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   #类的前置，执行这个类一开始要执行的东西
        pass
    @classmethod
    def tearDownClass(self): #类的后置，执行完整个类之后，要执行的东西
        pass

    def setUp(self):  #用例的前置，执行每条用例前要执行的东西
        pass
    def tearDown(self):  #用例的后置，执行每条用例后要执行的东西
        pass
    def test01(self):
        u"""供应商库列表接口显示所属单位字段"""
        res_list=ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        for i in res_list:
            self.assertIn('belongCompany',i)

    def test02(self):
        u"""查看具每个供应商接口显示字段“所属单位”"""
        res_list=ymsp.select_single_supplier()
        for i in res_list:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
    def test03(self):
        u"""新增化工集团下的供应商或非化工集团下的供应商保存接口是否包含所属单位字段"""
        res_list=ymsp.supplier_increase_preservation()
        for i in res_list:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        self.assertIn('OTHER', json.loads(res_list[0].text)['data']['belongCompany'])
        self.assertIn('HG', json.loads(res_list[1].text)['data']['belongCompany'])
    def test04(self):
        u"""新增化工集团下的供应商或非化工集团下的供应商提交接口是否包含所属单位字段"""
        res_list_HG=ymsp.supplier_increase_submit_HG()
        res_list_OTHER = ymsp.supplier_increase_submit_OTHER()
        for i in res_list_HG:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        for i in res_list_OTHER:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        self.assertIn('OTHER', json.loads(res_list_OTHER[0].text)['data']['belongCompany'])
        self.assertIn('HG', json.loads(res_list_HG[0].text)['data']['belongCompany'])


    def test05(self):
        u"""修改化工集团下的供应商或非化工集团下的供应商保存接口是否包含所属单位字段"""
        res_list=ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        HG=[]
        OTHER=[]
        for i in res_list:
            if i['belongCompany'] == 'HG' and i['auditStatus'] == '0':
                HG.append(i['id'])
            if i['auditStatus'] == '0' and i['belongCompany'] == 'OTHER':
                OTHER.append(i['id'])
        update_list = ymsp.supplier_update_preservation(random.choice(OTHER),random.choice(HG))
        for i in update_list:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        self.assertIn('OTHER', json.loads(update_list[0].text)['data']['belongCompany'])
        self.assertIn('HG', json.loads(update_list[1].text)['data']['belongCompany'])

    def test06(self):
        u"""验证非化工集团下的供应商对化工集团下的供应商进行修改保存操作"""
        res_list = ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        HG = []
        OTHER = []
        for i in res_list:
            if i['belongCompany'] == 'HG' and i['auditStatus'] == '0':
                HG.append(i['id'])
            if i['auditStatus'] == '0' and i['belongCompany'] == 'OTHER':
                OTHER.append(i['id'])
        update_list = ymsp.supplier_update_preservation(random.choice(HG), random.choice(OTHER))

        for i in update_list:
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        self.assertIn('OTHER', json.loads(update_list[0].text)['data']['belongCompany'])
        self.assertIn('HG', json.loads(update_list[1].text)['data']['belongCompany'])

    def test07(self):
        u"""化工集团下供应商修改提交接口包含所属单位字段"""
        res_list = ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        HG = []
        for i in res_list:
            if i['belongCompany'] == 'HG' and i['auditStatus'] == '0':
                HG.append(i['id'])

        update_list = ymsp.supplier_update_submit_HG(random.choice(HG))

        for i in update_list:
            print(i.text)
            self.assertIn('belongCompany',json.loads(i.text)['data'])
        self.assertIn('HG', json.loads(update_list[0].text)['data']['belongCompany'])
        self.assertIn('2', json.loads(update_list[0].text)['data']['auditStatus'])


    def test08(self):
        u"""非化工集团下供应商修改提交接口包含所属单位字段"""
        res_list = ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        OTHER = []
        for i in res_list:
            if i['belongCompany'] == 'OTHER' and i['auditStatus'] == '0':
                OTHER.append(i['id'])
        update_list = ymsp.supplier_update_submit_OTHER(random.choice(OTHER))

        for i in update_list:
            self.assertIn('belongCompany', json.loads(i.text)['data'])
        self.assertIn('OTHER', json.loads(update_list[0].text)['data']['belongCompany'])
        self.assertIn('2', json.loads(update_list[0].text)['data']['auditStatus'])

    def test09(self):
        u"""化工集团下的供应商审核列表显示只显示化工集团正在审核中的供应商"""
        res_list = ymsp.select_supplier_list('ba50a20028a5405da331a08297fe3de2')[1]['data']
        sql="SELECT * from supplier_lib WHERE belong_company='HG' and audit_status=2"
        result=mysql_db.all(sql)
        project_name=[]
        for i in result:
            if len(result) == 0:
                self.assertEqual(0, 0)
            else:
                project_name.append(i[3])
        for i in res_list:
            self.assertIn(i['supplierName'],project_name)
            self.assertEqual('HG',i['belongCompany'])

    #
    # def test09(self):
    #     u"""化工集团下的账号对供应商黑名单进行移除黑名单操作"""
    #     res_list = ymsp.select_supplier_list('ba50a20028a5405da331a08297fe3de2')
    #     id_list=[]
    #     for i in res_list[0]['data']:
    #             if i['auditStatus'] == '2' and i['belongCompany']=='HG':
    #                 id_list.append(i['id'])
    #
    #     # examine=ymsp.examine(random.choice(id_list))
    #     # print(examine[0].text)
    #     time.sleep(6)
    #     examinelist=[]
    #     for j in res_list[0]['data']:
    #             if j['auditStatus'] == '1' and j['belongCompany']=='HG':
    #                 examinelist.append(j['id'])
    #     time.sleep(6)
    #     join_blacklist=ymsp.join_blacklist(random.choice(examinelist))
    #     print(join_blacklist[0].text)
    #     time.sleep(6)
    #     joinlist = []
    #     for a in res_list[2]['data']:
    #         joinlist.append(a['id'])
    #     remove_blacklist=ymsp.remove_blacklist(random.choice(joinlist))
    #     print(remove_blacklist[0].text)
    #     # self.assertEqual("ok",json.loads(examine[0].text)['message'])
    #     self.assertEqual("ok", json.loads(join_blacklist[0].text)['message'])
    #     self.assertEqual("ok", json.loads(remove_blacklist[0].text)['message'])

    #
    # def test10(self):
    #     u"""非化工集团下的账号对供应商黑名单进行移除黑名单操作"""
    #     res_list=ymsp.select_single_expert_extraction()
    #     id_list=[]
    #     for i in res_list:
    #         if json.loads(i.text)['data']['applyStatus'] == 'draft':
    #             id_list.append(json.loads(i.text)['data']['id'])
    #     list = ymsp.update_expert_submit(random.choice(id_list))
    #     params=json.loads(list[0].text)['data']['id']
    #     sql="SELECT * from expert_apply WHERE id=%s"
    #     result=mysql_db.all_chall(sql,params)
    #     self.assertEqual(json.loads(list[0].text)['data']['applyStatus'],result[0][14])
    def test10(self):
        u"""查看非化工集团下供应商黑名单接口是否包含所属单位字段"""
        res_list = ymsp.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[2]['data']
        for i in res_list:
            self.assertIn('belongCompany',i)

    def test11(self):
        u"""查看化工集团下供应商黑名单接口是否包含所属单位字段"""
        res_list = ymsp.select_supplier_list('ba50a20028a5405da331a08297fe3de2')[2]['data']
        for i in res_list:
            self.assertIn('belongCompany',i)

    def test12(self):
        u"""查看化工集团下供应商黑名单接口是否包含所属单位字段"""
        res_list = ymsp.select_supplier_list('ba50a20028a5405da331a08297fe3de2')[2]['data']
        for i in res_list:
            self.assertIn('belongCompany',i)

    def test13(self):
        u"""备案计划、项目备案、备案项目统计、中标通知书备案时,化工集团下的账号显示全部已经审核通过，且未冻结、未拉黑的供应商"""
        res_list = ymsp.project_supplierPage('ymhg','123456')

        project_name=[]
        sql="SELECT * from supplier_lib WHERE supplier_class!='D' and audit_status=1 and status='use'"
        result=mysql_db.all(sql)
        for j in result:
            project_name.append(j[3])
        self.assertEqual(json.loads(res_list[0].text)['total'],len(result))
        for i in json.loads(res_list[0].text)['data']:
            self.assertIn(i['supplierName'],project_name)

    def test14(self):
        u"""备案计划、项目备案、备案项目统计、中标通知书备案时,非化工集团下的账号显示全部已经审核通过，且未冻结、未拉黑的供应商"""
        res_list = ymsp.project_supplierPage('apisxy','123456')
        project_name=[]
        sql="SELECT * from supplier_lib WHERE belong_company='OTHER' and supplier_class!='D' and audit_status=1 and status='use'"
        result=mysql_db.all(sql)
        for j in result:
            project_name.append(j[3])
        for i in json.loads(res_list[0].text)['data']:
            self.assertIn(i['supplierName'],project_name)
        self.assertEqual(json.loads(res_list[0].text)['total'], len(result))


