import sys

def push(data,num):
    data.append(num)
    return

def front(data):
    if len(data):
        return data[0]
    else:
        return -1

def back(data):
    if len(data):
        return data[-1]
    else:
        return -1

def size(data):
    return len(data)
    
def empty(data):
    if len(data):
        return 0
    else:
        return 1
    
def pop(data):
    if len(data):
        return data.pop(0)
    else:
        return -1

data=[]

for i in range(int(sys.stdin.readline())):
    order=sys.stdin.readline().split()
    if order[0] == "push" :
        push(data,int(order[1]))
    if order[0] == "pop" :
        print(pop(data))
    if order[0] == "size" :
        print(size(data))
    if order[0] == "empty" :
        print(empty(data))
    if order[0] == "front" :
        print(front(data))
    if order[0] == "back" :
        print(back(data))