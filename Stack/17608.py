import sys
from collections import deque

deq = deque()
n=int(sys.stdin.readline())
for i in range(n):
    floor=int(sys.stdin.readline())
    deq.append(floor)

height=0
view = 0

for i in range(n):
    isView=deq.pop()
    if isView>height:
        height=isView
        view+=1
    
print(view)