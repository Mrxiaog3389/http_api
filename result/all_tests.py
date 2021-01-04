import unittest
from common import HTMLTestRunner


# 测试用例存放路径
case_path = r'D:\Python\cloud_api\testcase'

# 获取所有测试用例
def get_allcase():
    testunit = unittest.TestSuite()
    # 测试模块的顶层目录，即测试用例不是放在多级目录下，top_levle_dir设置为none
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py",top_level_dir=None)

    for suite in discover:  #使用for循环出suite,再循环出case
        for case in suite:
            testunit.addTests(case)
    return testunit

allcasenames = get_allcase()
filename = 'report\\result.html'
fp = open(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
     stream=fp,
     title=u'小财训练营后台题库管理模块、考试管理模块接口测试报告',
     description=u'测试用例执行结果')

runner.run(allcasenames)

fp.close()