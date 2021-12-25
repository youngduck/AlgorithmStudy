import sys
n=int(sys.stdin.readline())

a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

a=sorted(a,key=lambda x:x,reverse=True)
b=sorted(b,key=lambda x:x)

result=0
for i in range(n):
    result=result+a[i]*b[i]
    
print(result)