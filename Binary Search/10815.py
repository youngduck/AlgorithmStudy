import sys

n=int(sys.stdin.readline())
data=set(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
for i in list(map(int,sys.stdin.readline().split())):
    if i in data:
        print(1,end=' ')
    else:
        print(0,end=' ')