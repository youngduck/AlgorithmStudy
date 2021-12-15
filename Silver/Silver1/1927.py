import sys
import heapq

data=[]

for n in range(int(sys.stdin.readline())):
    i = int(sys.stdin.readline())
    if i == 0 and len(data)==0:
        print(0)
    elif i ==0:
        print(heapq.heappop(data))
    else:
        heapq.heappush(data,i)

