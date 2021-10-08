from selenium import webdriver
import time

driver = webdriver.Chrome()     #打开谷歌驱动

driver.get("http://www.jd.com")     #打开京东网站

driver.maximize_window()        #窗口最大化

driver.find_element_by_xpath("//*[@id='key']").send_keys("G15")     #搜索 G15

driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()     #点击搜索

time.sleep(5)       #等待5秒

driver.find_element_by_xpath("//*[@title='戴尔（DELL）']").click()      #选择品牌：戴尔（DELL）

driver.find_element_by_xpath("//*[@src='//img10.360buyimg.com/n7/jfs/t1/43226/15/16406/189210/60ee8aaaE16b9181c/997ea383190fef37.jpg']").click()
#点击下侧列表中的链接图片

handles=driver.window_handles   #  获取窗口数量

driver.switch_to.window(handles[1])     #切换第二个窗口

driver.find_element_by_xpath("//*[@clstag='shangpin|keycount|product|picvideo']").click()       #点击新弹窗中的播放

time.sleep(10)       #等待10秒

driver.quit()   # 关闭浏览器