#漂亮打印
import random
import math
M = 40 #每行最多打印的字符数量
wordlenlist = list() #字符长度数组
n = 10 #单词数量
c = list()
pos = list()
for i in range(0,n):
    wordlenlist.append(random.randint(1,15))
    c.append(0)
    pos.append(0)
c.append(0)
pos.append(0)
print(wordlenlist)
#计算将第i到j的单词总长
def wordlen(i,j):
    sum=0
    for k in range(i,j):
        sum = sum + wordlenlist[k]
    return sum
#计算将第i到j的单词放到一行的空格
def space(i,j):
    return M - j + i + wordlen(i,j)
#结果打印到一行上的值
def exp(i,j):
    if space(i,j)<0:
        return 1000000
    elif j==n:
        return 0
    else:
        return math.pow(space(i,j),3)
def beaty(len):
    if len == 0:
        return 0
    tempmin = 0
    for i in range(1,len):
        temp = beaty(i-1)+exp(i,len)
        if temp<tempmin or tempmin==0:
            tempmin=temp
    return tempmin
print(beaty(2))