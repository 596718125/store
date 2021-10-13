'''
数据类：
    只准备数据，不参与操作
'''
import xlrd

class  InitPage:

    wb = xlrd.open_workbook(r"D:\Python\file\14-自动化\day3-测试报告\Excel版\登录测试用例.xlsx")

    list=["成功","失败"]

    sheet1 = wb.sheet_by_name(list[0])
    rows1 = sheet1.nrows        #行数
    sheet2 = wb.sheet_by_name(list[1])
    rows2 = sheet2.nrows        #行数

    success = []
    error = []

    for i in range(1,rows1):
        ctp = sheet1.cell(i,1).ctype
        no = sheet1.cell(i,1).value
        sheet1_data = sheet1.row_values(i)
        if ctp == 2:
            no = str(int(no))
            sheet1_data[1]=no
        success.append(sheet1_data)

    for j in range(1,rows2):
        ctp =sheet2.cell(j,1).ctype
        no = sheet2.cell(j,1).value
        sheet2_data = sheet2.row_values(j)
        if ctp == 2:
            no = str(int(no))
            sheet2_data[1]=no
        error.append(sheet2_data)

    success
    error

    # login_success_data = [
    #     {"username":"jason","password":"1234567","expect":"Student Login"},
    #     {"username":"不再爱了","password":"1234567","expect":"Student Login"}
    # ]
    # #
    # login_error_data = [
    #     # id : msg_uname
    #     {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "不再爱了", "password": "root", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]





