'''
    进入台账列表新建台账
'''

from selenium import webdriver
from operation.base_do import Base


class IndexPage(Base):
    oa_el1 = ('xpath', '//span[@title="测试表单台账"]')
    # oa_el2 = ('xpath', '//*[@id="app-wrapper"]/div[1]/div[1]/div/ul/div[8]/li/ul/div/a/li/span')
    oa_el2 = ('xpath', '//li/span[text()="测试表单台账"]')
    oa_el3 = ('xpath', '//span[text()="新建"]')
    oa_el4 = ('xpath',
              '//*[@id="app-wrapper"]/div[2]/section/section/section/main/div[1]/div/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/div/button[1]/span')
    oa_el5 = ('xpath', '//*[@id="app-wrapper"]/div[2]/section/section[2]/div[1]/div/div[1]/button/span')



    def taizhang_list(self):
        self.click(*self.oa_el1)
        self.sleep(1)
        self.click(*self.oa_el2)
        self.sleep(1)
        self.click(*self.oa_el3)
        self.sleep(5)



    def check_index(self):
        """元素是否存在"""
        try:
            self.driver.find_element('xpath',
                                     '//*[@id="app-wrapper"]/div[2]/section/section[2]/div[1]/div/div[1]/button/span').is_displayed()
        except Exception:
            return False
        return True