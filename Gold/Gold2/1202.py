import sys
import heapq

N,K=map(int,sys.stdin.readline().split())

jew=[]
bag=[]
result=0

#보석(무게,가격)
for i in range(N):
    jew.append(list(map(int,sys.stdin.readline().split())))

#가방
for i in range(K):
    heapq.heappush(bag,int(sys.stdin.readline()))

print(bag[0])
while len(bag)!=0:
    t=list(filter(lambda x:x[0]<=bag[0],jew))
    t=sorted(jew,key=lambda x:x[1],reverse = True)
    new=list(filter(lambda x:x[0]>3,jew))
    heapq.heappop(bag)
    print(jew)
    print(new)
    print(t)
    result+=t[0][1]




print(result)