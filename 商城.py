
# 1.准备一个商品柜
shop = [
    ["联想电脑", 5000],
    ["Mac Pc", 12000],
    ["HUA WEI WATCH", 1200],
    ["海尔洗衣机", 5000],
    ["卫龙辣条", 3.5],
    ["老干妈", 15],
    ["乌江榨菜", 1.5]
]

# 2.准备钱包
while True :
    money = input("请初始化您的余额：￥")
    if money.isdigit() :
        money = int(money)
        if money>=0:
            box=money
            break
        else:
            print("输入非法字符，请重新输入！")
    else:
        print("输入非法字符，请重新输入！")


# 3.空格购物车
mycart = []

# 4.进入商城，领取优惠券
import random
cheap=["联想电脑5折优惠券","老干妈6折优惠券","乌江榨菜9折优惠券"]
a=random.randint(0,2)
b=a     #优惠券编号
a= cheap[a]
print("您已领取：",a)
print()

# 5.正常买东西

print("----------------欢迎光临----------------")
# 展示商品
for key,value in enumerate(shop):
    print(key,value)
print("---------------------------------------")
# 买东西
while True:
    print("***输入k/K查看商品列表***输入q/Q退出系统***")
    chose = input("请输入您要的商品编号：")
    if chose == "k" or chose == "K" :
        print("----------------欢迎光临----------------")
        # 展示商品
        for key, value in enumerate(shop):
            print(key, value)
        print("---------------------------------------")
    elif chose.isdigit():     #  这个商品是否存在
        chose = int(chose)
        if chose >= len(shop):  # len(shop) = 7
            print("该商品不存在！请重新输入：")
        elif chose < 0:
            print("该商品不存在！请重新输入：")
        else:                # 看钱够不够
            if money < shop[chose][1]:
                print("对不起，您的余额不足,请选择其他商品")
            elif b==0 and chose==0:
                mycart.append(shop[chose])
                money = money - shop[chose][1]*0.5
                money = round(money,2)
                print("恭喜，添加购物车成功！您的余额还剩：￥", money, "!")
            elif b==1 and chose==5:
                mycart.append(shop[chose])
                money = money - shop[chose][1]*0.6
                money = round(money, 2)
                print("恭喜，添加购物车成功！您的余额还剩：￥", money, "!")
            elif b==2 and chose==6:
                mycart.append(shop[chose])
                money = money - shop[chose][1]*0.9
                money = round(money, 2)
                print("恭喜，添加购物车成功！您的余额还剩：￥", money, "!")
            else:
                mycart.append(shop[chose])
                money = money - shop[chose][1]
                money = round(money, 2)
                print("恭喜，添加购物车成功！您的余额还剩：￥", money, "!")
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法！请重新输入!")
# 结算,打印购物小条
import time
time =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())      #当前时间
print()
print("以下是您的购物小条，请查收：")
print("-----------购物小条-----------")
count = 0
for key,value in enumerate(mycart):     #遍历购物车
    print(key,value)

for i in mycart:                    #应付金额
    count+=float(i[1])
print()
print("应付金额：￥",round(count,2))
print("实付金额：￥",round(box-money,2))
print("优惠：￥",round(count-box+money,2))
print("您的余额为：￥",round(money,2))
print(time)
print("----------------------------")

