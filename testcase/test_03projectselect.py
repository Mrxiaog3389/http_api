# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import main_init
from models.db_con import Db_Connection
import unittest,json,random,time
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
        u"""备案计划根据检索条件“申报单位”输入关键字内容进行精准查询"""
        res_list=ymsp.Record_plan_view('1','10',applicationOrgan='阳煤石化',organizationalType='',capitalSourceId=''
                                       ,organizationalMode='',organizationalOrgan='')
        sql="SELECT * FROM project_record_plan WHERE is_delete='0' AND application_organ LIKE '%阳煤石化%'"
        sql_select=mysql_db.all(sql)
        projectname=[]
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[0].text)['data']:
            self.assertEqual('阳煤石化',i['applicationOrgan'])
            self.assertIn(i['projectName'],projectname)
        self.assertEqual(int(json.loads(res_list[0].text)['total']),len(sql_select))

    def test02(self):
        u"""备案计划根据检索条件“申报单位”输入关键字内容为空进行查询"""
        res_list=ymsp.Record_plan_view('1','10',applicationOrgan='',organizationalType='',capitalSourceId=''
                                       ,organizationalMode='',organizationalOrgan='')
        sql="SELECT * FROM project_record_plan WHERE is_delete='0' "
        sql_select=mysql_db.all(sql)
        projectname=[]
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[0].text)['data']:
            self.assertIn(i['projectName'],projectname)
        self.assertEqual(int(json.loads(res_list[0].text)['total']),len(sql_select))

    def test03(self):
        u"""备案计划根据检索条件“申报单位”输入关键字内容为空格进行查询"""
        res_list=ymsp.Record_plan_view('1','10',applicationOrgan=' ',organizationalType='',capitalSourceId='',
                                       organizationalMode='',organizationalOrgan='')
        self.assertEqual(json.loads(res_list[0].text)['data'],[])

    def test04(self):
        u"""备案计划根据检索条件“申报单位”输入关键字内容进行模糊查询"""
        res_list=ymsp.Record_plan_view('1','10',applicationOrgan='龙川',organizationalType='',capitalSourceId='',
                                       organizationalMode='',organizationalOrgan='')
        sql="SELECT * FROM project_record_plan WHERE is_delete='0' AND application_organ LIKE '%龙川%'"
        sql_select=mysql_db.all(sql)
        projectname=[]
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[0].text)['data']:
            self.assertIn('龙川',i['applicationOrgan'])
            self.assertIn(i['projectName'],projectname)
        self.assertEqual(int(json.loads(res_list[0].text)['total']),len(sql_select))

    def test05(self):
        u"""备案计划根据检索条件“申报单位”复输入相同的数据，如5次以上，看处理是否正确 """
        for a in range(1,6):
            res_list=ymsp.Record_plan_view('1','10',applicationOrgan='阳煤石化',organizationalType='',
                                           capitalSourceId='',organizationalMode='',organizationalOrgan='')
            sql="SELECT * FROM project_record_plan WHERE is_delete='0' AND application_organ LIKE '%阳煤石化%'"
            sql_select=mysql_db.all(sql)
            projectname=[]
            for j in sql_select:
                projectname.append(j[1])
            for i in json.loads(res_list[0].text)['data']:
                self.assertEqual('阳煤石化',i['applicationOrgan'])
                self.assertIn(i['projectName'],projectname)
            self.assertEqual(int(json.loads(res_list[0].text)['total']),len(sql_select))

    def test06(self):
        u"""项目备案根据检索条件“申报单位”输入关键字内容进行精准查询"""
        res_list = ymsp.Record_plan_view('1', '10',applicationOrgan='龙川电厂',organizationalType='',
                                         capitalSourceId='',organizationalMode='',organizationalOrgan='')
        sql = "SELECT * FROM project WHERE is_delete='0' AND application_organ LIKE '%龙川电厂%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[1].text)['data']:
            self.assertEqual('龙川电厂', i['applicationOrgan'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[1].text)['total']), len(sql_select))

    def test07(self):
        u"""项目备案根据检索条件“申报单位”输入关键字内容为空进行查询"""
        res_list = ymsp.Record_plan_view('1', '10',applicationOrgan='',organizationalType='',
                                         capitalSourceId='',organizationalMode='',organizationalOrgan='')
        sql = "SELECT * FROM project WHERE is_delete='0' "
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[1].text)['data']:
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[1].text)['total']), len(sql_select))

    def test08(self):
        u"""项目备案根据检索条件“申报单位”输入关键字内容为空格进行查询"""
        res_list = ymsp.Record_plan_view('1', '10',applicationOrgan=' ',organizationalType='',
                                         capitalSourceId='',organizationalMode='',organizationalOrgan='')
        self.assertEqual(json.loads(res_list[1].text)['data'], [])

    def test09(self):
        u"""项目备案根据检索条件“申报单位”输入关键字内容进行模糊查询"""
        res_list = ymsp.Record_plan_view('1', '10',applicationOrgan='龙川',organizationalType='',
                                         capitalSourceId='',organizationalMode='',organizationalOrgan='')
        sql = "SELECT * FROM project WHERE is_delete='0' AND application_organ LIKE '%龙川%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[1])
        for i in json.loads(res_list[1].text)['data']:
            self.assertIn('龙川', i['applicationOrgan'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[1].text)['total']), len(sql_select))

    def test10(self):
        u"""项目备案根据检索条件“申报单位”复输入相同的数据，如5次以上，看处理是否正确 """
        for a in range(1,6):
            res_list=ymsp.Record_plan_view('1','10',applicationOrgan='龙川电厂',organizationalType='',
                                           capitalSourceId='',organizationalMode='',organizationalOrgan='')
            sql="SELECT * FROM project WHERE is_delete='0' AND application_organ LIKE '%龙川电厂%'"
            sql_select=mysql_db.all(sql)
            projectname=[]
            for j in sql_select:
                projectname.append(j[1])
            for i in json.loads(res_list[1].text)['data']:
                self.assertEqual('龙川电厂',i['applicationOrgan'])
                self.assertIn(i['projectName'],projectname)
            self.assertEqual(int(json.loads(res_list[1].text)['total']),len(sql_select))

    def test11(self):
        u"""控制价备案查看根据检索条件“申报单位”输入关键字内容进行精准查询"""
        res_list = ymsp.Record_plan_view('1', '10', '阳煤石化')
        sql = "SELECT * FROM bidding_control_price_record WHERE is_delete='0' AND application_unit LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[2].text)['data']:
            self.assertEqual('阳煤石化', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[2].text)['total']), len(sql_select))

    def test12(self):
        u"""控制价备案查看根据检索条件“申报单位”输入关键字内容为空进行查询"""
        res_list = ymsp.Record_plan_view('1', '10', '')
        sql = "SELECT * FROM bidding_control_price_record WHERE is_delete='0'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[2].text)['data']:
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[2].text)['total']), len(sql_select))

    def test13(self):
        u"""控制价备案查看根据检索条件“申报单位”输入关键字内容为空格进行查询"""
        res_list = ymsp.Record_plan_view('1', '10', ' ')
        self.assertEqual(json.loads(res_list[2].text)['data'], [])

    def test14(self):
        u"""控制价备案查看根据检索条件“申报单位”输入关键字内容进行模糊查询"""
        res_list = ymsp.Record_plan_view('1', '10', '阳煤')
        sql = "SELECT * FROM bidding_control_price_record WHERE is_delete='0' AND application_unit LIKE '%阳煤%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[2].text)['data']:
            self.assertIn('阳煤', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[2].text)['total']), len(sql_select))

    def test15(self):
        u"""控制价备案查看根据检索条件“申报单位”复输入相同的数据，如5次以上，看处理是否正确 """
        for a in range(1,6):
            res_list=ymsp.Record_plan_view('1','10','阳煤石化')
            sql="SELECT * FROM bidding_control_price_record WHERE is_delete='0' AND application_unit LIKE '%阳煤石化%'"
            sql_select=mysql_db.all(sql)
            projectname=[]
            for j in sql_select:
                projectname.append(j[2])
            for i in json.loads(res_list[2].text)['data']:
                self.assertEqual('阳煤石化',i['applicationUnit'])
                self.assertIn(i['projectName'],projectname)
            self.assertEqual(int(json.loads(res_list[2].text)['total']),len(sql_select))

    def test16(self):
        u"""中标通知书备案查看根据检索条件“申报单位”输入关键字内容进行精准查询"""
        res_list = ymsp.Record_plan_view('1', '10', '阳煤石化')
        sql = "SELECT * FROM win_bidding_notification_filing WHERE is_delete='0' AND application_unit LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[3].text)['data']:
            self.assertEqual('阳煤石化', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[3].text)['total']), len(sql_select))

    def test17(self):
        u"""中标通知书备案查看根据检索条件“申报单位”输入关键字内容为空进行查询"""
        res_list = ymsp.Record_plan_view('1', '10', '')
        sql = "SELECT * FROM win_bidding_notification_filing WHERE is_delete='0'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[3].text)['data']:
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[3].text)['total']), len(sql_select))

    def test18(self):
        u"""中标通知书备案查看根据检索条件“申报单位”输入关键字内容为空格进行查询"""
        res_list = ymsp.Record_plan_view('1', '10', ' ')
        self.assertEqual(json.loads(res_list[3].text)['data'], [])

    def test19(self):
        u"""中标通知书备案查看根据检索条件“申报单位”输入关键字内容进行模糊查询"""
        res_list = ymsp.Record_plan_view('1', '10', '阳煤')
        sql = "SELECT * FROM win_bidding_notification_filing WHERE is_delete='0' AND application_unit LIKE '%阳煤%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[3].text)['data']:
            self.assertIn('阳煤', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[3].text)['total']), len(sql_select))

    def test20(self):
        u"""中标通知书备案查看根据检索条件“申报单位”复输入相同的数据，如5次以上，看处理是否正确 """
        for a in range(1,6):
            res_list=ymsp.Record_plan_view('1','10','阳煤石化')
            sql="SELECT * FROM win_bidding_notification_filing WHERE is_delete='0' AND application_unit LIKE '%阳煤石化%'"
            sql_select=mysql_db.all(sql)
            projectname=[]
            for j in sql_select:
                projectname.append(j[2])
            for i in json.loads(res_list[3].text)['data']:
                self.assertEqual('阳煤石化',i['applicationUnit'])
                self.assertIn(i['projectName'],projectname)
            self.assertEqual(int(json.loads(res_list[3].text)['total']),len(sql_select))

    def test21(self):
        u"""备案计划下组织类型、资金来源、组织方式、组织单位、申报单位组合查询"""
        res_list = ymsp.Record_plan_view('1', '10', applicationOrgan='阳煤',organizationalType='ENGINEERING',
                                         capitalSourceId='2MDof18kB3z2uXc2vtx1JC',organizationalMode='1',organizationalOrgan='1')

        sql = "SELECT * FROM project_record_plan WHERE organizational_type='ENGINEERING' and capital_source='矿转产资金'and organizational_mode='1' and organizational_organ='1' AND application_organ LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[1])
        # for i in json.loads(res_list[0].text)['data']:
        #     self.assertIn('阳煤', i['applicationOrgan'])
        #     self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[0].text)['total']), len(sql_select))


    def test22(self):
        u"""项目备案下组织类型、组织方式、组织单位、申报单位组合查询"""
        res_list = ymsp.Record_plan_view('1', '10', applicationOrgan='阳煤',organizationalType='ENGINEERING',capitalSourceId='',
                                         organizationalMode='1',organizationalOrgan='1')

        sql = "SELECT * FROM project WHERE organizational_type='ENGINEERING' and organizational_mode='1' and organizational_organ='1' AND application_organ LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[1])
        # for i in json.loads(res_list[0].text)['data']:
        #     self.assertIn('阳煤', i['applicationOrgan'])
        #     self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[1].text)['total']), len(sql_select))

    def test23(self):
        u"""控制价备案下组织方式、组织单位、申报单位组合查询"""
        res_list = ymsp.Record_plan_view('1', '10', applicationOrgan='阳煤石化',
                                         organizationalMode='招投标办组织',organizationalOrgan='公开招标')
        sql = "SELECT * FROM bidding_control_price_record WHERE organization_form='公开招标' and organization_unit='招投标办组织' AND application_unit LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[2].text)['data']:
            self.assertIn('阳煤', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[2].text)['total']), len(sql_select))

    def test24(self):
        u"""中标通知书备案下组织方式、组织单位、申报单位组合查询"""
        res_list = ymsp.Record_plan_view('1', '10', applicationOrgan='阳煤石化',
                                         organizationalMode='招投标办组织',organizationalOrgan='公开招标')
        sql = "SELECT * FROM win_bidding_notification_filing WHERE organization_form='公开招标' and organization_unit='招投标办组织' AND application_unit LIKE '%阳煤石化%'"
        sql_select = mysql_db.all(sql)
        projectname = []
        for j in sql_select:
            projectname.append(j[2])
        for i in json.loads(res_list[3].text)['data']:
            self.assertIn('阳煤', i['applicationUnit'])
            self.assertIn(i['projectName'], projectname)
        self.assertEqual(int(json.loads(res_list[3].text)['total']), len(sql_select))
