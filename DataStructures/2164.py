import sys
from collections import deque

n=int(sys.stdin.readline())
queue=deque([i for i in range(1,1+n)])

while(len(queue)>1):
    queue.popleft()
    queue.rotate(-1)

print(queue[0])