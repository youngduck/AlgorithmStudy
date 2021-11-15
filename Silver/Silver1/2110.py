import sys

n,c=map(int,sys.stdin.readline().split())

data=[int(sys.stdin.readline()) for i in range(n)]
data.sort()

result=0
left=1
right=data[-1]
start=data[0]
cnt=1

while left<=right:
    mid=int((left+right)/2)
    for i in data:
        if start+mid <= i:
            cnt+=1
            start=i
    start=data[0]
    if cnt>=c:    
        result=mid
        left=mid+1
        cnt=1
    else:
        right=mid-1
        cnt=1
    

print(result)