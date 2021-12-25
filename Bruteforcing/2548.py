import sys

n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data.sort()

#중앙값 문제 
#y=|x-1|+|x-3|+|x-6| 그래프에서 x=3일때 최소값.

if n % 2 == 0:
    print(data[n//2-1])
else:
    print(data[n//2])