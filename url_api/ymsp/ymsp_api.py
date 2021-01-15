# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import requests,json,grequests,time,datetime,uuid
from common.common import api_config,ymjt
from url_api.ymsp.parameters import parame

class Oalogin():

    def login(self,usename:str,password:str):
        """登录接口"""
        url = api_config.login_url+api_config.login
        data = {'loginName': usename, 'password': password,
                "captchaCode":"1",
                "s":"OlOGefRq7IrIA2L4R7JZGvnY5nMnvjAU7WjJwXNUxCG0RJRwEUocelnNXf9ZfAnE"}
        payload = json.dumps(data)
        html = requests.post(url, verify=False, data=payload,headers=api_config.headers).json()
        return html

    def select_supplier_list(self,orgId):#'apisxy','123456'
        """获取供应商列表、供应商审核列表、黑名单列表"""
        data = {'pageNum': '1','pageSize':'10'}
        data1={'pageNum': '1', 'pageSize': '10', 'orgId': orgId}
        # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # headers = {'Content-Type': 'application/json'}
        # headers['Authorization'] = token
        req =[
            grequests.post(ymjt.url + ymjt.supplier_list,data=data),
            grequests.post(ymjt.url + ymjt.Supplier_audit, data=data1),
            grequests.post(ymjt.url + ymjt.Supplier_blacklist,data=data)
        ]
        res_list = grequests.map(req)
        list=[]
        for r in res_list:
            list.append(json.loads(r.text))
        return list

    def select_single_supplier(self):
        """获取单一供应商信息"""
        res_list=self.select_supplier_list('0536e312fe3e44d58a10c38e88a3e1c3')[0]['data']
        id=[i['id'] for i in res_list]
        url_list=[ymjt.url+ymjt.single_supplier+f"id={i}"+f"&_={int(time.mktime(datetime.datetime.now().timetuple()) * 1000)}" for i in id]
        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers={}
        # # headers['Authorization'] = token
        req_list=[]
        for u in url_list:
            req_list.append(grequests.get(u))

        res_list = grequests.map(req_list)
        return res_list

    def supplier_increase_preservation(self):
        """新增供应商保存成草稿信息"""
        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers['Authorization'] = token
        data=parame.library.supplier_increase_preservation("0536e312fe3e44d58a10c38e88a3e1c3")
        data1 = parame.library.supplier_increase_preservation("ba50a20028a5405da331a08297fe3de2")
        data = json.dumps(data)
        data1 = json.dumps(data1)
        req = [
            grequests.post(ymjt.url+ymjt.preservation, headers=api_config.headers,data=data),
            grequests.post(ymjt.url + ymjt.preservation, headers=api_config.headers, data=data1)
        ]
        res_list = grequests.map(req)
        return res_list

    def supplier_update_preservation(self,id,id_hg):
        """修改供应商保存成草稿信息"""
        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers['Authorization'] = token
        data = parame.library.supplier_update_preservation("0536e312fe3e44d58a10c38e88a3e1c3")
        data1 = parame.library.supplier_update_preservation("ba50a20028a5405da331a08297fe3de2")
        data['id'] = id
        data1['id'] = id_hg
        data = json.dumps(data)
        data1 = json.dumps(data1)
        req = [
            grequests.post(ymjt.url+ymjt.preservation, headers=api_config.headers,data=data),
            grequests.post(ymjt.url + ymjt.preservation, headers=api_config.headers, data=data1)
        ]
        res_list = grequests.map(req)
        return res_list

    def supplier_increase_submit_HG(self):
        """新增供应商提交信息"""
        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers['Authorization'] = token
        data = parame.library.supplier_increase_submit_HG()
        data = json.dumps(data)
        req = [
            grequests.post(ymjt.url + ymjt.Supplier_summit, headers=api_config.headers, data=data)
        ]
        res_list = grequests.map(req)
        return res_list

    def supplier_increase_submit_OTHER(self):
        """新增供应商提交信息"""
        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers['Authorization'] = token
        data = parame.library.supplier_increase_submit_OTHER()
        data = json.dumps(data)
        req = [
            grequests.post(ymjt.url + ymjt.Supplier_summit, headers=api_config.headers, data=data)
        ]
        res_list = grequests.map(req)
        return res_list

    def supplier_update_submit_OTHER(self,id):

        token = 'Bearer ' + self.login('apisxy', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data = parame.library.supplier_update_submit_OTHER()
        data['id'] = id
        url = 'http://ymjt.jcebid.com/base-library/service/api/supplierBank/addSupplierBank'
        data1 = {"bankCountryCode": "",
                 "bankCountry": "645",
                 "bankCountryName": "中国",
                 "bankName": "中信银行股份有限公司东营胜利支行",
                 "bankCode": "302455077209",
                 "bankAccountPurpose": "基本存款账户",
                 "bankAccountName": "东营胜利支行",
                 "bankAccount": "8115501018888888888",
                 "file": "",
                 "attachmentId": str(uuid.uuid4()),
                 "bankFujianId": "d0d0f6bb24644486a9392fdb538f8f65,",
                 "supplierId": id}
        payload = json.dumps(data1)
        headers = {'Content-Type': 'application/json'}
        html = requests.post(url, verify=False, headers=headers, data=payload).json()

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.url + ymjt.Supplier_summit, headers=headers, data=data)
        ]

        res_list = grequests.map(req)
        return res_list

    def supplier_update_submit_HG(self,id):
        """修改供应商提交信息"""
        token = 'Bearer ' + self.login('apisxy', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data=parame.library.supplier_update_submit_HG()
        data['id']=id
        url = 'http://ymjt.jcebid.com/base-library/service/api/supplierBank/addSupplierBank'
        data1 = {"bankCountryCode": "",
                "bankCountry": "645",
                "bankCountryName": "中国",
                "bankName": "中信银行股份有限公司东营胜利支行",
                "bankCode": "302455077209",
                "bankAccountPurpose": "基本存款账户",
                "bankAccountName": "东营胜利支行",
                "bankAccount": "8115501018888888888",
                "file": "",
                "attachmentId": str(uuid.uuid4()),
                "bankFujianId": "d0d0f6bb24644486a9392fdb538f8f65,",
                "supplierId": id}
        payload = json.dumps(data1)
        headers = {'Content-Type': 'application/json'}
        html = requests.post(url, verify=False, headers=headers, data=payload).json()

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.url+ymjt.Supplier_summit, headers=headers,data=data)
        ]

        res_list = grequests.map(req)
        return res_list

    def examine(self,supplierId):

        token = 'Bearer ' + self.login('ymhg', "123456")['data']['token']
        headers = {}
        headers['Authorization'] = token
        url = ymjt.url + ymjt.examine +f"supplierId={supplierId}"+f"&_={int(time.mktime(datetime.datetime.now().timetuple()) * 1000)}"
        req = [grequests.get(url,headers=headers)]
        res_list = grequests.map(req)
        return res_list

    def join_blacklist(self,supplierId):

        # token = 'Bearer ' + self.login('ymhg', "123456")['data']['token']
        # headers = {}
        # headers['Authorization'] = token
        data = {'id': supplierId, 'supplierClass': 'D'}
        url = ymjt.url + ymjt.join_blacklist
        req = [grequests.post(url,data=data)]
        res_list = grequests.map(req)
        return res_list

    def remove_blacklist(self,supplierId):

        # token = 'Bearer ' + self.login('ymhg', "123456")['data']['token']
        # headers = {}
        # headers['Authorization'] = token
        data = {'id': supplierId, 'supplierClass': 'B'}
        url = ymjt.url + ymjt.join_blacklist
        req = [grequests.post(url,data=data)]
        res_list = grequests.map(req)
        return res_list

    def project_supplierPage(self,usename:str,password:str):
        token = 'Bearer ' + self.login(usename, password)['data']['token']
        headers = {}
        headers['Authorization'] = token
        url = ymjt.ym_url + ymjt.project_supplierPage+f"pageNum=1&pageSize=10&_={int(time.mktime(datetime.datetime.now().timetuple()) * 1000)}"
        req = [grequests.get(url,headers=headers)]
        res_list = grequests.map(req)
        return res_list

    def select_expert_extraction_list(self,usename:str,password:str):
        """获取专家抽取列表"""

        token = 'Bearer ' + self.login(usename,password)['data']['token']
        headers={}
        headers['Authorization'] = token
        url=ymjt.ym_url+ymjt.expert_extraction_list+'pageNum=1&pageSize=10&_=1610541183483'
        req = [grequests.get(url,headers=headers)]
        res_list = grequests.map(req)
        list = []
        for r in res_list:
            list.append(json.loads(r.text))
        return list

    def select_single_expert_extraction(self):
        """获取单一专家信息"""
        res_list=self.select_expert_extraction_list('apisxy','123456')[0]['data']

        id=[i['id'] for i in res_list]

        url_list=[ymjt.ym_url+ymjt.single_expert_extraction+f"id={i}"+f"&_={int(time.mktime(datetime.datetime.now().timetuple()) * 1000)}" for i in id]

        token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        headers={}
        headers['Authorization'] = token

        req_list=[]
        for u in url_list:
            req_list.append(grequests.get(u,headers=headers))

        res_list = grequests.map(req_list)
        return res_list

    def single_expert_preservation(self,usename:str,password:str,evaluateUseTime):
        """新增专家抽取保存信息"""
        token = 'Bearer ' + self.login(usename, password)['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data=parame.library.expert_extraction_increase(evaluateUseTime)

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.ym_url+ymjt.expert_extraction_increase, headers=headers,data=data)
        ]

        res_list = grequests.map(req)
        return res_list

    def single_expert_submit(self,usename:str,password:str,evaluateUseTime):
        """新增专家抽取提取信息"""
        token = 'Bearer ' + self.login(usename, password)['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data=parame.library.expert_extraction_sumit(evaluateUseTime)

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.ym_url+ymjt.expert_extraction_increase, headers=headers,data=data)
        ]

        res_list = grequests.map(req)
        return res_list

    def update_expert_preservation(self,id):
        """修改专家抽取保存信息"""
        token = 'Bearer ' + self.login('apisxy', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data=parame.library.expert_extraction_update()
        data['id']=id

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.ym_url+ymjt.expert_extraction_update, headers=headers,data=data)
        ]

        res_list = grequests.map(req)
        return res_list

    def update_expert_submit(self,id):
        """修改专家抽取提取信息"""
        token = 'Bearer ' + self.login('apisxy', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data=parame.library.expert_extraction_updatesumit()
        data['id'] = id

        data = json.dumps(data)
        req = [
            grequests.post(ymjt.ym_url+ymjt.expert_extraction_increase, headers=headers,data=data)
        ]

        res_list = grequests.map(req)
        return res_list



# o = Oalogin()
# o.project_supplierPage()
# o.supplier_update_submit_OTHER()
# o.supplier_update_submit_HG()
# o.supplier_update_preservation('81d97224-56d1-11eb-b718-a87eeafcaf9a')
# o.update_submit('2a7ade00-567f-11eb-bbbc-a87eeafcaf9a')
# o.login('apisxy','123456')