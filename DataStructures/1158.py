import sys

#초깃값
n,k=map(int,sys.stdin.readline().split())
destination=k-1
data=[]
result=[]

#배열
for num in range(1,n+1):
    data.append(num)

while(data):
    result.append(data.pop(destination))
    if len(data)==0:
        break
    destination=(destination+k-1)%(len(data))
    
print("<",end='')
for i in range(len(result)-1):
    print("%d, " %(result[i]),end='')
print(result[-1],end='')
print(">")
    