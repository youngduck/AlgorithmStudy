import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())

data=[ list(map(int,sys.stdin.readline().rstrip())) for i in range(n)]
direction=[[1,0],[0,-1],[0,1],[-1,0]]

cnt=1
visit=[[0,0]]
start=deque([[0,0]])
while start:
    temp=start.popleft()
    for d in direction:
        move=[d[0]+temp[0],d[1]+temp[1]]
        if ((move[0]<0) or (move[0]>n-1)) or ((move[1]<0) or (move[1]>m-1)):
            continue
        elif data[move[0]][move[1]] == 1:
            start+=[[move[0],move[1]]]
            data[move[0]][move[1]]=data[temp[0]][temp[1]]+1
    if data[n-1][m-1]!=1:
        print(data[n-1][m-1])
        break




