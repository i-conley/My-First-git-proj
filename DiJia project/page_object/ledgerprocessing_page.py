'''
    进入台账列表新建台账
'''
from operation.base_do import Base
from selenium.webdriver.common.keys import Keys


class LedgerProcessing(Base):
    # 宗地面积字段
    zdmj = ('xpath', '//div[@name="input_宗地面积"]/div/div/div/input')

    # 宗地建筑面积字段
    zdjzmj = ('xpath', '//div[@name="input_宗地建筑面积"]/div/div/div/input')

    # 容积率
    rjl = ('xpath', '//div[@name="input_容积率"]/div/div/div/input')

    # 联动的计算结果
    result = None
    result1 = None
    result2 = None
    result3 = None

    # 是否违约 字段
    sfwy = ('xpath', '//*[@id="1647500896000_94011"]/div/div[2]/div[1]/div/div/div/div/input')
    # 选择 否
    fou = ('xpath', '//li//span[text() = "否"]')
    # 选择 是
    shi = ('xpath', '//li//span[text() = "是"]')

    # 违约日期
    wyrq = ('xpath', '//*[@id="1647500896000_94011"]/div/div[2]/div[2]/div/div/div/input')
    # 表中表的 新增行 按钮
    xzh = ('xpath', '//*[@id="ghTable1647500993000_4232"]/div[4]/div[1]/table/thead/tr/th[4]/div/button/span')
    # 新增行后点击 确认
    xzh_qr = ('xpath', '//*[@id="1647500993000_4232"]/div/div[3]/div/button[2]/span')

    # 勾选商服
    shangfu = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[1]/span[1]')
    # 商服文本框
    shangfutxt = ('xpath', '//*[@id="1647502714000_18888"]/div/div[2]/div[1]/div/div/div/div[2]/input')
    # 勾选住宅
    zhuzhai = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[2]/span[1]/span')
    # 住宅文本框
    zhuzhaitxt = ('xpath', '//*[@id="1647502977000_88910"]/div/div[2]/div[1]/div/div/div/div[2]/input')
    # 勾选工业
    gongye = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[3]/span[1]/span')
    # 工业文本框
    gongyetxt = ('xpath', '//*[@id="1647502988000_62369"]/div/div[2]/div[1]/div/div/div/div[2]/input')
    # 获取勾选框的是否选中
    checkbook1 = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[1]/span[1]')
    checkbook2 = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[2]/span[1]')
    checkbook3 = ('xpath', '//*[@id="1647502695000_16990"]/div/div/div/div/div/div/label[3]/span[1]')

    # 【附件】
    fujian = ('xpath', '//*[@id="app-wrapper"]/div[2]/section/section[2]/section/div/div[1]/div[3]/i')
    # 勾选商服显示表单
    shangfubd = ('xpath', '//*[@id="1647501933000_28064"]/div/div[2]/div/div/div/div/label[1]/span[1]/span')
    shangfubdxs = ('xpath',
                   '//span//span[@title = "测试表单显示_商服（勿删）"]')
    # 勾选住宅显示表单
    zhuzhaibd = ('xpath', '//*[@id="1647501933000_28064"]/div/div[2]/div/div/div/div/label[2]/span[1]/span')
    zhuzhaibdxs = ('xpath', '//span//span[@title = "测试表单显示_住宅（勿删）"]')

    # 勾选办工显示表单
    bangongbd = ('xpath', '//*[@id="1647501933000_28064"]/div/div[2]/div/div/div/div/label[3]/span[1]/span')
    bangongbdxs = ('xpath', '//span//span[@title = "测试表单显示_办公（勿删）"]')

    # 勾选工业显示表单
    gongyebd = ('xpath', '//*[@id="1647501933000_28064"]/div/div[2]/div/div/div/div/label[4]/span[1]/span')
    gongyebdxs = ('xpath', '//span//span[@title = "测试表单显示_工业（勿删）"]')

    # 勾选商服，结果一览表单显示计算结果
    shangfujs = ('xpath', '//*[@id="1647590729000_60285"]/div/div[2]/div/div/div/div/label[1]/span[1]/span')
    jgylbd = ('xpath', '//span//span[@title = "测试结果一览（勿删）"]')
    # 结果一览表中表新增行按钮
    jgylbzb = ('xpath', '//*[@id="ghTable1647592046000_23794"]/div[4]/div[1]/table/thead/tr/th[3]/div/button')
    csbd = ('xpath',
            '//*[@id="app-wrapper"]/div[2]/section/section[2]/section/div/div[1]/div[4]/aside/div[2]/div[1]/div[1]/span[2]/span')

    # 点击【附件】
    def fujianclick(self):
        self.click(*self.fujian)

    def cleartxt(self):
        # 清空文本框
        self.locate(*self.rjl).clear()
        self.locate(*self.zdmj).clear()
        self.locate(*self.zdjzmj).clear()

    def gouxuan(self):
        self.click(*self.shangfu)
        self.sleep(1)
        self.click(*self.zhuzhai)
        self.sleep(1)
        self.click(*self.gongye)
        self.sleep(1)

    # 计算公式 用例编号id-1
    def calculation1(self, txt1, txt2):
        try:
            self.input(*self.zdmj, txt1)
            self.input(*self.rjl, txt2)
            # self.click(*self.zdjzmj)
            self.sleep(1)
            self.input(*self.rjl, Keys.ENTER)
            self.sleep(1)
            self.result = self.locate(*self.zdjzmj).get_attribute('value')
            # self.sleep(1)
            self.cleartxt()

            self.sleep(1)
        except:
            print('用例执行失败')

    # 计算公式 用例编号id-2
    def calculation2(self, txt3, txt4):
        try:
            self.input(*self.zdmj, txt3)
            self.sleep(1)
            self.input(*self.zdmj, Keys.ENTER)
            self.sleep(1)
            self.locate(*self.zdjzmj).clear()
            self.sleep(2)
            self.input(*self.zdjzmj, txt4)
            self.input(*self.zdjzmj, Keys.ENTER)
            self.sleep(1)
            self.result = self.locate(*self.rjl).get_attribute('value')

            self.cleartxt()
            self.sleep(1)
        except:
            print('用例执行失败')

    # 计算公式 用例编号id-3
    def calculation3(self, txt1, txt2, txt4, txt5, txt6):
        self.input(*self.zdmj, txt1)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt2)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.zdmj).clear()
        self.sleep(1)
        self.input(*self.zdmj, txt4)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.result = self.locate(*self.zdjzmj).get_attribute('value')
        self.sleep(1)
        self.locate(*self.zdmj).clear()
        self.sleep(1)
        self.input(*self.zdmj, txt5)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.result1 = self.locate(*self.zdjzmj).get_attribute('value')
        self.sleep(1)
        self.locate(*self.zdmj).clear()
        self.sleep(1)
        self.input(*self.zdmj, txt6)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.result2 = self.locate(*self.zdjzmj).get_attribute('value')

    # 计算公式 用例编号id-4
    def calculation4(self, txt1, txt2, txt3, txt4, txt5):
        self.cleartxt()
        self.sleep(1)
        self.input(*self.zdmj, txt1)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt2)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.rjl).clear()
        self.sleep(1)
        self.input(*self.rjl, txt3)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result = self.locate(*self.zdjzmj).get_attribute('value')
        self.sleep(1)
        self.locate(*self.rjl).clear()
        self.sleep(1)
        self.input(*self.rjl, txt4)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result1 = self.locate(*self.zdjzmj).get_attribute('value')
        self.locate(*self.rjl).clear()
        self.sleep(1)
        self.input(*self.rjl, txt5)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result2 = self.locate(*self.zdjzmj).get_attribute('value')

    # 计算公式 用例编号id-5
    def calculation5(self, txt1, txt2, txt3, txt4, txt5, txt6):
        self.cleartxt()
        self.sleep(1)
        self.input(*self.zdmj, txt1)
        self.sleep(1)
        self.input(*self.zdmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt2)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.rjl).clear()
        self.sleep(1)
        self.input(*self.rjl, txt3)
        self.sleep(1)
        self.input(*self.rjl, Keys.ENTER)
        self.sleep(1)
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt4)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result = self.locate(*self.rjl).get_attribute('value')
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt5)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result1 = self.locate(*self.rjl).get_attribute('value')
        self.locate(*self.zdjzmj).clear()
        self.sleep(1)
        self.input(*self.zdjzmj, txt6)
        self.sleep(1)
        self.input(*self.zdjzmj, Keys.ENTER)
        self.sleep(1)
        self.result2 = self.locate(*self.rjl).get_attribute('value')

    # 控件联动 用例编号id-6
    def control1(self):
        self.click(*self.sfwy)
        self.sleep(1)
        self.click(*self.fou)
        self.sleep(1)
        self.result = self.locate(*self.wyrq).get_attribute('disabled')
        self.sleep(1)
        try:
            self.click(*self.xzh)
            self.result1 = "false"
        except:
            self.result1 = "true"

    # 控件联动 用例编号id-7
    def control2(self):
        self.click(*self.sfwy)
        self.sleep(1)
        self.click(*self.shi)
        self.sleep(1)
        try:
            self.input(*self.wyrq, '2022-04-14')
            self.sleep(1)
            self.result = "true"
        except:
            self.result = "false"
        self.sleep(1)
        try:
            self.click(*self.xzh)
            self.sleep(1)
            self.click(*self.xzh_qr)
            self.result1 = "true"
        except:
            self.result1 = "false"
        self.sleep(1)

    # 控件联动 用例编号id-8
    def control3(self):
        try:
            checkstate = 'el-checkbox__input'
            if checkstate == self.locate(*self.checkbook1).get_attribute('class'):
                self.click(*self.shangfu)
                self.sleep(1)
                try:
                    self.input(*self.shangfutxt, '输入商服文本')
                    self.sleep(1)
                    self.result = 'true'
                except:
                    self.result = 'false'
            else:
                self.result = 'false'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-9
    def control4(self):
        try:
            checkstate = 'el-checkbox__input'
            if checkstate == self.locate(*self.checkbook2).get_attribute('class'):
                self.click(*self.zhuzhai)
                self.sleep(1)
                try:
                    self.input(*self.zhuzhaitxt, '输入住宅文本')
                    self.sleep(1)
                    self.result = 'true'
                except:
                    self.result = 'false'
            else:
                self.result = '勾选住宅后，文本框没有显示'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-10
    def control5(self):
        try:
            checkstate = 'el-checkbox__input'
            if checkstate == self.locate(*self.checkbook3).get_attribute('class'):
                self.click(*self.gongye)
                self.sleep(1)
                try:
                    self.input(*self.gongyetxt, '输入工业文本')
                    self.sleep(1)
                    self.result = 'true'
                except:
                    self.result = '勾选工业后，文本框没有显示'
            else:
                self.result = 'false'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-11
    def control6(self):
        # self.gouxuan()
        try:
            checkstate = 'el-checkbox__input is-checked'

            if checkstate == self.locate(*self.checkbook1).get_attribute('class') \
                    and checkstate == self.locate(*self.checkbook2).get_attribute('class') \
                    and checkstate == self.locate(*self.checkbook3).get_attribute('class'):
                # self.click(*self.shangfu)
                # self.sleep(1)
                # self.click(*self.zhuzhai)
                # self.sleep(1)
                # self.click(*self.gongye)
                # self.sleep(1)
                try:
                    self.input(*self.shangfutxt, '输入商服文本')
                    self.input(*self.zhuzhaitxt, '输入住宅文本')
                    self.input(*self.gongyetxt, '输入工业文本')
                    self.sleep(1)
                    self.result = 'true'
                except:
                    self.result = '勾选复选框后，文本框没有显示'
            else:
                self.result = '复选框已经勾选，没达到前置条件'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-14
    def control7(self):
        try:
            checkstate = 'el-checkbox__input is-checked'

            if checkstate == self.locate(*self.checkbook1).get_attribute('class') \
                    and checkstate == self.locate(*self.checkbook2).get_attribute('class') \
                    and checkstate == self.locate(*self.checkbook3).get_attribute('class'):
                self.click(*self.shangfu)
                self.sleep(1)
                self.click(*self.zhuzhai)
                self.sleep(1)
                self.click(*self.gongye)
                self.sleep(1)
                try:
                    self.input(*self.shangfutxt, '输入商服文本')
                    self.input(*self.zhuzhaitxt, '输入住宅文本')
                    self.input(*self.gongyetxt, '输入工业文本')
                    self.sleep(1)
                    self.result = '取消勾选后没有隐藏文本框'
                except:
                    self.result = 'true'
            else:
                self.result = '复选框并未勾选，没达到前置条件'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-12
    def control8(self):
        try:
            checkstate = 'el-checkbox__input'

            if checkstate == self.locate(*self.checkbook1).get_attribute('class'):
                self.click(*self.zhuzhai)
                self.sleep(1)
                try:
                    self.input(*self.zhuzhaitxt, '输入住宅文本')
                    self.sleep(1)
                    self.result = 'true'
                except:
                    self.result = '取消勾选后没有显示住宅文本框'
                self.click(*self.zhuzhai)
                self.sleep(1)
                try:
                    self.input(*self.zhuzhaitxt, '输入住宅文本')
                    self.sleep(1)
                    self.result = '取消勾选后没有隐藏住宅文本框'
                except:
                    self.result = 'true'
            else:
                self.result = '复选框已被勾选，没达到前置条件'
        except:
            print('用例执行失败')

    # 控件联动 用例编号id-13
    def control9(self):
        try:
            self.click(*self.shangfu)
            self.sleep(1)
            self.click(*self.zhuzhai)
            self.sleep(1)
            self.click(*self.gongye)
            self.sleep(1)
            try:
                self.input(*self.shangfutxt, '输入商服文本')
                self.input(*self.zhuzhaitxt, '输入住宅文本')
                self.input(*self.gongyetxt, '输入工业文本')
                self.sleep(1)
                self.result = 'true'
            except:
                self.result = '勾选后文本框没有显示'
            self.click(*self.shangfu)
            self.sleep(1)
            try:
                self.input(*self.shangfutxt, '输入商服文本')
                self.result1 = '取消勾选商服后还显示控件'
            except:
                self.result1 = 'true'
            try:
                self.input(*self.zhuzhaitxt, '输入住宅文本')
                self.input(*self.gongyetxt, '输入工业文本')
                self.result2 = 'true'
            except:
                self.result2 = '取消勾选商服后,住宅和工业输入框无法输入'
        except:
            print('用例执行失败')


    # 控件联动显隐表单 用例编号id-15
    def control10(self):
        try:
            self.click(*self.shangfubd)
            self.sleep(1)
            self.fujianclick()
            self.sleep(1)
        except:
            print('用例执行失败')

    def check_contro10(self):
        try:
            self.driver.find_element(*self.shangfubdxs).is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-16
    def control11(self):
        try:
            self.click(*self.zhuzhaibd)
            self.sleep(1)
        except:
            print('用例执行失败')

    def check_contro11(self):
        try:
            self.driver.find_element(*self.zhuzhaibdxs).is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-17
    def control12(self):
        try:
            self.click(*self.bangongbd)
            self.sleep(1)
        except:
            print('用例执行失败')

    def check_contro12(self):
        try:
            self.driver.find_element(*self.bangongbdxs).is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-18
    def control13(self):
        try:
            self.click(*self.gongyebd)
            self.sleep(1)
        except:
            print('用例执行失败')

    def check_control13(self):
        try:
            self.driver.find_element(*self.gongyebdxs).is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-19
    def check_control14(self):
        try:
            self.driver.find_element(*self.shangfubdxs).is_displayed()
            self.driver.find_element(*self.zhuzhaibdxs).is_displayed()
            self.driver.find_element(*self.bangongbdxs).is_displayed()
            self.driver.find_element(*self.gongyebdxs).is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-20
    def control15(self):
        self.click(*self.shangfubd)
        self.sleep(1)

    def check_control15(self):
        try:
            self.driver.find_element(*self.shangfubdxs).is_displayed()
        except Exception:
            return True
        return False

    # 控件联动显隐表单 用例编号id-21
    def control16(self):
        self.click(*self.zhuzhaibd)
        self.sleep(1)

    def check_control16(self):
        try:
            self.driver.find_element(*self.zhuzhaibdxs).is_displayed()
        except Exception:
            return True
        return False

    # 控件联动显隐表单 用例编号id-22
    def control17(self):
        self.click(*self.bangongbd)
        self.sleep(1)

    def check_control17(self):
        try:
            self.driver.find_element(*self.bangongbdxs).is_displayed()
        except Exception:
            return True
        return False

    # 控件联动显隐表单 用例编号id-23
    def control18(self):
        self.click(*self.gongyebd)
        self.sleep(1)

    def check_control18(self):
        try:
            self.driver.find_element(*self.gongyebdxs).is_displayed()
        except Exception:
            return True
        return False

    # 控件联动显隐表单 用例编号id-24
    def check_control19(self):
        try:
            try:
                self.click(*self.shangfubdxs)
                self.result = 'false'
            except:
                self.result = 'true'

            try:
                self.click(*self.zhuzhaibdxs)
                self.result1 = 'false'
            except:
                self.result1 = 'true'

            try:
                self.click(*self.bangongbdxs)
                self.result2 = 'false'
            except:
                self.result2 = 'true'

            try:
                self.click(*self.gongyebdxs)
                self.result3 = 'false'
            except:
                self.result3 = 'true'
        except Exception:
            self.result = '用例执行失败'

    # 控件联动显隐表单 用例编号id-35
    def control20(self):
        try:
            self.click(*self.shangfujs)
            self.sleep(1)
            self.click(*self.jgylbd)
            self.sleep(5)
        except:
            print('用例执行失败')

    def check_control20(self):
        try:
            self.driver.find_element('xpath',
                                     '//*[@id="ghTable1647592046000_23794"]/div[4]/div[1]/table/thead/tr/th[3]/div/button').is_displayed()
        except Exception:
            return False
        return True

    # 控件联动显隐表单 用例编号id-26
    def control21(self):
        try:
            self.click(*self.csbd)
            self.sleep(2)
            self.click(*self.shangfujs)
            self.sleep(2)
            self.click(*self.jgylbd)
            self.sleep(5)
        except:
            print('用例执行失败')

    def check_control21(self):
        try:
            self.driver.find_element('xpath',
                                     '//*[@id="ghTable1647592046000_23794"]/div[4]/div[1]/table/thead/tr/th[3]/div/button').is_displayed()
        except Exception:
            return True
        return False

# def check_calculation(self):
#     """元素是否存在"""
#     try:
#         self.driver.find_element('xpath',
#                                  '//span[@title="测试表单台账"]').is_displayed()
#     except Exception:
#         return False
#     return True
