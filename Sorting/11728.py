import sys
import heapq

a_len,b_len=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
a_pointer,b_pointer=0,0
result=[]

while(a_pointer!=a_len or b_pointer!=b_len):
    if a_pointer==a_len:
        result.append(b[b_pointer])
        b_pointer+=1
    elif b_pointer==b_len:
        result.append(a[a_pointer])
        a_pointer+=1
    else:
        if(a[a_pointer]>=b[b_pointer]):
            result.append(b[b_pointer])
            b_pointer+=1
            
        elif (b[b_pointer]>=a[a_pointer]):
            result.append(a[a_pointer])
            a_pointer+=1

    
print(*result)
