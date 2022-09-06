"""
    登录页
"""
from operation.base_do import Base
from selenium import webdriver
import unittest


class LoginPage(Base):
    # url = 'http://10.40.0.108:8888/CeShi/#/login'
    username = ('name', 'username')
    password = ('name', 'password')
    vcode = ('id', 'vcode')
    button_el = ('xpath', '//*[@id="app"]/div/form/div[2]/button')

    def login(self, url, user, pwd, vcode):
        self.open(url)
        self.input(*self.username, user)
        self.input(*self.password, pwd)
        self.input(*self.vcode, vcode)
        #self.sleep(5)
        self.click(*self.button_el)

    def check_login(self):
        """元素是否存在"""
        try:
            self.driver.find_element('xpath',
                                     '//span[@title="测试表单台账"]').is_displayed()
        except Exception:
            return False
        return True


if __name__ == "__main__":
    lp = LoginPage(webdriver.Chrome())
    lp.login('http://10.40.0.108:8888/CeShi/#/login', '陈智康', 'gh001#GHOOI', '1')
