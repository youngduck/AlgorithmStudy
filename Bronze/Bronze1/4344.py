C=int(input())
for i in range(C):
    N=list(map(int,input().split()))
    s=0
   
    
    result=0
    n=N.pop(0)
    for i in  N:
        s=s+i
    
    a=0
    for i in N:
        if i > s/n:
            a+=1
    result=a/n*100
    print('%.3f%%' %result)    