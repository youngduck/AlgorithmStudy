import sys

n,m=map(int,sys.stdin.readline().split())
data=[list(map(int,sys.stdin.readline().split()))for i in range(n)]

acc=[[0]*(m+1) for i  in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        acc[i][j]=data[i-1][j-1]+acc[i-1][j]+acc[i][j-1]-acc[i-1][j-1]

for k in range(int(sys.stdin.readline())):
    i,j,x,y=map(int,sys.stdin.readline().split())
    print(acc[x][y]-acc[x][j-1]-acc[i-1][y]+acc[i-1][j-1])
    