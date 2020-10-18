#线性选择算法
import random
import math
#数据生成过程
n = 15 #数组长度,可变参数
xarr = list()#x数组
temparr = list()#用于生成权值
warr = list()#w数组
sum = 0
for i in range(0,n):
    randomp = random.randint(0,100)
    #防止出现重复数
    while randomp in xarr:
        randomp = random.randint(0,100)
    xarr.append(randomp)
    temparr.append(random.randint(0,100))
    sum = sum + temparr[i]
for i in range(0,n):
    warr.append(temparr[i]/sum)
print("原始数据")
for i in range(0,n):
    print("值:",xarr[i],"权:",warr[i])



#找出带权中位数
wsum = 0
curid = 0
for i in range(1,n):
    if xarr[i]>xarr[curid]:
        curid = i
    else:
        wsum = wsum + warr[i]
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
#求数组中位数的函数
def select(arr):
    #将数组分割为n/5个数组
    arrlength = int(len(arr)/5)
    if arrlength>1:
        arrlist = []
        for i in range(0,arrlength):
            temparr = []
            arrlist.append(temparr)
        for i in range(0,5):
            for j in range(0,arrlength):
                try:
                    arrlist[j].append(arr[j*5+i])
                except:
                    pass
        #中位数数组
        medianlist =[]
        for i in range(0,arrlength):
            medianlist.append(select(arrlist[i]))
        #递归结束条件
        if len(medianlist)<6:
            for x in range(0,len(medianlist)):
                for y in range(0,x):
                    if xarr[x]<xarr[y]:
                        temp = medianlist[x]
                        medianlist[x] = medianlist[y]
                        medianlist[y] = temp
            return medianlist[2]
        else:
            return select(medianlist)
    else:
        return arr[0]
print(select(xarr))
# print("排序结果")
# for i in range(0,n):
#     print("值:",xarr[i],"权:",warr[i])
# wsum = 0
# for i in range(0,n):
#     if wsum < 0.5 and (1-wsum-warr[i]) < 0.5:
#             print("带权中位数是：",xarr[i])
#     wsum = wsum + warr[i]