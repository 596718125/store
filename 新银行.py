import random
import pymysql
# bank={"123":
#           {"account": 12345678,
#            "password": "123123",
#            "country": "1",
#            "province": "1",
#            "street": "1",
#            "door": "1",
#            "money": 100,
#            "bank_name": "中国工商银行起码路分行"
#            },
#       "张三":
#           {"account": 12121212,
#            "password": "123456",
#            "country": "1",
#            "province": "1",
#            "street": "1",
#            "door": "1",
#            "money": 100,
#            "bank_name": "中国工商银行起码路分行"
#            }
#       }
bank_name = "中国工商银行起码路分行"

def adduser():      #开户
    username=input("请输入您的用户名")      #输入用户名
    password = input("请输入您的密码")     #输入密码
    # 密码判断
    while True:
        if password.isdigit():
            if len(password)!=6 :
                print("密码长度有误，请重新输入")
                password = input("请输入您的密码")
            else:
                break
        else:
            print("输入非法字符，请输入6位数字！")
            password = input("请输入您的密码")

    print("请输入您的地址")                    #输入地址
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    money = input("请输入金额：")
    while True:
        if money.isdigit():
            break
        else:
            print("输入非法，请重新输入！")
            money = input("请输入金额：")

    account=random.randint(10000000, 99999999)
    while True:
        if read(account) == 1 :
            account = random.randint(10000000, 99999999)
        else:
            break

    # while True:
    #     for i in bank:
    #         if bank[i]["account"]==account :
    #             account=random.randint(10000000, 99999999)
    #     else:
    #         break

    status = bank_adduser(account,password,country,province,street,door,money,bank_name,username)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        My = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(My % (username, account, country, province, street, door, money, bank_name))
    elif status==2:
        print("用户名重复，请重新操作！")
    else:
        print("抱歉！当前系统维护，无法进行开户操作。")


def read(a):        #判断账户是否重复
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    sql = "select * from bank where account = %s"
    date = cursor.execute(sql,a)
    if date > 0 :
        cursor.close()
        con.close()
        return 1
    else:
        cursor.close()
        con.close()
        return 0


def bank_adduser(account,password,country,province,street,door,money,bank_name,username):     #添加账户
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    sql_1 = "select count(*) from bank "
    data1 = cursor.execute(sql_1)
    if  data1 > 100 :
        cursor.close()
        con.close()
        return 3

    sql2 = "select * from bank where username = %s"
    user = [username]
    date2 = cursor.execute(sql2,user)

    if date2 > 0:
        cursor.close()
        con.close()
        return 2

    sql_3 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    insert = [account,password,country,province,street,door,money,bank_name,username]
    cursor.execute(sql_3,insert)
    con.commit()

    cursor.close()
    con.close()
    # bank[username]={
    #     "account": account,#键：你输入的值account=random.randint(10000000,99999999)
    #     "password": password,# password = input("请输入您的密码")
    #     "country": country,#country = input("\t\t请输入您的国家")
    #     "province": province,
    #     "street": street,
    #     "door": door,
    #     "money":int(money),
    #     "bank_name":bank_name
    # }
    return 1

def takemoney():        #取款
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    while True:
        info = input("请输入账户：")
        sql1 = "select * from bank where account = %s"
        info = [info]
        data = cursor.execute(sql1, info)
        if data > 0:
            pwd = input("请输入密码")
            while True:
                sql2 = "select password from bank where password = %s"
                pwd = [pwd]
                data = cursor.execute(sql2, pwd)
                if data > 0:
                    while True:
                        money = input("请输入取款金额")
                        if money.isdigit():
                            sql3 = "select money from bank where account = %s"
                            slt = [info]
                            cursor.execute(sql3, slt)
                            data = cursor.fetchone()
                            if int(data[0]) < int(money) :
                                print("余额不足，取款失败！")
                                continue
                            else:
                                money = int(money)
                                sql4 = "update bank set money=money - %s where account = %s"
                                take = [money, info]
                                cursor.execute(sql4, take)
                                con.commit()
                                cursor.execute(sql3, slt)
                                data = cursor.fetchone()
                                print("取款成功！余额为：",data[0])
                                cursor.close()
                                con.close()
                                return
                        else:
                            print("输入非法字符，请重新输入！")
                            continue
                else:
                    print("密码输入错误，请重新输入！")
                    pwd = input("请输入密码：")
        else:
            print("账户不存在，请重新输入！")

