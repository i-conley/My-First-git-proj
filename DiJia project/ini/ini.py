'''
ini配置文件
简单 直观

[节]
键 = 值

例如：
[section]
key = value

写入方法：手写，程序写入

'''

import configparser

conf = configparser.ConfigParser()
conf.read('./ini_study.ini', encoding= 'UTF-8')

# 查看section
print(conf.sections())

# 查看键
print(conf.options('database'))

# 查看键值对
print(conf.items('database'))


confi = conf.items('database')
for one in confi:
    print(f'键：{one[0]}')
    print(f'键：{one[1]}')

# 判断section是否存在
if conf.has_section('database'):
    print("database 存在")
else:
    print("database9 不import configparser

conf = configparser.ConfigParser()
conf.read('./ini_study.ini', encoding= 'UTF-8')

# 查看section
print(conf.sections())

# 查看键
print(conf.options('database'))

# 查看键值对
print(conf.items('database'))


confi = conf.items('database')
for one in confi:
    print(f'键：{one[0]}')
    print(f'键：{one[1]}')

# 判断section是否存在
if conf.has_section('database'):
    print("database 存在")
else:
    print("database9 不存在")

# 判断option是否存在
if conf.has_option('database','admin'):
    print("admin 存在")
else:
    print("admin 不存在")

# 写入
conf.add_section("电影")
with open('./ini_study.ini', 'w+') as f:
    conf.write(f)存在")

# 判断option是否存在
if conf.has_option('database','admin'):
    print("admin 存在")
else:
    print("admin 不存在")

# 写入
conf.add_section("电影")
with open('./ini_study.ini', 'w+') as f:
    conf.write(f)