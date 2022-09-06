# from selenium import webdriver
# from time import sleep
#
#
# def HighLight(driver, element):
#     # 封装好的高亮显示页面元素的方法
#     # 使用JavaScript代码将传入的页面元素对象的边框颜色
#     # 3次循环，边框颜色先蓝后红中间各停留1秒，产生闪烁效果
#     for i in range(0, 3):
#         driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
#                               element, "border:2px solid blue;")
#         sleep(1)
#         driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
#                               element, "border:2px solid red;")
#         sleep(1)
#     # 恢复页面元素原装
#     driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",
#                           element, "")
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get("https://www.baidu.com/")
# input_search = driver.find_element('id','kw')
# HighLight(driver, input_search)
# input_search.send_keys('测试123')
# btn_go = driver.find_element('id', 'su')
# HighLight(driver, btn_go)
# sleep(10)
# btn_go.click()
# sleep(5)
# driver.quit()

data={}
para =['user', '123456']
data[para[0]] = para[1]

print(data)