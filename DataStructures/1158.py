import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())

deq=deque(list(range(1,n+1)))

print('<',end='')
while (deq):
    deq.rotate(-k)
    if(len(deq)!=1):
        print(deq.pop(),end=', ')
    else:
        print(deq.pop(),end='')
print('>',end='')
