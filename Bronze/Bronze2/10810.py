import sys

N,M=map(int,sys.stdin.readline().split())
bag=[0]*N

for m in range(M):
    start,end,num=map(int,input().split())
    for i in range(start-1,end):
        bag[i]=num

print(*bag)