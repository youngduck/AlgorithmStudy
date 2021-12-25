import sys
a,b=map(int,sys.stdin.readline().split())

if b>a:
    a,b=b,a

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

maxnum=gcd(a,b)
minnum=a*b//maxnum

print(maxnum)
print(minnum)