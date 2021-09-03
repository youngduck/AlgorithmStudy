import sys
import heapq

n,m=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))

result=0
heapq.heapify(data)
for i in range(m):
    min=heapq.heappop(data)+heapq.heappop(data)
    heapq.heappush(data,min)
    heapq.heappush(data,min)
print(sum(data))
# import sys
# n,m=map(int,sys.stdin.readline().split())

# data=list(map(int,sys.stdin.readline().split()))
# for i in range(m):
#     data.sort()
#     min=data[0]+data[1]
#     data[0]=min
#     data[1]=min
# print(sum(data))