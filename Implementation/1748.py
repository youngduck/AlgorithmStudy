import sys

n=int(sys.stdin.readline())
i=1
len=1
result=0

while(i<=n):
    if(i*10-1<n):
        result+=(i*10-i)*len
    else:
        result+=(n-i+1)*len  
    i*=10
    len+=1
    
print(result)