#     info=int(info)
#     for i in bank:
#         if bank[i]["account"]==info:
#             pwd = input("请输入密码：")
#             while True:
#                 if pwd!=bank[i]["password"]:
#                     print("密码输入错误，请重新输入！")
#                     pwd = input("请输入密码：")
#                 else:
#                     money = input("请输入取款金额：")
#                     money=int(money)
#                     if money > bank[i]["money"]:
#                         print("余额不足，取款失败！")
#                     else:
#                         bank[i]["money"]-=money
#                         print("取款成功！取款：",money,"余额：",bank[i]["money"])
#                         return
#
#     else:
#         print("该账户不存在！")

def savemoney():        #存款
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    while True:
        info = input("请输入账户：")
        sql1 = "select * from bank where account = %s"
        info = [info]
        data = cursor.execute(sql1,info)
        if data > 0 :
            pwd = input("请输入密码")
            while True:
                sql2 = "select password from bank where password = %s"
                pwd = [pwd]
                data = cursor.execute(sql2, pwd)
                if data > 0:
                    while True:
                        money = input("请输入存款金额")
                        if money.isdigit():
                            sql3 = "update bank set money=money + %s where account = %s"
                            money = int(money)
                            save = [money,info]
                            cursor.execute(sql3, save)
                            con.commit()
                            cursor.close()
                            con.close()
                            return
                        else:
                            print("输入非法字符，请重新输入！")
                            continue
                else:
                    print("密码输入错误，请重新输入！")
                    pwd = input("请输入密码：")
        else:
            print("账户不存在，请重新输入！")

    # for i in bank:
    #     if bank[i]["account"] == int(info):
    #         pwd = input("请输入密码：")
    #         while True:
    #             if pwd != bank[i]["password"]:
    #                 print("密码输入错误，请重新输入！")
    #                 pwd = input("请输入密码：")
    #             else:
    #                 money = input("请输入存款金额：")
    #                 money=int(money)
    #                 bank[i]["money"] += money
    #                 print("存款成功！存款：", money, "余额：", bank[i]["money"])
    #                 return
    # else:
    #     print("该账户不存在！")

def transfer():       #转账
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    while True:
        info = input("请输入转出账户：")
        sql1 = "select * from bank where account = %s"
        info = [info]
        data = cursor.execute(sql1, info)
        if data > 0:
            while True:
                pwd = input("请输入密码")
                sql2 = "select password from bank where password = %s"
                pwd = [pwd]
                data = cursor.execute(sql2, pwd)
                if data > 0:
                    while True:
                        account = input("请输入转入账户：")
                        sql3 = "select account from bank where account = %s"
                        fin = [account]
                        data = cursor.execute(sql3, fin)
                        if data > 0 :
                            while True:
                                money = input("请输入转账金额：")
                                if money.isdigit():
                                    sql4 = "select money from bank where account = %s"
                                    cursor.execute(sql4, info)
                                    data = cursor.fetchone()
                                    if int(data[0]) < int(money):
                                        print("余额不足，转账失败！")
                                        continue
                                    else:
                                        money = int(money)
                                        sql5 = "update bank set money=money - %s where account = %s"
                                        take = [money, info]
                                        cursor.execute(sql5,take)
                                        con.commit()
                                        sql6 = "update bank set money=money + %s where account = %s"
                                        save = [money,fin]
                                        cursor.execute(sql6,save)
                                        con.commit()
                                        print("转账成功！转账金额为：", money)
                                        cursor.close()
                                        con.close()
                                        return
                                else:
                                    print("输入非法字符，请重新输入！")
                        else:
                            print("转入账户不存在，请重新输入！")
                else:
                    print("密码错误，请重新输入！")
        else:
            print("账户不存在，请重新输入！")

