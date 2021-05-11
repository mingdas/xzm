# encodings = utf-8
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
# Chrome浏览器可执行文件的地址
options.brinary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# 浏览器驱动：chromedriver的下载地址
chrome_driver_brinary = "/Python/chromedriver"
driver = webdriver.Chrome(chrome_driver_brinary, chrome_options=options)
# 要测试的网页，打开网页
driver.get("http://www.baidu.com")
sleep(3)
# 找到id为"id"的控件, 输入测试文本：Test search
driver.find_element_by_id("kw").send_keys("Test search")
# 找到id为"su"的控件, 模拟鼠标执行点击
driver.find_element_by_id("su").click()
sleep(3)
# 推出浏览器
driver.quit()