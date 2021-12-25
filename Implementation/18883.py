import sys

N,M=map(int,sys.stdin.readline().split())

for i in range(1,N*M+1):
    if i % M == 0:
        print(i)
    else:
        print(i,end=' ')