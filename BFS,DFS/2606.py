import sys
from collections import deque

computer_num=int(sys.stdin.readline())
edge_cnt=int(sys.stdin.readline())
edge={}
computer=[]
#초깃값 설정
for i in range(1,computer_num+1):
    edge[i]=[]
    computer.append(i)

#edge넣어주기
for i in range(edge_cnt):
    num1,num2=map(int,sys.stdin.readline().split())
    edge[num1].append(num2)
    edge[num2].append(num1)

#BFS로 구현.
visit=[]
queue=deque([1])
while queue:
    n=queue.popleft()
    visit.append(n)
    temp=list(set(edge[n])-set(visit))
    temp.sort()
    queue+=temp


print(len(set(visit))-1)