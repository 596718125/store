from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
from urllib import request

driver = webdriver.Chrome()

driver.get("http://www.jd.com")

driver.maximize_window()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='key']").send_keys("G15")     #搜索 G15

driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()     #点击搜索

driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@title='戴尔（DELL）']").click()      #选择品牌：戴尔（DELL）

driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[4]/div/div[1]/a/img").click()
#点击下侧列表中的链接图片

handles = driver.window_handles   #  获取窗口数量

driver.switch_to.window(handles[1])     #切换第二个窗口

driver.implicitly_wait(3)      #等待加载，参数：等待可执行时长

driver.find_element_by_xpath("//*[@id='spec-n1']/ul/li/span").click()       #点击新弹窗中的播放

time.sleep(2)       #等待10秒

driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[4]/a/i").click()      #选择配置1

driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@id='choose-attr-2']/div[2]/div[3]/a").click()        #选择配置2

driver.implicitly_wait(3)

driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()      #加入购物车

time.sleep(2)

driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()     #点击账户登录

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("12306")           #输入用户名

driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("admin")           #输入密码

driver.find_element_by_xpath("//*[@id='loginsubmit']").click()            #点击登录

time.sleep(3)

ac = ActionChains(driver)

ele = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")     #获取滑动按钮

while True:           #循环滑动
    ac.click_and_hold(ele).move_by_offset(200,0).perform()
    ac.release().perform()











