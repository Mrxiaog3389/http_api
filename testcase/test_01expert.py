# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import main_init
from models.db_con import Db_Connection
import unittest,json,random
from url_api.ymsp.ymsp_api import Oalogin

config = main_init.Init_Config('172.17.52.68','ym_approval_platform','root','123456')
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
        u"""新增专家抽取信息而保存接口,评标用时字段为0.5测试"""
        res_list=ymsp.single_expert_preservation('apisxy','123456',0.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])
    def test02(self):
        u"""新增专家抽取信息而保存接口,评标用时字段为1.5测试"""
        res_list=ymsp.single_expert_preservation('apisxy','123456',1.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])
    def test03(self):
        u"""新增专家抽取信息而保存接口,评标用时字段为2.5测试"""
        res_list=ymsp.single_expert_preservation('apisxy','123456',2.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])


    def test04(self):
        u"""新增专家抽取信息而提交接口,评标用时字段为0.5测试"""
        res_list=ymsp.single_expert_submit('apisxy','123456',0.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])
    def test05(self):
        u"""新增专家抽取信息而提交接口,评标用时字段为1.5测试"""
        res_list=ymsp.single_expert_submit('apisxy','123456',1.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])
    def test06(self):
        u"""新增专家抽取信息而提交接口,评标用时字段为2.5测试"""
        res_list=ymsp.single_expert_submit('apisxy','123456',2.5)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])


    def test07(self):
        u"""查看专家抽取信息接口,评标用时字段显示为.5测试"""
        res_list=ymsp.select_single_expert_extraction()
        for i in res_list:
           self.assertIn('.5',str(json.loads(i.text)['data']['evaluateUseTime']))

    def test08(self):
        u"""修改专家抽取信息再保存接口测试"""
        res_list=ymsp.select_single_expert_extraction()
        id_list=[]
        for i in res_list:
            if json.loads(i.text)['data']['applyStatus'] == 'draft':
                id_list.append(json.loads(i.text)['data']['id'])
        list = ymsp.update_expert_preservation(random.choice(id_list))
        params=json.loads(list[0].text)['data']['id']
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertEqual(json.loads(list[0].text)['data']['projectName'],result[0][1])

    def test09(self):
        u"""修改专家抽取信息再提交接口测试"""
        res_list=ymsp.select_single_expert_extraction()
        id_list=[]
        for i in res_list:
            if json.loads(i.text)['data']['applyStatus'] == 'draft':
                id_list.append(json.loads(i.text)['data']['id'])
        list = ymsp.update_expert_submit(random.choice(id_list))
        params=json.loads(list[0].text)['data']['id']
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertNotEqual(json.loads(list[0].text)['data']['applyStatus'],'draft')

    def test10(self):
        u"""新增专家抽取信息而保存接口,评标用时字段为0.4测试"""
        res_list=ymsp.single_expert_preservation('apisxy','123456',0.4)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])
    def test11(self):
        u"""新增专家抽取信息而提交接口,评标用时字段为0.4测试"""
        res_list=ymsp.single_expert_submit('apisxy','123456',0.4)
        params=f"{json.loads(res_list[0].text)['data']['id']}"
        sql="SELECT * from expert_apply WHERE id=%s"
        result=mysql_db.all_chall(sql,params)
        self.assertIn(json.loads(res_list[0].text)['data']['id'],result[0])

