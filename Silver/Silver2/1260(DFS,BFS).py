import sys
from collections import deque

node,edge,start=map(int,sys.stdin.readline().split())

#노드,양방향 간선 구현
data={}
#edge가 단한개일때를 위해 빈것도 만들어줘야됨
for i in range(1,node+1):
    data[i]=[]
for i in range(edge):
    a,b=map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)  
#DFS
visit=[]
stack=deque([start])

while stack:
    n=stack.pop()
    if n not in visit:
        visit.append(n)
        temp=list(set(data[n])-set(visit))
        temp.sort(reverse=True)
        stack+=temp
print(*visit)


#BFS
visit=[]
queue =deque([start])

while queue:
    n=queue.popleft()
    if n not in visit:
        visit.append(n)
        temp=list(set(data[n])-set(visit))
        temp.sort()
        queue+=temp
        
print(*visit)