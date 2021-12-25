import sys
from itertools import accumulate
n,m=map(int,sys.stdin.readline().split())

data=list(map(int,sys.stdin.readline().split()))
result=list(accumulate(data))
for t in range(m):
    start,end=map(int,sys.stdin.readline().split())
    if start!=1:
        print(result[end-1]-result[start-2])
    else:
        print(result[end-1])
