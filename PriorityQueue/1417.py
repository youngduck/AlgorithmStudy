import sys

n=int(sys.stdin.readline())
num=int(sys.stdin.readline())
data=[]
cnt=0

if n ==1:
    cnt=0
else:
    for i in range(n-1):
        data.append(int(sys.stdin.readline()))
    while num <= max(data):
        data[data.index(max(data))]-=1
        num+=1
        cnt+=1




print(cnt)