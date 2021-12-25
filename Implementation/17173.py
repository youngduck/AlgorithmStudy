import sys

n,m=map(int,sys.stdin.readline().split())
num_list=list(map(int,sys.stdin.readline().split()))

data=[False]*(n+1)
result=0

for i in num_list:
    for j in range(i,n+1,i):
        if data[j] == False:
            data[j]=True
            result+=j

print(result)
