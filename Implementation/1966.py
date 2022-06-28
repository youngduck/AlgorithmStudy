import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n,m=map(int,sys.stdin.readline().split())
    queue=deque(list(map(int,sys.stdin.readline().split())))
    ord=0
    while queue:
        big=max(queue)
        front = queue.popleft()
        m-=1

        if big == front:
            ord+=1
            if m<0:
                print(ord)
                break
        else:
            queue.append(front)
            if m<0:
                m=len(queue)-1