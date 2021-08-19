import sys

N,K=map(int,sys.stdin.readline().split())

coin=[]
for i in range(N):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)

cnt=0

for i in range(N):
    if K<coin[i]:
        continue
    else:
        part=K//coin[i]
        cnt+=part
        K-=coin[i]*part
        if K == 0:
            break
print(cnt)