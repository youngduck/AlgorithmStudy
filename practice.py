import heapq

a=[5,7,2,1]
b=[10,6,4]

heapq.heapify(a)
heapq.heappush(b,a[0])

while(b):
    print(b)
    heapq.heappop(b)