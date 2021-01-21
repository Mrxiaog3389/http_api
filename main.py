from common import HTMLTestRunner
from result import all_tests
from email.mime.text import MIMEText
import smtplib

if __name__ == '__main__':
     allcasenames = all_tests.get_allcase()
     filename = 'report\\result.html'
     fp = open(filename, 'wb')
     runner = HTMLTestRunner.HTMLTestRunner(
          stream=fp,
          title=u'阳煤审批V1.1.6.1接口测试报告',
          description=u'测试用例执行结果')

     runner.run(allcasenames)

     fp.close()