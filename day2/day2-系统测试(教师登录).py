from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

driver.implicitly_wait(2)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()

time.sleep(1)

driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")

driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='submit']").click()

driver.implicitly_wait(2)

driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("贾生")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='search_user']/span").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_12']/span[4]/a").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']/span[4]/a").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("英语")

time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("English is good")

time.sleep(1)
driver.find_element_by_xpath("/html/body/div[9]/div[3]/a[1]/span/span[1]").click()

time.sleep(1)
driver.find_element_by_xpath("/html/body/div[12]/div[3]/a/span").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_15']/span[4]/a").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_16']/span[4]/a").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']/span[4]/a").click()

time.sleep(2)

driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]").click()