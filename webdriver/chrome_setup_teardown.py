from selenium import webdriver
import unittest  # 第一步引入一个unittest
import time


class Search(unittest.TestCase):  # 第二步创建继承一个unittest.TestCase的类

    def setUp(self):  # 第三步定义一个setup，放一些准备的工作，或者准备一些测试数据。
        print('========== 测试开始 ==========')
        self.driver = webdriver.Chrome()  # 加载chrome驱动
        self.driver.maximize_window()  # 放大浏览器
        self.driver.get("https://www.baidu.com")  # 打开网址
        print(self.driver.title)  # 获取标题头并打印出来
        print(self.driver.current_url)  # 获取当前页面的url
        time.sleep(2)  # 休眠5s

    def test_001(self):  # 进行搜索
        self.driver.find_element_by_id('kw').send_keys("Pytest")  # 输入账号
        self.driver.find_element_by_id('su').click()  # 点击搜索
        time.sleep(2)
        print(u'进入高圆圆的搜索结果页')

    def test_002(self):  # 进行搜索
        self.driver.find_element_by_id('kw').send_keys("Jmeter")  # 输入账号
        self.driver.find_element_by_id('su').click()  # 点击搜索
        time.sleep(2)
        print(u'进入张天爱的搜索结果页')

    def tearDown(self):  # 第三步：定义一个tearDown，当我在测试完的时候我要对测试有一个销毁的过程比如说关闭浏览器，那么我们就写在tearDown当中
        self.driver.quit()
        print('========== 测试结束 ==========\n')


if __name__ == '__main__':  # 如果其他的类调用的这个类的时候他就会自动忽略掉这个函数，他是为了测试自身的类用的
    unittest.main()  # 启动程序