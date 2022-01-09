import sys

n,m=map(int,sys.stdin.readline().split())

data=[ list(map(int,sys.stdin.readline().split())) for i in range(n)]
prefixSum=[[0]*(n+1) for i in range(n+1)]

#누적 합 넣어주기
for i in range(1,n+1):
    for j in range(1,n+1):
        prefixSum[i][j]=data[i-1][j-1]+prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]

#출력
for i in range(m):
    start_x,start_y,end_x,end_y=map(int,sys.stdin.readline().split())
    result=prefixSum[end_x][end_y]-prefixSum[start_x-1][end_y]-prefixSum[end_x][start_y-1]+prefixSum[start_x-1][start_y-1]
    print(result)
    