from itertools import combinations
import sys

n,s=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))
cnt=0

for i in range(1,n+1):
    com=list(combinations(data,i))
    print(i)
    for j in com:
        if sum(j)==s:
            cnt+=1

print(cnt)