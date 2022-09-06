import unittest
from time import sleep
from selenium import webdriver

from page_object.index_page import IndexPage
from page_object.ledgerprocessing_page import LedgerProcessing
from page_object.login_page import LoginPage


class BasicFlow(unittest.TestCase):
    # 用例前置：打开谷歌浏览器驱动
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)
        cls.lpp = LedgerProcessing(cls.driver)

    # 用例后置：关闭浏览器驱动
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录页
    def test_login_01(self):
        """登录页"""
        self.lp.login('http://10.40.0.108:8888/CeShi/#/login', '陈智康', 'gh001#GHOOI', '1')
        self.assertTrue(self.lp.check_login())

    def test_taizhanglist_02(self):
        """台账列表新建台账"""
        self.ip.taizhang_list()
        self.assertTrue(self.ip.check_index())

    def test_taizhanglist_03(self):
        """用例编号id-1"""
        # 输入两个参数，第一个：宗地面积，第二个：容积率
        self.lpp.calculation1('10000', '1')
        # 输入第一个参数，参数为：宗地建筑面积字段的预期结果值；验证自动计算的值是否正确
        self.assertEqual('10000', self.lpp.result)

    def test_taizhanglist_04(self):
        """用例编号id-2"""
        # 输入两个参数，第一个：宗地面积，第二个：宗地建筑面积
        self.lpp.calculation2('20000', '4000')
        # self.lpp.calculation2()
        # 输入第一个参数，参数为：容积率字段的预期结果值；验证自动计算的值是否正确
        self.assertEqual('0.2', self.lpp.result)

    def test_taizhanglist_05(self):
        """用例编号id-3"""
        # 输入两个参数，第一个：宗地建筑面积，第二个：容积率
        self.lpp.calculation3('10000', '10000', '100', '1000', '10000')
        # self.lpp.calculation2()
        # 输入第一个参数，参数为：容积率字段的预期结果值；验证自动计算的值是否正确
        self.assertEqual('100', self.lpp.result)
        self.assertEqual('1000', self.lpp.result1)
        self.assertEqual('10000', self.lpp.result2)

    def test_taizhanglist_06(self):
        """用例编号id-4"""
        self.lpp.calculation4('100000', '400000', '1', '2', '3')
        self.assertEqual('100000', self.lpp.result)
        self.assertEqual('200000', self.lpp.result1)
        self.assertEqual('300000', self.lpp.result2)

    def test_taizhanglist_07(self):
        """用例编号id-5"""
        self.lpp.calculation5('100', '100', '1', '10000', '100000', '1000000')
        self.assertEqual('100', self.lpp.result)
        self.assertEqual('1000', self.lpp.result1)
        self.assertEqual('10000', self.lpp.result2)

    def test_taizhanglist_08(self):
        """用例编号id-6"""
        self.lpp.control1()
        self.assertEqual('true', self.lpp.result)
        self.assertEqual('true', self.lpp.result1)

    def test_taizhanglist_09(self):
        """用例编号id-7"""
        self.lpp.control2()
        self.assertEqual('true', self.lpp.result)
        self.assertEqual('true', self.lpp.result1)

    def test_taizhanglist_10(self):
        """用例编号id-8"""
        self.lpp.control3()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_11(self):
        """用例编号id-9"""
        self.lpp.control4()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_12(self):
        """用例编号id-10"""
        self.lpp.control5()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_13(self):
        """用例编号id-11"""
        self.lpp.control6()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_14(self):
        """用例编号id-14"""
        self.lpp.control7()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_15(self):
        """用例编号id-12"""
        self.lpp.control8()
        self.assertEqual('true', self.lpp.result)

    def test_taizhanglist_16(self):
        """用例编号id-13"""
        self.lpp.control9()
        self.assertEqual('true', self.lpp.result)
        self.assertEqual('true', self.lpp.result1)
        self.assertEqual('true', self.lpp.result2)

    def test_taizhanglist_17(self):
        """用例编号id-15"""
        self.lpp.control10()
        self.assertTrue(self.lpp.check_contro10())

    def test_taizhanglist_18(self):
        """用例编号id-16"""
        self.lpp.control11()
        self.assertTrue(self.lpp.check_contro11())

    def test_taizhanglist_19(self):
        """用例编号id-17"""
        self.lpp.control12()
        self.assertTrue(self.lpp.check_contro12())

    def test_taizhanglist_20(self):
        """用例编号id-18"""
        self.lpp.control13()
        self.assertTrue(self.lpp.check_control13())

    def test_taizhanglist_21(self):
        """用例编号id-19"""
        self.assertTrue(self.lpp.check_control14())

    def test_taizhanglist_22(self):
        """用例编号id-20"""
        self.lpp.control15()
        self.assertTrue(self.lpp.check_control15())

    def test_taizhanglist_23(self):
        """用例编号id-21"""
        self.lpp.control16()
        self.assertTrue(self.lpp.check_control16())

    def test_taizhanglist_24(self):
        """用例编号id-22"""
        self.lpp.control17()
        self.assertTrue(self.lpp.check_control17())

    def test_taizhanglist_25(self):
        """用例编号id-23"""
        self.lpp.control18()
        self.assertTrue(self.lpp.check_control18())

    def test_taizhanglist_26(self):
        """用例编号id-24"""
        self.lpp.check_control19()
        self.assertEqual('true', self.lpp.result)
        self.assertEqual('true', self.lpp.result1)
        self.assertEqual('true', self.lpp.result2)
        self.assertEqual('true', self.lpp.result3)

    def test_taizhanglist_27(self):
        """用例编号id-25"""
        self.lpp.control20()
        self.assertTrue(self.lpp.check_control20())

    def test_taizhanglist_28(self):
        """用例编号id-26"""
        self.lpp.control21()
        self.assertTrue(self.lpp.check_control21())
if __name__ == '__main__':
    unittest.main()
