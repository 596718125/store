#实现输入10个数字，并打印10个数的求和结果
'''
a=0
i=1
while i<=10:
    print("请输入第",i,"个数")
    num=input()
    num=int(num)
    a+=num
    i+=1
print("总和：",a)
'''
#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
max=0
count=0
avg=0
n=1
while n<=10:
    print("请输入第", n, "个数")
    m = input()
    m = int(m)
    count+= m
    if m>max:
        max=m
    avg=round(count/n,2)
    n += 1
print("最大值：", max)
print("总和：",count)
print("平均数:",avg)
'''
#使用random模块，如何产生 50~150之间的数？
'''
import random
n=random.randint(50,150)
print(n)
'''
#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
a=input("请输入第一条边：")
a=int(a)
b=input("请输入第二条边：")
b=int(b)
c=input("请输入第三条边：")
c=int(c)
if ((a+b)>c)&((a+c)>b)&((b+c)>a) :
    if (a==b)|(a==c)|(b==c) :
        print("是等边三角形");
    elif (a==b)&(b==c) :
        print("是等边三角形");
    elif (a*a==b*b+c*c)|(b*b==a*a+c*c)|(c*c==a*a+b*b) :
        print("是直角三角形");
    else :
        print("是普通三角形");
else:
    print("不能形成三角形")
'''
#有以下两个数，使用+，-号实现两个数的调换。
#   A=56
#   B=78
#实现效果：
#   A=78
#   B=56
'''
a=56
b=78
print(a,b)
a=a+b
b=a-b
a=a-b
#a,b=b,a
print(a,b)
'''
#实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
user='root'
pwd='admin'
i=1
a=input("请输入用户名：")
if a!=user :
    print("用户名错误")
else:
    while i<=3 :
        b=input("请输入密码：")
        if b!=pwd :
            print("密码错误，请重新输入！",i)
            i+=1
        else:
            print("登录成功")
            break
        if i>3 :
            print("输入错误密码3次，退出系统！")
'''
#编程实现下列图形的打印
'''
i=1
while i<8 :
    j=0
    k=8-i
    while j<k :
        print(end="  ")
        j+=1
    while k<8 :
        print("*",end="   ")
        k+=1
    i+=1
    print()
'''
#使用while循环实现99乘法表的打印
'''
i=1
while i<=9 :
    j=1
    while j<=i :
        print(i,"*",j,"=",i*j,end="  ")
        j+=1
    i+=1
    print()
'''
#编程实现99乘法表的倒叙打印
'''
i=9
while i>0 :
    j=1
    while j <=i:
        print(j, "*", i, "=", i * j, end="   ")
        j += 1
    i-=1
    print()
'''
#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出
'''
i=1
n=0
while i :
    n+=3
    if n>=20 :
        break
    else:
        n-=2
    i+=1
print("第",i,"天能出来")
'''
#判断下列变量命名是否合法
'''
char="root"
Oax_li="root"
fLul="root"
BYTE="root"
T_T="root"
print()
#Cy%ty，$123，3_3 不合法
'''
#继续完成上午的猜数字游戏的需求功能。
#添加计数打印功能
#添加次数金币功能和锁定系统功能
'''
import random
num=random.randint(0,100)
money=100
i=0
while money :
   i+=1
   into=input("猜猜我是谁：")
   into=int(into)
   if into >num :
       print("大了")
   elif into <num :
       print("小了")
   else:
       print("-------------------------------")
       money-=10
       print("恭喜你才对了，答案是：",num)
       print("共猜了：",i,"次")
       print("金币剩余：",money)
       print("-------------------------------")
       break
   money-=10
   if money ==0:
       print("-------------------------------")
       print("金币用完了")
       print("-------------------------------")
'''
#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
i=1
num=0
while i<=20 :
    j=i
    a = 1
    while j :
        a*=j
        j-=1
    i+=1
    num+=a
print(num)
'''