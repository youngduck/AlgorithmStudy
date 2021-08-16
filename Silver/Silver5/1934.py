import sys
t=int(sys.stdin.readline())
def gcd(a,b):
    if a>b:
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    else:
        if a == 0 :
            return b
        else:
            return gcd(a,b%a)
        
    
for i in range(t):
    a,b=map(int,sys.stdin.readline().split())
    result=a*b//gcd(a,b)
    print(result)