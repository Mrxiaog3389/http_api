# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import requests,json,grequests,time,datetime
from common.common import api_config,ymjt

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

    def select_supplier_list(self):
        """获取供应商列表、供应商审核列表、黑名单列表"""
        data = {'pageNum': '1','pageSize':'10'}
        # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # headers={}
        # headers['Authorization'] = token
        req =[
            grequests.post(ymjt.url + ymjt.supplier_list,data=data),
            grequests.post(ymjt.url + ymjt.Supplier_blacklist, data=data),
            grequests.post(ymjt.url + ymjt.Supplier_audit, data=data)
        ]
        res_list = grequests.map(req)
        list=[]
        for r in res_list:
            list.append(json.loads(r.text))
        return list

    def select_single_supplier(self):
        """获取单一供应商信息"""
        res_list=self.select_supplier_list()[0]['data']

        id=[i['id'] for i in res_list]

        url_list=[ymjt.url+ymjt.single_supplier+f"id={i}"+f"&_={int(time.mktime(datetime.datetime.now().timetuple()) * 1000)}" for i in id]

        # # token = 'Bearer ' + self.login('apisxy','123456')['data']['token']
        # # headers={}
        # # headers['Authorization'] = token

        req_list=[]
        for u in url_list:
            req_list.append(grequests.get(u))

        res_list = grequests.map(req_list)
        for r in res_list:
            print(json.loads(r.text))

o = Oalogin()
o.select_single_supplier()