import random
import math
#以十进制为例
#生成两个大于10位数的十进制数
a = 0
b = 0
for i in range(0,6):
    a = a + random.randint(0,9)*math.pow(10,i)
    b = b + random.randint(0,9)*math.pow(10,i)
#分治法计算两个十进制数的积
a = int(a)
b = int(b)
def cal(num1,num2):
    if num1 < 10 and num2 < 10:
        #个位乘法直接计算
        return num1*num2
    else:
        #大于一位将其拆分成三段
        n = len(str(num1))
        n = int((n-1) / 3) + 1
        u0 = int(num1 % math.pow(10,n))
        u1 = int((num1 % math.pow(10,n*2) - u0)/math.pow(10,n))
        u2 = int((num1 - u1*math.pow(10,n) - u0)/math.pow(10,n*2))
        v0 = int(num2 % math.pow(10,n))
        v1 = int((num2 % math.pow(10,n*2) - v0)/math.pow(10,n))
        v2 = int((num2 - v1*math.pow(10,n) - v0)/math.pow(10,n*2))
        def w(x):
            return cal(int((u0+u1*x+u2*math.pow(x,2))),int((v0+v1*x+v2*math.pow(x,2))))
        wx1 = w(0)
        wx2 = w(-2)
        wx3 = w(2)
        wx4 = w(-1)
        wx5 = w(1)
        w0 = wx1
        w1 = (wx2-wx3-8*(wx4-wx5))/12
        w2 = (-wx2-wx3+16*(wx4+wx5)-30*wx1)/24
        w3 = (-wx2+wx3+2*(wx4-wx5))/12
        w4 = (wx2+wx3-4*(wx4+wx5)+6*wx1)/24
        result = int(w0 + w1*math.pow(10,n) + w2*math.pow(10,n*2) + w3*math.pow(10,n*3) + w4*math.pow(10,n*4))
        return result
print("乘数分别为：",a,b)
print("大数直接相乘的结果：",a*b)
print("采用分治法计算出的结果",cal(a,b))



