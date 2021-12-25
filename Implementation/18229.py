import sys

N,M,K=map(int,sys.stdin.readline().split())
people=[0]*N
escape=False
data=[list(map(int,sys.stdin.readline().split())) for i in range(N)]


for j in range(M):
    for i in range(N):
        people[i]+=data[i][j]
        if people[i]>=K:
            cnt=j+1
            num=i+1
            escape=True
            break
    if escape==True:
        break


print(num,cnt)

        
