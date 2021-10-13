import pymysql

class  InitPage:

    con = pymysql.connect(host="localhost" , user="root" , password="" ,database="hkr")
    cursor = con.cursor()

    sql_1 = "select * from data_success"
    sql_2 = "select * from data_error"

    cursor.execute(sql_1)
    data1 = cursor.fetchall()

    cursor.execute(sql_2)
    data2 = cursor.fetchall()

    cursor.close()
    con.close()

