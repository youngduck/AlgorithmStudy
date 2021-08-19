import sys
from collections import deque

n=int(sys.stdin.readline())
data=deque([])

def push(num):
    data.append(num)
def pop():
    if len(data)== 0:
        print(-1)
    else:
        print(data.popleft())
def size():
    print(len(data))
def empty():
    if len(data)== 0:
        print(1)
    else:
        print(0)
        
def front():
    if len(data)==0:
        print(-1)
    else:
        print(data[0])
def back():
    if len(data)==0:
        print(-1)
    else:
        print(data[-1])

for i in range(n):  
    word=sys.stdin.readline().split()
    command=word[0]
    num=word[-1]  
    if command == 'push':
        push(num)
    if command == 'pop':
        pop()
    if command == 'size':
        size()
    if command == 'empty':
        empty()
    if command == 'front':
        front()
    if command == 'back':
        back()