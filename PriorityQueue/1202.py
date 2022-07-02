import sys
import heapq
#가방무게,보석무게 모두 오름차순 정렬.
#가방무게에 들어갈 수 있는 보석들을 최대힙(보석가격)으로 넣어줌


n,k = map(int,sys.stdin.readline().split())


jew=[ list(map(int,sys.stdin.readline().split())) for i in range(n)]
bag=[int(sys.stdin.readline()) for i in range(k)]
jew.sort()
bag.sort()

temp=[]
result=0

for i in bag:
    while(jew and i>=jew[0][0]):
        heapq.heappush(temp,-jew[0][1])
        heapq.heappop(jew)
    if temp:
        result+=heapq.heappop(temp)
    elif not jew:
        break

print(-result)