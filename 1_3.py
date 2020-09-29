#线性选择算法
import random
import math
n = 10 #数组长度,可变参数
xarr = list()
temparr = list()#用于生成权值
warr = list()
sum = 0
for i in range(0,n):
    xarr.append(random.randint(0,9))
    temparr.append(random.randint(0,9))
    sum = sum + temparr[i]
for i in range(0,n):
    warr.append(temparr[i]/sum)
#对数组进行排序
#xarr.sort()
for i in range(0,n):
    for j in range(0,i):
        if xarr[i]<xarr[j]:
            temp = xarr[i]
            tempw = warr[i]
            xarr[i] = xarr[j]
            warr[i] = warr[j]
            xarr[j] = temp
            warr[j] = tempw
print("x数列为：",xarr)
print("y数列为：",warr)
wsum = 0
for i in range(0,n):
    if wsum < 0.5 and (1-wsum-warr[i]) < 0.5:
            print("带权中位数是：",xarr[i])
    wsum = wsum + warr[i]