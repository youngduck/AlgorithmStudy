import sys
from collections import deque

#입력값
n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())

data={}
#양방향 노드 만들기
for _ in range(1,n+1):
    data[_]=[]
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    data[x].append(y)
    data[y].append(x)


#BFS
visit=[]
queue=deque()
queue.append((0,a))
find = False
result=-1

while queue:
    edge,q=queue.popleft()
    if q not in visit:
        visit.append(q)
        temp=list(set(data[q])-set(visit))
        for i in data[q]:
            if b is i:
                result=edge+1
                break
            else:
                queue.append((edge+1,i))
        if find:
            break  

print(result)
