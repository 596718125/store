'''
    xlrd:读取
    xlwt:写入
    xlrd:0.9.3版本
    xlwt:

    python -m  pip install   xlrd==0.9.3

    1.步骤
    1.打开工作簿
    2.找到你想操作的选项卡
    3.通过坐标读取数据
任务1：
    把2020年的所有数据统计分析并打印出来
任务2：
    把excel表的所有数据存储到数据库。
任务3：
    将三国集团数据，导出到excel里。
'''
import xlrd
import xlwt
import pymysql

#1.打开
wb = xlrd.open_workbook(filename=r"D:\Python自动化测试\专题项目\ptyhon\day8【xlrd】\资料\2020年每个月的销售情况.xlsx")
#月份(全局)
moon = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
#全年的销售总额
def sum():
    sum = 0
    for i in range(0,12):
        sheet = wb.sheet_by_name(moon[i])
        rows = sheet.nrows
        num = 0
        for j in range(1,rows):
            data = sheet.row_values(j)
            sum += data[2] * data[4]
            num += data[2] * data[4]
        print(moon[i],"销售总额：￥",round(num,2))
    print("全年销售总额：￥",round(sum,2))
    return


# 每件衣服的销售（件数）占比
def list():
    cls = {}
    for i in range(0,12):
        sheet = wb.sheet_by_name(moon[i])
        rows = sheet.nrows
        for j in range(1,rows):
            data_1 = sheet.row_values(j)
            a = data_1[1]
            b = data_1[4]
            if a in cls:
                cls[a] = cls[a] + b
            else:
                cls[a] = b
    sum = 0
    for i in cls:
        sum += cls[i]
    num = 0
    for i in cls:
        print(i,"年销售（件数）占比：",round(cls[i]/sum*100,1),"%")
    return


# 每件衣服的月销售（件数）占比
def Moon_list():
    for i in range(0,12):
        cls = {}
        sheet = wb.sheet_by_name(moon[i])
        rows = sheet.nrows
        for j in range(1,rows):
            data_1 = sheet.row_values(j)
            a = data_1[1]
            b = data_1[4]
            if a in cls:
                cls[a] = cls[a] + b
            else:
                cls[a] = b
        sum = 0
        for k in cls:
            sum += cls[k]

        num = 0
        print("----------",moon[i],"----------")
        for n in cls:
            print(n, "销售（件数）占比：", round(cls[n] / sum * 100, 1), "%")
        print()
    return


# 每件衣服的销售额占比（价格）
def money_list():
    for i in range(0,12):
        cls = {}
        sheet = wb.sheet_by_name(moon[i])
        rows = sheet.nrows
        for j in range(1,rows):
            data_1 = sheet.row_values(j)
            a = data_1[1]
            b = data_1[4] * data_1[2]
            if a in cls:
                cls[a] = cls[a] + b
            else:
                cls[a] = b
        sum = 0
        for k in cls:
            sum += cls[k]
        num = 0
        print("----------",moon[i],"----------")
        for n in cls:
            print(n, "销售额占比：", round(cls[n] / sum * 100, 1), "%")
        print()
    return
# 最畅销的衣服是那种
def year_max():
    print("年销量最高的衣服是：",qt(moon))

# 每个季度最畅销的衣服
def quarter():
    quarter_1 = ["2月","3月","4月"]        #第一季度
    quarter_2 = ["5月","6月","7月"]        #第二季度
    quarter_3 = ["8月","9月","10月"]       #第三季度
    quarter_4 = ["1月","11月","12月"]      #第四季度
    print("第一季度销量最高的衣服是：",qt(quarter_1))
    print("第二季度销量最高的衣服是：",qt(quarter_2))
    print("第三季度销量最高的衣服是：",qt(quarter_3))
    print("第四季度销量最高的衣服是：",qt(quarter_4))
    return

def qt(a):
    cls = {}
    for i in a:
        sheet = wb.sheet_by_name(i)
        rows = sheet.nrows
        for j in range(1,rows):
            data = sheet.row_values(j)
            x = data[1]
            y = data[4]
            if x in cls:
                cls[x] = cls[x] + y
            else:
                cls[x] = y
    sum = 0
    for k in cls:
        sum += cls[k]
    max = 0
    for l in cls:
        if cls[l] >= max:
            max = cls[l]
            clothes = l
    return clothes


# 全年销量最低的衣服
def year_min():
    cls = {}
    for i in range(0,12):
        sheet = wb.sheet_by_name(moon[i])
        rows = sheet.nrows
        for j in range(1,rows):
            data_1 = sheet.row_values(j)
            a = data_1[1]
            b = data_1[4]
            if a in cls:
                cls[a] = cls[a] + b
            else:
                cls[a] = b
    sum = 0
    for i in cls:
        sum += cls[i]
    min = sum
    for i in cls:
        if cls[i] <= min :
            min = cls[i]
            clothes = i
    print("年销量最低的衣服是：",clothes)
    return

#任务1：
#全年的销售总额
#运行sum()
# 每件衣服的销售（件数）占比
#运行list()
# 每件衣服的月销售（件数）占比
#运行Moon_list()
# 每件衣服的销售额占比（价格）
#执行money_list()
# 最畅销的衣服是那种
#运行year_max()
# 每个季度最畅销的衣服
#运行quarter()
# 全年销量最低的衣服
#运行year_min()






















