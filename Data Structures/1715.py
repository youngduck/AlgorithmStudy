import heapq
N=int(input())
data=[]

for _ in range(N):
    heapq.heappush(data,int(input()))

check=0

while len(data) != 1:
    sum = (heapq.heappop(data)+heapq.heappop(data))
    check +=sum
    heapq.heappush(data,sum)

print(check)
