from selenium import webdriver
import unittest
from ddt import ddt, unpack, file_data
from time import sleep


@ddt
class test_text(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://10.40.0.108:8888/CeShi/#/login")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    @file_data('./data/data1.yaml')
    def test_login(self, **parse):
        self.driver.find_element('name', 'username').send_keys(parse["用户名"])
        self.driver.find_element('name', 'password').send_keys(parse["密码"])
        self.driver.find_element('id', 'vcode').send_keys(parse["验证码"])
        self.driver.find_element('xpath', '//button/span[text()="登录"]').click()
        sleep(4)


if __name__ == '__main__':
    unittest.main()
