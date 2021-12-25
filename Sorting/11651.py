import sys
n=int(sys.stdin.readline())
data=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

data=sorted(data,key=lambda x:(x[1],x[0]))

for i in data:
    print("%d %d" %(i[0],i[1]))