#     info = input("请输入转出账户：")
#     info = int(info)
#     for i in bank:
#         if bank[i]["account"] == info:
#             pwd = input("请输入密码：")
#             while True:
#                 if pwd != bank[i]["password"]:
#                     print("密码输入错误，请重新输入！")
#                     pwd = input("请输入密码：")
#                 else:
#                     outfo = input("请输入转入账户：")
#                     outfo = int(outfo)
#                     for j in bank:
#                         if bank[j]["account"] == outfo:
#                             while True:
#                                 money = input("请输入转账金额：")
#                                 money = int(money)
#                                 if bank[i]["money"] < money:
#                                     print("余额不足，请输入其他金额！")
#                                 else:
#                                     bank[i]["money"] -= money
#                                     bank[j]["money"] += money
#                                     print("转账成功！转账金额：", money, "余额：", bank[i]["money"])
#                                     return
#     else:
#         print("该账户不存在！")

def select():         #查询
    con = pymysql.connect(host="localhost", user="root", password="", database="company")
    cursor = con.cursor()
    while True:
        info = input("请输入账户：")
        sql1 = "select * from bank where account = %s"
        info = [info]
        data = cursor.execute(sql1, info)
        if data >0 :
            while True:
                pwd = input("请输入密码：")
                sql2 = "select password from bank where password = %s"
                pwd = [pwd]
                data = cursor.execute(sql2, pwd)
                if data > 0 :
                    sql3 = "select * from bank where account = %s"
                    cursor.execute(sql3, info)
                    data = cursor.fetchone()
                    info = '''
                                                    ------------个人信息------------
                                                    用户名:%s
                                                    账号：%s
                                                    密码：*****
                                                    国籍：%s
                                                    省份：%s
                                                    街道：%s
                                                    门牌号：%s
                                                    余额：%s
                                                    开户行名称：%s
                                                '''
                    print(info % (data[8], data[0], data[2], data[3], data[4],data[5],data[6], data[7]))
                    cursor.close()
                    con.close()
                    return
                else:
                    print("密码错误，请重新输入！")
        else:
            print("账户不存在，请重新输入！")
#     info = input("请输入账户：")
#     info = int(info)
#     for i in bank:
#         if bank[i]["account"] == info:
#             pwd = input("请输入密码：")
#             while True:
#                 if pwd != bank[i]["password"]:
#                     print("密码输入错误，请重新输入！")
#                     pwd = input("请输入密码：")
#                 else:
#                     # print("---------------个人信息---------------")
#                     # print("\t\t用户名:",i)
#                     # print("\t\t账号：", bank[i]["account"])
#                     # print("\t\t密码：*****")
#                     # print("\t\t国籍：", bank[i]["country"])
#                     # print("\t\t省份：", bank[i]["province"])
#                     # print("\t\t街道：", bank[i]["street"])
#                     # print("\t\t门牌号：", bank[i]["door"])
#                     # print("\t\t余额：",bank[i]["money"])
#                     # print("\t\t开户行名称：", bank[i]["bank_name"])
#                     # print("------------------------------------")
#                     info = '''
#                                         ------------个人信息------------
#                                         用户名:%s
#                                         账号：%s
#                                         密码：*****
#                                         国籍：%s
#                                         省份：%s
#                                         街道：%s
#                                         门牌号：%s
#                                         余额：%s
#                                         开户行名称：%s
#                                     '''
#                     # 每个元素都可传入%
#                     print(info % (i , bank[i]["account"],bank[i]["country"], bank[i]["province"], bank[i]["street"], bank[i]["door"], bank[i]["money"], bank[i]["bank_name"]))
#                     return
#     else:
#         print("该账户不存在！")

while True:
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、存钱              ------------|")
    print("|------------3、取钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、存钱")
        savemoney()
    elif  begin == "3":
        print("3、取钱")
        takemoney()
    elif  begin == "4":
        print("4、转账")
        transfer()
    elif  begin == "5":
        print("5、查询 ")
        select()
    elif  begin == "6":
        print("6、退出")
        break
    else:
        print("非法输入，请重新输入！")