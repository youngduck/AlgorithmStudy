import sys
from collections import deque
n=int(sys.stdin.readline())

data={}
parents=[0]*(n+1)


for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    if a in data:
        data[a].append(b)
    else:
        data[a]=[b]
    if b in data:
        data[b].append(a)
    else:
        data[b]=[a]

#BFS
queue=deque([1])
while queue:
    n=queue.popleft()
    for i in data[n]:
        if parents[i] == 0:
            parents[i]=n
            queue.append(i)

for i in parents[2:]:
    print(i)