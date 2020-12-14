#coding=utf-8
import ddt
import os
import time
import unittest
import sys
sys.path.append('E:/pythonProject/SeleniumPython')
import traceback
from selenium import webdriver
import HTMLTestRunner
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
ex=ExcelUtil()
data=ex.get_data()
#邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        # self.logger.info("this is chrome")
        self.login=RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name=self._testMethodName
                file_path = os.path.join("E:/pythonProject/SeleniumPython" + "/report/" + case_name+".png")
                self.driver.save_screenshot(file_path)
        # print("这个是case的后置条件")
        self.driver.close()
    # @ddt.data(
    #     ['123','gryufeng01','111111','code','user_email_error','请输入有效的电子邮件地址'],
    #     ['@qq.com', 'gryufeng02', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['123323@qq.com', 'gryufeng03', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址']
    #     )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self,data):
        email, username, password, code, assertCode, assertText=data
        email_error=self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error,'测试失败')

if __name__=='__main__':
    file_path = os.path.join("E:/pythonProject/SeleniumPython" + "/report/" + "first_case1.html")
    f = open(file_path, 'wb')
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description="这个是我们第一次测试报告1",verbosity=2)
    runner.run(suite)


