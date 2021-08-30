import sys
n=int(sys.stdin.readline())
ls=[]
for i in range(n):
    a=int(sys.stdin.readline())
    ls.append(a)
ls.sort()
for i in ls:
    print(i)