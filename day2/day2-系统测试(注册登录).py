from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()     #打开谷歌驱动

driver.get("http://localhost:8080/HKR/")        #打开网站

driver.maximize_window()        #窗口最大化

driver.implicitly_wait(2)       #等待窗口加载

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()       #点击注册

driver.implicitly_wait(2)       #等待窗口加载

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("wyt")       #账户

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys("王一桐")     #用户名

driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123123")      #密码

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys("123123")      #确认密码

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()      #下一步

time.sleep(1)       #等待1s

driver.find_element_by_xpath("//*[@id='valid_age']").send_keys("20")        #年龄

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys("女")      #性别

driver.find_element_by_xpath("//*[@id='classname']").send_keys("Python自动化")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()

driver.implicitly_wait(3)

time.sleep(1)

driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys("12306@163.com")

driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys("18698763456")

driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("昌平区")

driver.find_element_by_xpath("//*[@id='btn_reg']").click()

time.sleep(1)

driver.find_element_by_xpath("/html/body/div[2]/div[3]/a/span/span").click()

time.sleep(1)

driver.get("http://localhost:8080/HKR/")

time.sleep(1)

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("wyt")       #登录账户

driver.find_element_by_xpath("//*[@id='password']").send_keys("123123")     #登录密码

driver.find_element_by_xpath("//*[@id='submit']").click()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='img']").click()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='ul_pic']/li[3]/img").click()

driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()

driver.refresh()    #窗口刷新

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys("7(没有晚自习)")

driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys("贾生")

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[5]/td[3]/div/label[1]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[6]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[7]/td[3]/div/label[3]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[8]/td[2]/div/label[1]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[9]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[10]/td[3]/div/label[3]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[11]/td[2]/div/label[1]/div").click()

driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[12]/td[2]/div/label[2]/div").click()

driver.find_element_by_xpath("//*[@id='textarea']").send_keys("みんなさん，こんにちわ，私は王一です，どうぞよろしくお願いいたします。")

driver.find_element_by_xpath("//*[@id='subtn']").click()

time.sleep(2)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a/span/span").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()

time.sleep(1)
ke = Keys       #键盘事件

time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[1]/td[2]/input").send_keys("double")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("admin")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").click()
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='_easyui_textbox_input1']").send_keys("18")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[5]/td[2]/select").send_keys("男")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[6]/td[2]/input").send_keys("北京市")


time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys(Keys.CONTROL,"a")
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[8]/td[2]/input").send_keys("147258369@163.com")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys(" im here")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='btn_modify']").click()

# driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[3]/td[2]/input").send_keys("")


