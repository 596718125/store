dict={
    "吃鸡":{"冲锋枪":{"UMP45":".45口径子弹","野牛冲锋枪":"9毫米子弹","Vector":"9毫米子弹"},
          "突击步枪":{"M416":"5.56毫米子弹","AKM":"7.62毫米子弹","SCAR-L":"5.56毫米子弹","GROZA":"7.62毫米子弹"},
          "栓动狙击":{"Kar98K":"7.62毫米子弹","M24":"7.62毫米子弹","AWM":".300马格南子弹"},
          "射手步枪":{"SKS":"7.62毫米子弹","VSS":"9毫米子弹","Mini14":"5.56毫米子弹","Mk14":"7.62毫米子弹"},
          "散弹枪":{"S686":"12口径散弹","S1897":"12口径散弹","S12K":"12口径散弹","DBS":"12口径散弹"},
          "轻机枪":{"M249":"5.56毫米子弹","DP-28":"7.62毫米子弹","MG3":"7.62毫米子弹"},
          "手枪":{"沙漠之鹰":".45口径子弹","P1911":".45口径子弹","R1895":"7.62毫米子弹","蝎式手枪":"9毫米子弹","短管散弹":"12口径散弹","信号枪":"信号弹"}
          },
    "王者":{"上海路":{"羽绒教育元区":"狼腾测试员"}}
#     键  :  值
      }
 #通过键来获取值，


while True:
    print("----------------------")
    for a, b in enumerate(dict):
        print(b)
    print("----------------------")

    into=input("请输入游戏名称")#input默认是字符串类型
    if  into == "吃鸡":
        while True:
            print("----------------------")
            for a, b in enumerate(dict[into]):
                print(b)
            print("----------------------")
            num=input("请选择武器类型")

            if num=="冲锋枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name=input("请输入武器名称：")
                if name=="UMP45":
                    print(dict[into][num][name])
                elif name=="野牛冲锋枪":
                    print(dict[into][num][name])
                elif name=="Vector":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num=="突击步枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "M416":
                    print(dict[into][num][name])
                elif name == "AKM":
                    print(dict[into][num][name])
                elif name == "SCAR-L":
                    print(dict[into][num][name])
                elif name == "GROZA":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num == "栓动狙击":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "Kar98K":
                    print(dict[into][num][name])
                elif name == "M24":
                    print(dict[into][num][name])
                elif name == "AWM":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num=="射手步枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "SKS":
                    print(dict[into][num][name])
                elif name == "VSS":
                    print(dict[into][num][name])
                elif name == "Mini14":
                    print(dict[into][num][name])
                elif name == "Mk14":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num == "散弹枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "S686":
                    print(dict[into][num][name])
                elif name == "S1897":
                    print(dict[into][num][name])
                elif name == "S12K":
                    print(dict[into][num][name])
                elif name == "DBS":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num == "轻机枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "M249":
                    print(dict[into][num][name])
                elif name == "DP-28":
                    print(dict[into][num][name])
                elif name == "MG3":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")

            elif num == "手枪":
                print("----------------------")
                for a, b in enumerate(dict[into][num]):
                    print(b)
                print("----------------------")
                name = input("请输入武器名称：")
                if name == "沙漠之鹰":
                    print(dict[into][num][name])
                elif name == "P1911":
                    print(dict[into][num][name])
                elif name == "R1895":
                    print(dict[into][num][name])
                elif name == "蝎式手枪":
                    print(dict[into][num][name])
                elif name == "短管散弹":
                    print(dict[into][num][name])
                elif name == "信号枪":
                    print(dict[into][num][name])
                else:
                    print("暂无该记录！")
            else:
                print("无此类型")
    else:
        print("暂不支持")

#输出键、值
'''
for a,b in enumerate(dict["吃鸡"]["冲锋枪"]):
    print(b,dict["吃鸡"]["冲锋枪"][b])
'''