import unittest

from BeautifulReport import BeautifulReport

# 收集测试用例
# suite = unittest.defaultTestLoader.discover(r'/Users/kang/PycharmProjects/ZD-CWBX/case')
from case.case import BasicFlow

testcases = unittest.TestLoader().loadTestsFromTestCase(BasicFlow)
# 执行测试用例
bf = BeautifulReport(testcases)
bf.report(description="地价表单控件联动的用例",
          filename='DiJiarp.html',
          report_dir=r'/Users/kang/PycharmProjects/DiJia project/reports'
          )
