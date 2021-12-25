import sys

a=list(sys.stdin.readline().rstrip())
b=list(sys.stdin.readline().rstrip())
data=[]

#초기 세팅
for i in range(8):
    data.append(int(a[i]))
    data.append(int(b[i]))


for i in range(15,1,-1):
    for j in range(i):
        data[j]=data[j]+data[j+1]

print(data[0]%10,data[1]%10,sep='')