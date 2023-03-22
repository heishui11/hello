#第七章 input的使用
message =input('qingshurunimende xinxi')
print(message)
#练习7-1
message1 = input('qingshuruninxiangzhulindeqiche:')
message1 += input('\n,wokeyibangnitiaoxuan')
message2 =input('qingshurupailiang')
message2 = int(message2)
print(f"{message1},\nmessage2{message2}")
#练习7-4
message3 = input('请输入您您的年龄:')
while int(message3) >0:
    if int(message3)<=3:
        print("nikeyimianfeiruyuancanguan!!!")
        message3=input('请输入您您的年龄:')
        continue
    elif int(message3)>3 and int(message3)<=13:
        print("nin yao jiao fei 5 yuan")
        message3=input('请输入您您的年龄:')
        continue
    else :
        print('nin yao jiao fei 15 yuan')
        message3=input('请输入您您的年龄:')
        continue
#列表转移
banji =['xiaohong','xiaoming','xiaoli','xiaobai']
banji1 =[]
for xuesheng in banji:
    print(banji)
while banji:
    xuesheng = banji.pop()
    banji1.append(xuesheng)
    print(banji1)
