import heapq
import sys

data=[]

for i in range(int(sys.stdin.readline())):
    num=int(sys.stdin.readline())
    if num ==0:
        if len(data):
            maxNum=heapq.heappop(data)
            print(-maxNum)
        else:
            print(0)
    else:
        heapq.heappush(data,-num)
