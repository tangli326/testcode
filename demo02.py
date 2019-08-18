jine = input("请输入金额:")
print("输入的金额为：",jine) 

num = jine.count(".")
if num == 0 or num == 1:
    hstr = "0123456789."
    for i in jine:
        print("現在變數 i 的值為 :",i)
        if i not in hstr:
            print("输入的值不合法")
            exit()
    jine = float(jine)  # 强制转换数据类型为小数
    if jine >= 0.01 and jine <= 200:
        print("发送红包成功")
    else:
         print("金额超出范围")
else:
    print("输入的金额不合法，请重新输入！")

dd = range(10) #数列生成器
print(dd)
print(list(dd))  #强制转换成数组


for v in range(1,10):
    for m in range(1,10):
        print(v,"x",m,"=",v*m,end="\t")

