import sys

N,K=map(int,sys.stdin.readline().split())

jew=[]
bag=[]
result=0
for i in range(N):
    jew.append(list(map(int,sys.stdin.readline().split())))

for i in range(K):
    bag.append(int(sys.stdin.readline()))

bag.sort()
jew=sorted(jew,key=lambda x:x[1],reverse=True)
check=[False]*len(jew)

for i in bag:
    for j in range(len(jew)):
        if i>=jew[j][0] and check[j] == False:
            result+=jew[j][1]
            check[j]=True
            break




print(result)