# 任务2：把excel表的所有数据存储到数据库。
def my(sql,param):
    con = pymysql.connect(host="localhost",user="root",password="",database="company")
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
    return

#执行添加到数据库
for i in moon:
    sheet = wb.sheet_by_name(i)
    rows = sheet.nrows
    for j in range(1, rows):
        data = sheet.row_values(j)
        print(data)
        sql = "insert into clothes values(%s,%s,%s,%s,%s,%s)"
        param = [i,data[0],data[1],data[2],data[3],data[4]]
        my(sql, param)
