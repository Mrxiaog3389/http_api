# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : xiaoyunlong
import requests,json
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

    def bidding_login(self,usename:str,password:str):
        """开标系统——登录接口"""
        url = api_config.biddinglogin
        data = {'username': usename, 'password': password,
                "userClass":"empty"}
        html = requests.post(url, verify=False, data=data)
        return html.cookies

    def select_version(self):
        """获取版本号"""
        url = ymjt.url+ymjt.version
        token='Bearer '+self.login('zhangjinli','123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization']=token
        response = requests.request("GET", url,headers=headers).json()
        return response

    def increase_project(self):
        """获取题库分类列表"""
        url = ymjt.url+ymjt.insert_project
        token = 'Bearer ' + self.login('zhangjinli', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token
        data={"organTId":"8066ebc38b714d9e9123a74152c26991", # 招标人
              "ipsoJure":"1",  # 招标人
              "name":"测试12-30",# 项目名称
              "address":"四川成都",  # 项目地址
              "regionName":"临沧市", # 项目行政划分
              "regionCode":"530900", #
              "legalPerson":"丽娜测试单位", # 项目法人单位名称
              "contactPerson":"招标人",   # 联系人（招标人）
              "contactWay":"18483663883", # 联系方式（招标人）
              "industryTypesName":"煤炭开采和洗选业", # 项目行业类型
              "industryTypes":"B06", #
              "currencyCode":"156", #
              "investmentAmount":"2000", # 投资金额
              "priceUnit":"2", #
              "approvalName":"测试12-30", # 项目批文名称
              "projectSchemeNumber":"564343453", # 招标方案核准号
              "file":"", # 上传文件
              "approvalFileId":"", #
              "approvalAuthority":"招标办", # 项目批文单位
              "approvalNumber":"4242", # 批文号
              "approvalDate":"2020-12-30", # 项目审批时间
              "isEnterArena":"0", # 是否进场
              "superviseCheck":"0", #
              "tradingCenter":"yangmei8a9s7455634s7d55s8f45sdf", #
              "capitalSourceType":"C", #
              "capitalSource":"111", # 资金来源
              "scale":"111", # 项目规模
              "percentage":""}
        payload = json.dumps(data)
        response = requests.request("POST", url, data=payload,headers=headers).json()
        print(response)
        return response

    def select_project(self):
        """查询项目"""
        url = ymjt.url+ymjt.select_project

        token = 'Bearer ' + self.login('zhangjinli', '123456')['data']['token']
        headers = {'Content-Type': 'application/json'}
        headers['Authorization'] = token

        data = {'pageNum': '1', 'pageSize': '10'}
        response = requests.request("POST", url, data=data,headers=headers).json()
        print(response)
        return response['data'][0]['id']

    def delete_project(self,ids):
        """删除项目"""
        url = ymjt.url+ymjt.delete_project

        token = 'Bearer ' + self.login('zhangjinli', '123456')['data']['token']
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        headers['Authorization'] = token

        data = {'ids': ids}
        response = requests.post(url, headers=headers, data=data).json()
        return  response

    def select_Bidding_project(self,d):
        """查询预审或后审项目"""
        url = ymjt.url+ymjt.select_Bidding_project+f'?reviewType={d}'
        token = 'Bearer ' + self.login('zhangjinli', '123456')['data']['token']
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'TenantKey': 'OlOGefRq7IrIA2L4R7JZGvnY5nMnvjAU7WjJwXNUxCG0RJRwEUocelnNXf9ZfAnE',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                   'UserClass': 'AGENCY',
                   'Origin': 'http://ymjt.jcebid.com'}
        headers['Authorization'] = token

        data = {'pageNum': '1', 'pageSize': '10'}
        response = requests.request("POST", url, data=data, headers=headers).json()
        print(response)
        return response

    def select_Bidding(self):
        """查询预审或后审项目"""
        url = ymjt.select_Bidding
        response =  requests.get(url, verify=False, cookies=self.bidding_login('toufu1', '1'))
        print(response.json())
        return response

    def username(self):

        url = ymjt.username
        token = 'Bearer ' + self.login('admin', '123456')['data']['token']
        headers = {'Host': 'zts.ztb.jcebid.com', 'Connection': 'keep-alive',
                   'Accept': 'application/json, text/javascript, */*; q=0.01'}
        headers['Authorization'] = token
        response = requests.get(url, headers=headers)
        print(response)
        return response
    #
    # def dale_question_bank(self,admin_id,key,class_id:int):
    #     """删除题库分类"""
    #     url = api_config.url+api_config.dele_question_class+f"&admin_id={admin_id}&key={key}"+api_config.appcode
    #
    #     payload = {'class_id': class_id}
    #     response = requests.request("POST", url,data=payload).json()
    #     return response
    #
    # def select_subject(self,admin_id,key,curpage:int,pagesize:int,question_type:str=None,question_title:str=None,class_id:int=None):
    #     """获取题目列表"""
    #     url = api_config.url+api_config.sele_question+f"&admin_id={admin_id}&key={key}"+api_config.appcode
    #     payload = {'curpage': curpage,
    #                'pagesize': pagesize,
    #                'question_type':question_type,
    #                'question_title':question_title,
    #                'class_id':class_id}
    #     response = requests.request("POST", url,data=payload).json()
    #     return response
    #
    # def divert(self,admin_id,key,question_id:str,class_id:str):
    #     """转移题"""
    #     url = api_config.url+api_config.divert+api_config.appcode
    #     payload = {'question_id': question_id,
    #                'class_id': class_id,
    #                'admin_id': admin_id,
    #                'key': key}
    #     response = requests.request(api_config.url_prefix, url,data=payload).json()
    #     return response
    #
    # def delete(self,admin_id,key,question_id:int):
    #     """删除题"""
    #     url = api_config.url+api_config.delete+api_config.appcode
    #     payload = {'question_id': question_id,
    #                'admin_id': admin_id,
    #                'key': key}
    #     response = requests.request(api_config.url_prefix, url,data=payload).json()
    #     return response
    #
    # def increase(self,admin_id,key,class_id:int,question_type:int,question_title:str,correct_option:str,analysis:str,options:list):
    #     """添加题目"""
    #     url = api_config.url+api_config.increase_question+api_config.appcode
    #     options=json.dumps(options, ensure_ascii=False)
    #     payload = {'class_id': class_id,
    #                'question_type':question_type,
    #                'question_title': question_title,
    #                'correct_option': correct_option,
    #                'analysis': analysis,
    #                'options': options,
    #                'admin_id': admin_id,
    #                'key': key}
    #     response = requests.request(api_config.url_prefix, url,data=payload).json()
    #     return response
    #
    # def updata(self,admin_id,key,question_id:int,class_id:int,question_title:str,correct_option:str,analysis:str,options:list):
    #     """更新题目"""
    #     url = api_config.url+api_config.increase_question+api_config.appcode
    #     options = json.dumps(options, ensure_ascii=False)
    #     payload = {'question_type':question_id,
    #                'class_id': class_id,
    #                'question_title': question_title,
    #                'correct_option': correct_option,
    #                'analysis': analysis,
    #                'options': options,
    #                'admin_id': admin_id,
    #                'key': key}
    #     response = requests.request(api_config.url_prefix, url,data=payload).json()
    #     return response

o = Oalogin()
o.username()
# o.delete_project(o.select_project())

# options=[{'serial_num':'A','option_title':'qw'},{'serial_num':'B','option_title':'we'}]
# jsonArr = json.dumps(options, ensure_ascii=False)
# print(type(jsonArr))
# o.increase(test['data']['admin_id'], test['data']['key'],14,1,'您的主要收入来源是：','A','',jsonArr)
# o.delete(test['data']['admin_id'], test['data']['key'],'18')
# o.increase_question_bank(test['data']['admin_id'], test['data']['key'],'18')
# o.alter_question_bank(test['data']['admin_id'], test['data']['key'],'51','98')
# o.dale_question_bank(test['data']['admin_id'], test['data']['key'],240)