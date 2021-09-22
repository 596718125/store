# 任务3：将三国集团数据，导出到excel里。
import pymysql
import os
import xlrd
import xlwt

class DB_Excel_Utils:
    def __init__(self):
        self.con = pymysql.connect(host="localhost",user="root",password="",database="三国创业")
        self.cursor = self.con.cursor()

    #  数据库转换成excel表
    def DB_to_Excel(self,table="",filename=""):
        if filename.endswith(".xlsx") or filename.endswith(".xls"): # 判断文件是否是以xlsx或者xls结尾
            self.wb = xlwt.Workbook()
            self.st = self.wb.add_sheet(table)
        # 获取所有字段名
        sql = '''select * from %s''' % (table)
        self.cursor.execute(sql, [])
        # 将所有表头提取出来
        names = []
        for cu in self.cursor.description:
            names.append(cu[0])

        # 将所有数据提取出来
        data = self.cursor.fetchall()

        # 写入excel表格
        # 1.先写表头
        index = 0
        for j,value in enumerate(names):
            self.st.write(index,j,value)

        # 2.写数据
        for i,value in enumerate(data):
            index = index + 1
            for v_k,v_v in enumerate(value):
                self.st.write(index,v_k,v_v)

        # 3.保存数据
        self.wb.save(filename)

    # 公共的拼接sql的方法
    def concatSql(self,sql1,names):
        # 将表头拼接到sql1语句里 : 形成 values(%s,%s,%s.....)
        for i in range(len(names)):
            if i == len(names) - 1:
                sql1 = sql1 + "%s)"
                break
            else:
                sql1 = sql1 + "%s, "
        return sql1


utils = DB_Excel_Utils()
# utils.Excel_to_DB(filename="data.xlsx",sheet="0")

utils.DB_to_Excel(filename="三国创业.xlsx",table="t_employees")