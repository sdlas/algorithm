#最长递增子序列
import random
import math
n = 10 #数组长度,可变参数
# 遍历的数组
a = list()
# 存储结尾元素最小值
b = list()
for i in range(0,n):
    a.append(random.randint(0,9))
print(a)
k = 1
b.append(a[0])
def binary(x):
    if x<b[0]:
        return 0
    for i in range(1,len(b)):
        if x>b[i-1] and x<b[i]:
            return i
    return 0
for i in range(1,n):
    if a[i]>b[k-1] or a[i]==b[k-1]:
        k = k+1
        b.append(a[i])
    else:
        b[binary(a[i])] = a[i]
print(b)
print(k)
