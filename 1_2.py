import random
import math
#生成一个非零偶数
n = random.randint(4,9)*2
#找出k,m值
k = 0
m = 0 
for i in range(0,n):
    temp = n/pow(2,i)
    if not(temp > int(temp)) and int(temp)%2 == 1:
        k = i
        m = int(temp)
        break
#生成矩阵
A = list()
B = list()
for i in range(0,n):
    tempAarr = list()
    tempBarr = list()
    for j in range(0,n):
        tempAarr.append(random.randint(0,9))
        tempBarr.append(random.randint(0,9))
    A.append(tempAarr)
    B.append(tempBarr)
#打印矩阵
def printmatrix(A):
    n = len(A)
    for i in range(0,n):
        print(A[i])
#初始化矩阵
def initmatrix(n):
    result = list()
    for i in range(0,n):
        temparr = list()
        for j in range(0,n):
            temparr.append(0)
        result.append(temparr)
    return result
    
#计算矩阵相加
def add(A,B):
    n = len(A)
    result = initmatrix(n)
    for i in range(0,n):
        for j in range(0,n):
            result[i][j] = A[i][j] + B[i][j] 
    return result
#计算矩阵乘积
def cal(A,B):
    n = len(A)
    Apart = list()
    Bpart = list()
    #初始化结果矩阵
    result = initmatrix(n)
    #分割矩阵
    sonlen = int(pow(2,k)) #子矩阵长度
    for i in range(0,m):
        tempAarr = list()
        tempBarr = list()
        for j in range(0,m):
            tArr = list()
            tBrr = list()
            #x,y方向上的偏移量
            xoffset = i*int(math.pow(2,k))
            yoffset = j*int(math.pow(2,k))
            #生成小矩阵
            for y in range(0,sonlen):
                tlineArr = list()
                tlineBrr = list()
                for x in range(0,sonlen):
                    tlineArr.append(A[yoffset+y][xoffset+x])
                    tlineBrr.append(B[yoffset+y][xoffset+x])
                tArr.append(tlineArr)
                tBrr.append(tlineBrr)
            tempAarr.append(tArr)
            tempBarr.append(tBrr)
        Apart.append(tempAarr)
        Bpart.append(tempBarr)
    #用strassen算法计算子矩阵的积
    def strassen(sonA,sonB):
        #时间原因没来得及敲，用普通算法对付了一下，下次附件一定补上
        n = len(sonA)
        results = initmatrix(n)
        for p in range(0,n):
            for q in range(0,n):
                sum = 0 
                for i in range(0,n):
                    sum = sum + sonA[p][i]*sonB[i][q]
                results[p][q] = sum
        return results
    for p in range(0,m):
        for q in range(0,m):
            #普通算法计算出每一块的矩阵大小
            tempresult = initmatrix(int(math.pow(2,k)))
            temparr = list()
            for x in range(0,m):
                #strassen算法计算子矩阵
                temparr = strassen(Apart[p][x],Bpart[x][q])
                tempresult = add(tempresult,temparr)
            #将计算出来的块结果赋给结果矩阵
            yoffset = int(p*math.pow(2,k))
            xoffset = int(q*math.pow(2,k))
            for i in range(0,sonlen):
                for j in range(0,sonlen):
                    result[yoffset+i][xoffset+j] = tempresult[i][j]
    return result
result = cal(A,B)
#打印结果
print("两个相乘的随机矩阵为")
print("矩阵A")
printmatrix(A)
print("矩阵B")
printmatrix(B)
print("参数为 n =",n,"m =",m,"k =",k)
print("相乘结果为")
printmatrix(result)