#Ackerman函数，因为生成器不大会用，这里就直接愚蠢地用了数组，n太大会崩掉
a=list()
for i in range(0,100):
    templist = list()
    for j in range(0,100):
        templist.append(0)
    a.append(templist)
def Acker(m,n):
    if a[m][n]>0:
        return a[m][n]
    if m==0:
        a[0][n] = n+1
        return a[0][n]
    if n==0:
        a[m][0] =Acker(m-1,1)
        return a[m][0]
    a[m][n] = Acker(m-1,Acker(m,n-1))
    return a[m][n]
print(Acker(2,48))
