#dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
'''
for a in (dict):
    print(a)
'''
#2、请循环遍历出所有的value
'''
print()
for a in (dict):
    print(dict[a])
'''
# 3、请在字典中增加一个键值对,"k4":"v4"
'''
print()
dict["k4"]="v4"
print(dict)
'''
#请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用,用水果名称做key，金额做value，创建一个字典
'''
info = {"苹果":32.8,"香蕉": 22,"葡萄: 15.5}
'''
#小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
'''
Friuts = {
	"苹果": 12.3,  # 水果和单价
	"草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}
info = {            #水果和数量
    "小明": {"fruits":{"苹果":4, "草莓":13, "香蕉":10},"money":0},
    "小刚": {"fruits":{"葡萄":19, "橘子":12, "樱桃":30},"money":0}
}
s1 = 0      #小明的总金额
s2 = 0      #小刚的总金额
for i in (Friuts):
    for j in (info["小明"]["fruits"]):
        if i==j :
            num=Friuts[i]*info["小明"]["fruits"][j]
            s1+=num
            info["小明"]["money"]=s1
    for k in (info["小刚"]["fruits"]):
        if i == k:
            num = Friuts[i] * info["小刚"]["fruits"][k]
            s2 += num
            info["小刚"]["money"] = s2

for keys in info:
    print(keys,info[keys])
'''
#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
'''
dict={}
while True:
    a = input("请输入数字：")
    if a=="q" or a=="Q":
        break
    if a.isdigit():
        for i in (dict):        #一个神奇的逻辑 for ~ else
            if i==a:
                dict[i]+=1
                break
        else:
            dict[a]=1
        print(dict)
    else:
        print("输入非数值，请重新输入！")
'''
#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
#       姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = {   #效果
#     "刘备":{"年龄":"56","性别":"男","编号":"106","任职公司":"IBM","薪资":500,"部门编号":"50"},
#     "大乔":{"年龄":"19","性别":"女","编号":"230","任职公司":"微软","薪资":501,"部门编号":"60"},
#     "小乔":{"年龄":"19","性别":"女","编号":"210","任职公司":"Oracle","薪资":600,"部门编号":"60"},
#     "张飞":{"年龄":"45","性别":"男","编号":"230","任职公司":"Tencent","薪资":700,"部门编号":"10"}
# }

dict={}

def name(a):
    for i in dict:
        if i==a:
            age=input("请输入年龄：")     #年龄判断
            while True:
                if age.isdigit():
                    if int(age)>60 or int(age)<=0:
                        print("输入错误，请重新输入(区间1，60)")
                        age = input("请输入年龄：")
                    else:
                        break
                else:
                    print("输入错误，请重新输入(区间1，60)")
                    age = input("请输入年龄：")

            sex=input("请输入性别：")     #性别判断
            while True:
                if sex=="男" or sex=="女":
                    break
                else:
                    print("输入错误，请重新输入(男/女)！")
                    sex = input("请输入性别：")

            money=input("请输入薪资：")
            while True :
                if money.isdigit():
                    break
                else:
                    print("输入错误，请重新输入！")
                    money = input("请输入薪资：")


            dict[a]["年龄"]=age
            dict[a]["性别"]=sex
            dict[a]["编号"]=input("请输入编号：")
            dict[a]["任职公司"]=input("请输入任职公司：")
            dict[a]["薪资"]=int(money)
            dict[a]["部门编号"]=input("请输入部门编号：")
            return dict[a]
    else:
        dict[a] = {"年龄": 0}
        dict[a]["性别"] = 0
        dict[a]["编号"] = 0
        dict[a]["任职公司"] = 0
        dict[a]["薪资"] = 0
        dict[a]["部门编号"] = 0
        name(a)

while True:
    a=input("请输入姓名：")
    if a=="q" or a=="Q":
        break
    name(a)
    for i in dict:
        print(i,dict[i])







#dict["刘备"]={"年龄":0}
#dict["刘备"]["性别"]=0
#dict["年龄"]="56"
# dict["刘备"]["性别"]="男"
# dict["刘备"]["编号"]="106"
#print(dict["刘备"]["年龄"])







