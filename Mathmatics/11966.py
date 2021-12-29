import sys

n=int(sys.stdin.readline())
result=1

while(n>=2):
    if(n%2==0):
        n=n/2
    else:
        result=0
        break

print(result)