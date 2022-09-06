import xlrd
import openpyxl


class ExcelCase:

    # 解析参数字符串
    def unpark_date(self, value): # 原数据为 'user=admin;pwd=gh001#GHOOI'
        data = {}
        # 第一次拆分参数
        str_temp = value.split(";")  # 拆分为['user=admin'，'pwd=gh001#GHOOI']
        print(str_temp)
        # 第二次拆分参数  遍历sre_temp，把元素逐个细拆
        for temp in str_temp:  # temp = ['user=admin']
            one_para = temp.split("=")   # 拆分为['user','admin']    ['pwd','gh001#GHOOI']
            data[one_para[0]] = one_para[1]   # 组键值对，data['user'] = 'admin' 变成 data['user':'admin']
        return data

    # 运行测试用例文件
    def run(self, file):
        # 读入excel文件
        excel = openpyxl.load_workbook(file)
        # excel = xlrd.open_workbook(file)

        # 遍历sheet页
        for name in excel.sheetnames:
            # 处理一个单独的sheet页
            sheet = excel[name]
            print(sheet)

            # 遍历每一行数据
            for value in sheet.values:
                print(value)

                # 如果编号列数据类型为整数
                if type(value[0]) is int:
                    print("参数", value[2])

                    print(f"处理关键字{value[1]}--------------")
                    if value[2]:
                        para = self.unpark_date(value[2])
                        print(f"解析结果\n{para}")
                    print(f"处理关键字{value[1]}结束--------------")


if __name__ == '__main__':
    file_name = "./case_excel.xlsx"
    ExcelCase().run(file_name)
