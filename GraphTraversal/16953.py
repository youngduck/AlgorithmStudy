import sys

A,B=map(int,sys.stdin.readline().split())
cnt=1
while True:
    if A==B:
        break
    elif A>B:
        cnt=-1
        break
    elif B%10 == 1:
        B=int(str(B)[:-1])
        cnt+=1    
    elif B%2 == 0:
        B=int(B/2)
        cnt+=1   
    else:
        cnt=-1
        break
            
print(cnt)