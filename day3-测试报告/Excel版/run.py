'''
执行类：
    执行
'''

from unittest import TestCase
from selenium import webdriver
from ddt import ddt
from ddt import data
from Data import InitPage
from Login import LoginTest
import time

@ddt
class TestLogin(TestCase):
    # 在所有方法执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get(r"http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在所有用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()  # 退出浏览器

    #成功结果
    @data(*InitPage.success)
    def testSuccessCase1(self,testdata):

        # 提取数据
        username = testdata[0]
        password = testdata[1]
        expect = testdata[2]

        # 调用被测操作类
        ClassLogin = LoginTest(self.driver)
        time.sleep(1)
        ClassLogin.login(username,password)

        # 获取实际结果
        data = ClassLogin.getSuccessResult()
        #  断言
        if expect != data:
            self.driver.save_screenshot("登陆失败.png")
        else:
            self.assertEqual(data,expect)

    #失败结果
    @data(*InitPage.error)
    def testSuccessCase2(self,testdata):

        # 提取数据
        username = testdata[0]
        password = testdata[1]
        expect = testdata[2]

        # 调用被测操作类
        time.sleep(1)
        ClassLogin = LoginTest(self.driver)
        time.sleep(1)
        ClassLogin.login(username,password)

        # 获取实际结果
        data = ClassLogin.getErrorResult()

        #  断言
        if expect != data:
            self.driver.save_screenshot("登陆失败.png")
        else:
            self.assertEqual(data,expect)




#
# @ddt
# class TestLogin(TestCase):
#     # 在所有方法执行前执行
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get(r"http://localhost:8080/HKR")
#         self.driver.maximize_window()
#
#     # 在所有用例执行后执行
#     def tearDown(self) -> None:
#         self.driver.quit()  # 退出浏览器
#
#
#     @data(*InitPage.login_success_data)
#     def testSuccessCase1(self,testdata):
#
#         # 提取数据
#         username = testdata["username"]
#         password =  testdata["password"]
#         expect =  testdata["expect"]
#
#         # 调用被测操作类
#         loginObj = LoginTest(self.driver)
#         time.sleep(2)
#         loginObj.login(username,password)
#
#         # 获取实际结果
#         data = loginObj.getSuccessResult()
#         #  断言
#         self.assertEqual(data,expect)
#
#
#     @data(*InitPage.login_error_data)
#     def testSuccessCase2(self,testdata):
#
#         # 提取数据
#         username = testdata["username"]
#         password =  testdata["password"]
#         expect =  testdata["expect"]
#
#         # 调用被测操作类
#         loginObj = LoginTest(self.driver)
#         time.sleep(2)
#         loginObj.login(username,password)
#
#         # 获取实际结果
#         data = loginObj.getErrorResult()
#
#         #  断言
#         self.assertEqual(data,expect)