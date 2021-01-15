import uuid,random,datetime,string,requests,json

class supplier_library(object):


    def supplier_increase_submit_HG(self):
        supplier_insert={"id": str(uuid.uuid1()),
                         "founderId": "ba50a20028a5405da331a08297fe3de2",
                         "createUnitsId": "ba50a20028a5405da331a08297fe3de2",
                         "supplierName": "成都测试"+str(random.randint(0,100000)),
                         "supplierCode": "",
                         "supplierAccount": "cdzts"+str(random.randint(0,100000)),
                         "supplierPassword": "123456",
                         "supplierAbbreviation": "q",
                         "supplierLevel": "1",
                         "supplierType": "1",
                         "capital": "200",
                         "capitalType": "CNY",
                         "corporateRepresentativeName": "qw",
                         "language": "ZH",
                         "supplierCountry": "CN",
                         "supplierProvince": "510",
                         "suplierCity": "成都",
                         "supplierDetailAddress": "东升街道双楠大道中段199号世代积家装饰家居广场五楼",
                         "contactPerson": "测试",
                         "contactPhone": "18483663883",
                         "postCode": "643000",
                         "companyEmail": "18483663883@163.com",
                         "companyPhone": "02896324568",
                         "faxNo": "02896324568",
                         "businessTime": "2012-08-29 至 无固定期限",
                         "companyNature": "205",
                         "supplierInsideCode": "1",
                         "threeInOne": "Y",
                         "unifySocialCode": "91140000110014497J",
                         "file": "",
                         "unifySocialFujianId": "7878061cb88347088a0ad05e07289f71",
                         "registrationNumber": "",
                         "taxNumber": "",
                         "organizationCode": "",
                         "registrationNumberFujianId": "",
                         "taxNumberFujianId": "",
                         "organizationFujianId": "",
                         "belongCompany": "HG",
                         "qualification": "91140000110014497J",
                         "performance": "91140000110014497J",
                         "addOrUpdate": "add",
                         "otherFujianId": "",
                         "bankFrontVoList": ""}
        url = 'http://ymjt.jcebid.com/base-library/service/api/supplierBank/addSupplierBank'
        data = {"bankCountryCode": "",
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
                "supplierId": supplier_insert['id']}
        payload = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        html = requests.post(url, verify=False, headers=headers, data=payload).json()
        return supplier_insert

    def supplier_increase_submit_OTHER(self):
        supplier_insert={
            "id":str(uuid.uuid1()),
            "founderId":"0536e312fe3e44d58a10c38e88a3e1c3",
            "createUnitsId":"0536e312fe3e44d58a10c38e88a3e1c3",
            "supplierName":"成都测试"+str(random.randint(0,100000)),
            "supplierCode":"",
            "supplierAccount":"cdzts"+str(random.randint(0,100000)),
            "supplierPassword":"123456",
            "supplierAbbreviation":"中条山",
            "supplierLevel":"1",
            "supplierType":"1",
            "capital":"87,386.1",
            "capitalType":"CNY",
            "corporateRepresentativeName":"刘广耀",
            "language":"ZH",
            "supplierCountry":"CN",
            "supplierProvince":"140",
            "suplierCity":"运城",
            "supplierDetailAddress":"垣曲县东峰山 ",
            "contactPerson":"刘广耀",
            "contactPhone":"18483663883",
            "postCode":"643000",
            "companyEmail":"18483663883@163.com",
            "companyPhone":"0359-6031597",
            "faxNo":"0359-6031597",
            "businessTime":"1989-07-20 至 无固定期限",
            "companyNature":"205",
            "supplierInsideCode":"1",
            "threeInOne":"Y",
            "unifySocialCode":"91140000110014497J",
            "file":"",
            "unifySocialFujianId":"08dfab5eb8d44f2499f466dd532dfc1b",
            "registrationNumber":"",
            "taxNumber":"",
            "organizationCode":"",
            "registrationNumberFujianId":"",
            "taxNumberFujianId":"",
            "organizationFujianId":"",
            "belongCompany":"OTHER",
            "qualification":"加工制造工业硅及其炭素制品；批发零售建材(木材除外）；进出口：出口本企业自产的水泥；进口本企业生产科研所需的原辅材料、机械设备、仪器仪表及零配件（以批准的商品目录为准）；设备制造、修理、安装及备件制作（除特种设备）；",
            "performance":"加工制造工业硅及其炭素制品；批发零售建材(木材除外）；进出口：出口本企业自产的水泥；进口本企业生产科研所需的原辅材料、机械设备、仪器仪表及零配件（以批准的商品目录为准）；设备制造、修理、安装及备件制作（除特种设备）；",
            "addOrUpdate":"add",
            "otherFujianId":"",
            "bankFrontVoList":""
        }
        url = 'http://ymjt.jcebid.com/base-library/service/api/supplierBank/addSupplierBank'
        data = {"bankCountryCode":"",
                "bankCountry":"645",
                "bankCountryName":"中国",
                "bankName":"中信银行股份有限公司东营胜利支行",
                "bankCode":"302455077209",
                "bankAccountPurpose":"基本存款账户",
                "bankAccountName":"东营胜利支行",
                "bankAccount":"8115501018888888888",
                "file":"",
                "attachmentId":str(uuid.uuid4()),
                "bankFujianId":"d0d0f6bb24644486a9392fdb538f8f65,",
                "supplierId":supplier_insert['id']}
        payload = json.dumps(data)
        headers = {'Content-Type': 'application/json'}
        html = requests.post(url, verify=False, headers=headers,data=payload).json()
        return supplier_insert

    def supplier_increase_preservation(self,createUnitsId):
        """新增后保存"""
        supplier_insert={
            "id":str(uuid.uuid1()),
            "supplierName": "成都测试"+str(random.randint(0,100000)),
            "supplierCode": "",
            "supplierAccount": "cdzts"+str(random.randint(0,100000)),
            "supplierPassword": "123456",
            "supplierAbbreviation": "中条山",
            "supplierLevel": "1",
            "supplierType": "1",
            "capital": "",
            "capitalType": "CNY",
            "corporateRepresentativeName": "",
            "language": "ZH",
            "supplierCountry": "",
            "supplierProvince": "",
            "suplierCity": "",
            "supplierDetailAddress": "",
            "contactPerson": "",
            "contactPhone": "",
            "postCode": "",
            "companyEmail": "",
            "companyPhone": "",
            "faxNo": "",
            "businessTime": "",
            "companyNature": "205",
            "supplierInsideCode": "1",
            "threeInOne": "Y",
            "unifySocialCode": "",
            "unifySocialFujianId": "",
            "registrationNumber": "",
            "taxNumber": "",
            "organizationCode": "",
            "registrationNumberFujianId": "",
            "taxNumberFujianId": "",
            "organizationFujianId": "",
            "qualification": "",
            "performance": "",
            "addOrUpdate": 'addDraft',
            "otherFujianId": "",
            "founderId": "0536e312fe3e44d58a10c38e88a3e1c3",
            "createUnitsId": createUnitsId}

        return supplier_insert

    def supplier_update_preservation(self,createUnitsId):
        """修改后保存"""
        supplier_insert={
            "supplierName": "成都测试"+str(random.randint(0,100000)), "supplierCode": "",
            "supplierAccount": "cdzts"+str(random.randint(0,100000)), "supplierPassword": "123456", "supplierAbbreviation": "中条山", "supplierLevel": "1",
            "supplierType": "1", "capital": "2000", "capitalType": "CNY", "corporateRepresentativeName": "",
            "language": "ZH", "supplierCountry": "", "supplierProvince": "", "suplierCity": "",
            "supplierDetailAddress": "", "contactPerson": "", "contactPhone": "", "postCode": "", "companyEmail": "",
            "companyPhone": "", "faxNo": "", "businessTime": "", "companyNature": "205", "supplierInsideCode": "1",
            "threeInOne": "Y", "unifySocialCode": "", "unifySocialFujianId": "", "registrationNumber": "", "taxNumber": "",
            "organizationCode": "", "registrationNumberFujianId": "", "taxNumberFujianId": "", "organizationFujianId": "",
            "qualification": "", "performance": "", "addOrUpdate": "updateDraft", "otherFujianId": "",
            "founderId": "0536e312fe3e44d58a10c38e88a3e1c3", "createUnitsId": createUnitsId}
        return supplier_insert

    def supplier_update_submit_OTHER(self):
        """修改后提交"""
        supplier_insert={
            "addOrUpdate":"update","founderId":"0536e312fe3e44d58a10c38e88a3e1c3",
            "createUnitsId":"0536e312fe3e44d58a10c38e88a3e1c3","supplierName":"成都测试"+str(random.randint(0,100000)),"supplierCode":"",
            "supplierAccount":"cdzts"+str(random.randint(0,100000)),"supplierPassword":"123456","supplierAbbreviation":"中条山","supplierLevel":"1",
            "supplierType":"1","capital":"2000","capitalType":"CNY","corporateRepresentativeName":"qw","language":"ZH",
            "supplierCountry":"CN","supplierProvince":"510","suplierCity":"成都",
            "supplierDetailAddress":"东升街道双楠大道中段199号世代积家装饰家居广场五楼","contactPerson":"测试",
            "contactPhone":"18483663883","postCode":"643000","companyEmail":"18483663883@163.com","companyPhone":"02896324568",
            "faxNo":"02896324568","businessTime":"2012-08-29 至 无固定期限","companyNature":"205","supplierInsideCode":"1",
            "threeInOne":"Y","unifySocialCode":"91140000110014497J","file":"","unifySocialFujianId":"c6ab8b9aa2ba4ff28bb563f4e75efec5",
            "registrationNumber":"","taxNumber":"","organizationCode":"","registrationNumberFujianId":"",
            "taxNumberFujianId":"","organizationFujianId":"","belongCompany":"OTHER",
            "qualification":"91140000110014497J","performance":"91140000110014497J","otherFujianId":"","bankFrontVoList":""}
        return supplier_insert

    def supplier_update_submit_HG(self):
        """修改后提交"""
        supplier_insert={"addOrUpdate":"update","founderId":"ba50a20028a5405da331a08297fe3de2","createUnitsId":"ba50a20028a5405da331a08297fe3de2",
                         "supplierName":"成都测试"+str(random.randint(0,100000)),"supplierCode":"","supplierAccount":"cdzts"+str(random.randint(0,100000)),"supplierPassword":"123456",
                         "supplierAbbreviation":"cd123","supplierLevel":"1","supplierType":"1","capital":"380","capitalType":"CNY",
                         "corporateRepresentativeName":"qqq","language":"ZH","supplierCountry":"CN","supplierProvince":"510",
                         "suplierCity":"成都","supplierDetailAddress":"东升街道双楠大道中段199号世代积家装饰家居广场五楼",
                         "contactPerson":"cd123","contactPhone":"18483663883","postCode":"643000","companyEmail":"18483663883@163.com",
                         "companyPhone":"02896324568","faxNo":"02896324568","businessTime":"2012-08-29 至 无固定期限","companyNature":"205",
                         "supplierInsideCode":"1","threeInOne":"Y","unifySocialCode":"91140000110014497J","file":"",
                         "unifySocialFujianId":"b760610457e44d4c8180b7853696be66","registrationNumber":"",
                         "taxNumber":"","organizationCode":"","registrationNumberFujianId":"","taxNumberFujianId":"",
                         "organizationFujianId":"","belongCompany":"HG","qualification":"1111111111111111111111111111111",
                         "performance":"111111111111111111111111111111111111111","otherFujianId":"","bankFrontVoList":""}
        return supplier_insert

    def expert_extraction_increase(self,evaluateUseTime):
        supplier_insert={
            "projectName":"成都测试"+str(random.randint(0,100000)),
            "projectCode":string.digits,
            "organAName":"常州福特干燥设备有限公司",
            "organAId":"8543cd8acd3b4ef1bdfaeff3d3967043",
            "openTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "openPlace":"",
            "evaluateTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "evaluatePlace":"",
            "evaluateUseTime":evaluateUseTime,
            "projectContent":"",
            "applyType":"random",
            "expertCount":"",
            "applyStatus":"draft",
            "avoidances":[],
            "demands":[],
            "results":[]
        }
        return supplier_insert

    def expert_extraction_sumit(self,evaluateUseTime):
        supplier_insert = {
            "projectName":"成都测试"+str(random.randint(0,100000)),
            "projectCode":string.digits,
            "organAName":"常州福特干燥设备有限公司",
            "organAId":"8543cd8acd3b4ef1bdfaeff3d3967043",
            "openTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "openPlace":"cd",
            "evaluateTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "evaluatePlace":"成都",
            "evaluateUseTime":evaluateUseTime,
            "expertCount":"1",
            "applyType":"random",
            "projectContent":"11111",
            "demands":[{"majorId":"244be134b2e64eeead9e8ae3414c3bb1","majorName":"测试001","majorAllName":"测试1-测试1-1-测试001","expertCount":"1"}],
            "applyStatus":"process",
            "avoidances":[{"organId":"2960ea8f53ad479a8adc6e90bdd1a0f3","organName":"供应商测试token"},{"organId":"2da331a48f1d4b7c8bf885402843f14a","organName":"测试供应商审核"}]
        }
        return supplier_insert

    def expert_extraction_update(self):
        supplier_insert={
            "projectName":"成都测试"+str(random.randint(0,100000)),
            "projectCode":"651661",
            "organAName":"常州福特干燥设备有限公司",
            "organAId":"8543cd8acd3b4ef1bdfaeff3d3967043",
            "openTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "openPlace":"cd",
            "evaluateTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "evaluatePlace":"",
            "evaluateUseTime":"0.5",
            "projectContent":"",
            "applyStatus":"draft",
            "applyType":"random",
            "expertCount":"",
            "avoidances":[],
            "demands":[],
            "results":[]
        }
        return supplier_insert

    def expert_extraction_updatesumit(self):
        supplier_insert={
            "projectName":"成都测试"+str(random.randint(0,100000)),
            "projectCode":"651661",
            "organAName":"常州福特干燥设备有限公司",
            "organAId":"8543cd8acd3b4ef1bdfaeff3d3967043",
            "openTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "openPlace":"cd",
            "evaluateTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "evaluatePlace":"cd",
            "evaluateUseTime":"0.5",
            "expertCount":"1",
            "applyType":"random",
            "projectContent":"11111",
            "demands":[{"majorId":"5bdb7c10660843888e42f17f47812a53","majorName":"测3-3","majorAllName":"测试3-测3-3","expertCount":"1"}],
            "applyStatus":"process",
            "avoidances":[{"organId":"2960ea8f53ad479a8adc6e90bdd1a0f3","organName":"供应商测试token"},{"organId":"2da331a48f1d4b7c8bf885402843f14a","organName":"测试供应商审核"}]
        }
        return supplier_insert

library=supplier_library()
