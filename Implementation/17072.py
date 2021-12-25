import sys

def I(r,g,b):
    result=2126*r+7152*g+722*b
    if result >=0 and result<510000:
        return chr(35)
    elif result>=510000 and result <1020000:
        return chr(111)
    elif result>=1020000 and result <1530000:
        return chr(43)
    elif result>=1530000 and result <2040000:
        return chr(45)
    else:
        return chr(46)

n,m=map(int,sys.stdin.readline().split())

data=[]

for i in range(n):
    data=list(map(int,sys.stdin.readline().split()))
    for j in range(m):
        print(I(data[3*j],data[3*j+1],data[3*j+2]),end='')
    print('')
