import sys
from itertools import combinations

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())

data=list(map(int,sys.stdin.readline().split()))
road=max(data)
data=set(data)
num=list(range(road+1))

a=list(combinations(num,k))

result=[]
for i,j in a:
    sum=0
    for x in data:
        dis=min(abs(x-i),abs(x-j))
        sum+=dis
    result.append(sum)

print(min(result))


