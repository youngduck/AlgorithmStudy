import sys

n=int(sys.stdin.readline())
queue=[]


for i in range(n):
    do=[]
    do=sys.stdin.readline().split()
    
    if do[0]=="push":
        queue.append(do[1])
    elif do[0] =="front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif do[0] == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif do[0] == "size":
        print(len(queue))
    elif do[0] == "empty":
        print(1-int(bool(queue)))
    elif do[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        pass