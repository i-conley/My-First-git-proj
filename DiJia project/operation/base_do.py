"""
    封装操作行为
"""
from selenium import webdriver
from time import sleep


class Base():
    #初始化属性
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # 打开地址
    def open(self, url):
        self.driver.get(url)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 强制等待
    def sleep(self, time_):
        sleep(time_)

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 关闭当前页面
    def close(self):
        self.driver.close()
