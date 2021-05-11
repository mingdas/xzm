import pandas as pd
from selenium import webdriver
from time import sleep
def chromeexcel():
    data = pd.read_excel("data.xlsx")
    a = data.iloc[1, 1]
    a = str(a)
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id("kw").send_keys(a)
    driver.find_element_by_id("su").click()
    sleep(2)
    driver.quit()

if __name__ == '__main__':
    chromeexcel()